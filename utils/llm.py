from openai import OpenAI


def get_openai_client(api_key: str) -> OpenAI:
    """
    Create and return an OpenAI client using the provided API key.

    Args:
        api_key (str): The OpenAI API key.

    Returns:
        OpenAI: An instance of the OpenAI client.
    """
    return OpenAI(api_key=api_key)


def get_chat_response(client: OpenAI, model: str, messages: list) -> str:
    """
    Get a chat response from the OpenAI client.

    Args:
        client (OpenAI): The OpenAI client instance.
        model (str): The model to use for generating the response.
        messages (list): A list of messages to send to the model.

    Returns:
        str: The response from the model.
    """

    return client.chat.completions.create(model=model, messages=messages, stream=True)
