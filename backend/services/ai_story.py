import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_business_story(analysis):

    prompt = f"""
You are InsightPilot AI.

You are a Senior Business Consultant.

Your task is to create a professional business story based ONLY on the uploaded dataset.

Dataset Information:

{analysis}

Instructions:

- Never invent people or characters.
- Never create fictional names.
- Never make up facts.
- Use only the provided dataset information.
- Write in simple English.
- Sound like a business consultant.
- Explain why the dataset exists.
- Explain how the organization can use it.
- Maximum 180 words.

Write in this style:

Business Story

Explain:

1. What this dataset represents.
2. What information it contains.
3. Why this information is valuable.
4. How management can use these insights.
5. End with one concluding sentence.

Do not use bullet points.

Return only the business story.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):

            return (
                "This dataset represents business records collected for operational "
                "analysis and decision making. It contains valuable information that "
                "helps organizations understand trends, compare performance and "
                "identify areas that require improvement. By analyzing this data, "
                "management can make better strategic decisions, improve efficiency "
                "and monitor overall business performance. The dashboard transforms "
                "raw data into meaningful insights that support planning and growth."
            )

        raise e