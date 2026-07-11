import json
import os
import streamlit as st

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)


def get_client():

    api_key = st.session_state.get("OPENAI_API_KEY")

    # Fallback to .env for local development
    if not api_key:
        api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OpenAI API Key not found. Please enter it on the Home page."
        )

    return OpenAI(api_key=api_key)


def generate_json(system_prompt, user_data, max_tokens=800):

    client = get_client()

    response = client.responses.create(

        model="gpt-4.1-mini",

        max_output_tokens=max_tokens,

        input=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": str(user_data)
            }
        ]
    )

    text = response.output_text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    if not text:
        raise Exception("OpenAI returned an empty response.")

    try:
        return json.loads(text)

    except Exception as e:
        raise Exception(
            f"Invalid JSON returned by OpenAI:\n\n{text}"
        ) from e

        