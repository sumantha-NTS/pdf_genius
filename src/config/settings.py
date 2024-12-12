from dotenv import load_env
import os

load_env()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME","gpt-4o-mini")