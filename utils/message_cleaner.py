def message_cleaner(messages: list) -> list:
    """
    Clean and format messages for the OpenAI API.

    Args:
        messages (list): A list of messages, each containing a 'role' and 'content'.

    Returns:
        list: A cleaned list of messages formatted for the OpenAI API.
    """
    return [{"role": msg["role"], "content": msg["content"]} for msg in messages]
