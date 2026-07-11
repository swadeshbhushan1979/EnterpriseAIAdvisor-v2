from services.llm_service import generate_json
from prompts.opportunity_prompt import SYSTEM_PROMPT


def generate_opportunities(data):

    return generate_json(
        SYSTEM_PROMPT,
        data,
        max_tokens=900
    )


# import json
# from openai import OpenAI
# from dotenv import load_dotenv
# import os

# from prompts.opportunity_prompt import SYSTEM_PROMPT

# load_dotenv(override=True)

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# def generate_opportunities(data):

#     response = client.responses.create(

#         model="gpt-4.1-mini",

#         max_output_tokens=500,

#         input=[

#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },

#             {
#                 "role": "user",
#                 "content": str(data)
#             }

#         ]

#     )

#     text = response.output_text.strip()

#     if text.startswith("```json"):
#         text = text.replace("```json", "").replace("```", "").strip()

#     return json.loads(text)