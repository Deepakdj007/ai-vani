from vani.config import BUSINESS_NAME

GREETING = f"Hello! Welcome to {BUSINESS_NAME}. How can I help you today?"

def echo_response(transcript: str) -> str:
    return f"You said: {transcript}"
