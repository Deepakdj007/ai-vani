import os
from dotenv import load_dotenv

load_dotenv()

LIVEKIT_URL = os.environ["LIVEKIT_URL"]
LIVEKIT_API_KEY = os.environ["LIVEKIT_API_KEY"]
LIVEKIT_API_SECRET = os.environ["LIVEKIT_API_SECRET"]
SARVAM_API_KEY = os.environ["SARVAM_API_KEY"]

DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en-IN")
BUSINESS_NAME = os.getenv("BUSINESS_NAME", "My Booking Agent")
