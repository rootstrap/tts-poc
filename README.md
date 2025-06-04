# Text-To-Speech Chatbot

A Streamlit-based web application that combines OpenAI's chat capabilities with ElevenLabs' text-to-speech technology to create an interactive conversational experience with audio responses.

## Features

- Interactive chat interface built with Streamlit
- AI-powered responses using OpenAI's language models
- Text-to-speech conversion using ElevenLabs
- Chat history persistence during session
- Audio playback of AI responses
- Stream-based response display

## Prerequisites

- Python 3.10 or higher
- OpenAI API key
- ElevenLabs API key

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/tts-poc.git
cd tts-poc
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Set up your environment variables:
   - Create a `.streamlit/secrets.toml` file with the following content:
   ```toml
   OPENAI_API_KEY = "your-openai-api-key"
   ELEVENLABS_API_KEY = "your-elevenlabs-api-key"
   OPENAI_MODEL = "gpt-3.5-turbo"  # or your preferred model
   ```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in your terminal (typically `http://localhost:8501`)

3. Enter your message in the chat input and press Enter to receive both text and audio responses
