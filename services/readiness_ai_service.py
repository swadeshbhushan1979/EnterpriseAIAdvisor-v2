from services.llm_service import generate_json

SYSTEM_PROMPT = """
You are an Enterprise AI Transformation Consultant.

Analyze the organization's AI readiness based on the supplied inputs.

Return ONLY valid JSON in the following format:

{
    "overall_score": 85,
    "overall_level": "Advanced",
    "strengths": [
        "...",
        "...",
        "..."
    ],
    "gaps": [
        "...",
        "...",
        "..."
    ],
    "recommendations": [
        "...",
        "...",
        "..."
    ]
}

Do not return markdown.
"""


def generate_assessment(data):

    return generate_json(
        SYSTEM_PROMPT,
        data,
        max_tokens=800
    )