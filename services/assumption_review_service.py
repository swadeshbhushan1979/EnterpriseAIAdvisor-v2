from services.llm_service import generate_json
from prompts.assumption_prompt import SYSTEM_PROMPT


def review_assumptions(data):

    return generate_json(
        SYSTEM_PROMPT,
        data,
        max_tokens=500
    )


# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import json

# from prompts.assumption_review_prompt import SYSTEM_PROMPT

# load_dotenv(override=True)

# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# def review_assumptions(data):

#     response = client.responses.create(

#         model="gpt-4.1-mini",

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

#     #return response.output_text
#     text = response.output_text.strip()

#     print("=" * 80)
#     print("ASSUMPTION REVIEW RESPONSE")
#     print(text)
#     print("=" * 80)

#     if not text:
#         raise Exception("OpenAI returned an empty response.")

#     if text.startswith("```json"):
#         text = text.replace("```json", "").replace("```", "").strip()

#     return json.loads(text)