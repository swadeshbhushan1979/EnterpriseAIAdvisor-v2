from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

print("First 15 chars:", api_key[:15])

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input="Reply with only SUCCESS"
    )

    print(response.output_text)

except Exception as e:
    print(e)