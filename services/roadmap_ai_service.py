from services.llm_service import generate_json
from prompts.roadmap_prompt import SYSTEM_PROMPT


def generate_roadmap(data):

    return generate_json(
        SYSTEM_PROMPT,
        data,
        max_tokens=700
    )

# import json
# import os

# from dotenv import load_dotenv
# from openai import OpenAI

# from prompts.roadmap_prompt import SYSTEM_PROMPT

# load_dotenv(override=True)

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def generate_roadmap(data):

#     response = client.responses.create(

#         model="gpt-4.1-mini",

#         max_output_tokens=700,

#         input=[
#             {
#                 "role":"system",
#                 "content":SYSTEM_PROMPT
#             },
#             {
#                 "role":"user",
#                 "content":str(data)
#             }
#         ]

#     )

#     text = response.output_text.strip()

#     if text.startswith("```json"):
#         text = text.replace("```json", "").replace("```", "").strip()

#     print(text)

#     if not text:
#         raise Exception("OpenAI returned an empty response.")

#     return json.loads(text)