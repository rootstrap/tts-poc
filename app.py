import io

import streamlit as st

from utils.elevenlabs import get_elevenlabs_client, get_elevenlabs_tts
from utils.llm import get_chat_response, get_openai_client
from utils.message_cleaner import message_cleaner

st.title("Text-To-Speech Bot")

# Load API keys from environment variables
if "OPENAI_API_KEY" not in st.session_state:
    st.session_state["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
if "ELEVENLABS_API_KEY" not in st.session_state:
    st.session_state["ELEVENLABS_API_KEY"] = st.secrets["ELEVENLABS_API_KEY"]

# Create OpenAI and ElevenLabs clients
if "openai_client" not in st.session_state:
    st.session_state["openai_client"] = get_openai_client(
        api_key=st.session_state["OPENAI_API_KEY"]
    )
if "elevenlabs_client" not in st.session_state:
    st.session_state["elevenlabs_client"] = get_elevenlabs_client(
        api_key=st.session_state["ELEVENLABS_API_KEY"]
    )

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = st.secrets["OPENAI_MODEL"]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

    # Display audio messages from history on app rerun
    if message.get("audio"):
        st.audio(message["audio"], format="audio/mpeg")

# Accept user input
if prompt := st.chat_input("Enter your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        llm_response = get_chat_response(
            client=st.session_state["openai_client"],
            model=st.session_state["openai_model"],
            messages=message_cleaner(st.session_state.messages),
        )
        response = st.write_stream(llm_response)

    # Get TTS response from ElevenLabs
    tts_audio = get_elevenlabs_tts(
        client=st.session_state["elevenlabs_client"],
        text=response,
        voice="JBFqnCBsd6RMkjVDRZzb",
        # lang=st.secrets["ELEVENLABS_LANG"],
    )

    # Display TTS audio in the app
    st.audio(tts_audio, format="audio/mpeg")

    # Add assistant message to chat history
    st.session_state.messages.append(
        {"role": "assistant", "content": response, "audio": tts_audio}
    )
