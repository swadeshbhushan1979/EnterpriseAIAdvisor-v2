from services.llm_service import generate_json
from prompts.roi_prompt import SYSTEM_PROMPT


def generate_business_case(data):

    return generate_json(
        SYSTEM_PROMPT,
        data,
        max_tokens=900
    )


# from openai import OpenAI
# from dotenv import load_dotenv
# import os
# import json

# from prompts.roi_prompt import SYSTEM_PROMPT

# load_dotenv(override=True)

# client = OpenAI(
#     api_key=os.getenv("OPENAI_API_KEY")
# )


# def generate_business_case(company):

#     response = client.responses.create(

#         model="gpt-4.1-mini",

#         input=[

#             {
#                 "role": "system",
#                 "content": SYSTEM_PROMPT
#             },

#             {
#                 "role": "user",
#                 "content": str(company)
#             }

#         ]

#     )

#     #return response.output_text
#     return json.loads(response.output_text)