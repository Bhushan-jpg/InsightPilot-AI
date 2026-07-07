import os
import json

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_ai_summary(analysis):

    prompt = f"""
You are InsightPilot AI.

You are a Senior Business Intelligence Analyst.

Your job is to explain datasets in a professional but very simple way.

Dataset Information:

{json.dumps(analysis, indent=2)}

Instructions:

- Use very simple English.
- Write like a business analyst, not like ChatGPT.
- Never invent information.
- Use only the provided dataset.
- Avoid technical words whenever possible.
- Do NOT mention JSON, dataframe, rows of code or Python.
- Keep the language suitable for managers and beginners.
- Maximum 180 words.

Return ONLY valid JSON in this format:

{{
    "ai_summary":
    "Executive summary here.",

    "key_findings":[
        "...",
        "...",
        "...",
        "...",
        "..."
    ],

    "recommendations":[
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}

Guidelines

AI Summary should include:

• Dataset overview
• Data quality
• Business importance
• Possible business use

Key Findings should be observations, NOT statistics.

Good examples:

- The dataset is complete and suitable for analysis.
- Patient records are well organized.
- Treatment costs vary across diseases.
- The dataset supports operational decision making.
- Multiple cities are represented.

Recommendations should be practical business actions.

Good examples:

- Monitor high-cost treatments regularly.
- Compare performance across cities.
- Focus on reducing expensive operations.
- Use historical trends for forecasting.
- Review unusual records periodically.

Return JSON only.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = (
                text.replace("```json", "")
                    .replace("```", "")
                    .strip()
            )

        return json.loads(text)

    except Exception as e:

        if "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e):

            return {

                "ai_summary":
                (
                    f"This dataset contains {analysis.get('rows',0):,} records "
                    f"across {analysis.get('columns',0)} fields. "
                    "The available information appears suitable for business analysis "
                    "and can help identify trends, compare performance and support "
                    "better decision-making."
                ),

                "key_findings":[
                    "Dataset analysis completed successfully.",
                    "The available data appears suitable for business reporting.",
                    "The dataset can be explored using charts and KPIs.",
                    "No AI-generated insights are available at the moment.",
                    "Dashboard metrics are still available."
                ],

                "recommendations":[
                    "Review KPI cards to identify important metrics.",
                    "Use charts to discover trends and patterns.",
                    "Compare different categories before making decisions.",
                    "Use the chatbot to explore the uploaded data.",
                    "Generate the report after reviewing the dashboard."
                ]

            }

        raise e