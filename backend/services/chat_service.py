import os
import json

from dotenv import load_dotenv
from google import genai
from services.smart_query import smart_query

load_dotenv()


client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)




def ask_ai(
    question,
    df,
    analysis,
    preview,
    summary,
    story,
    kpis,
    findings,
    recommendations,
    charts,
    history=None
):

    question_lower = question.lower().strip()

    # =====================================================
    # Smart Query Engine (Pandas)
    # =====================================================

    smart_answer = smart_query(question, df)

    if smart_answer is not None:
        return smart_answer

    # =====================================================
    # Safe Values
    # =====================================================

    rows = analysis.get("rows", 0)
    columns = analysis.get("columns", 0)
    duplicates = analysis.get("duplicates", 0)
    null_values = analysis.get("null_values", 0)
    column_names = analysis.get("column_names", [])

    if history is None:
        history = []

    # =====================================================
    # Greetings
    # =====================================================

    if question_lower in ["hi", "hello", "hey", "hii"]:

        return (
            "👋 Hello! I am InsightPilot AI.\n\n"
            "I can help you understand your uploaded dataset.\n"
            "Ask me about rows, columns, KPIs, charts, findings, recommendations or business insights."
        )

    # =====================================================
    # Instant Dataset Answers
    # =====================================================

    if "column name" in question_lower:

        return (
            "The dataset contains these columns:\n\n"
            + ", ".join(column_names)
        )

    if "summary" in question_lower:
        return summary

    if "business story" in question_lower or question_lower == "story":
        return story

    if "finding" in question_lower:

        if findings:
            return "\n".join([f"• {item}" for item in findings])

        return "No findings are available."

    if "recommendation" in question_lower:

        if recommendations:
            return "\n".join([f"• {item}" for item in recommendations])

        return "No recommendations are available."

    if "kpi" in question_lower:

        if not kpis:
            return "No KPI information available."

        text = "Here are the KPI cards:\n\n"

        for kpi in kpis:

            text += (
                f"• {kpi.get('title','')} : "
                f"{kpi.get('value','')} "
                f"- {kpi.get('description','')}\n"
            )

        return text

    if "chart" in question_lower or "visual" in question_lower:

        if not charts:
            return "No charts are available."

        text = "The dashboard contains these charts:\n\n"

        for chart in charts:
            text += f"• {chart.get('title','')}\n"

        return text

    # =====================================================
    # Previous Chat
    # =====================================================

    history_text = ""

    for chat in history:

        history_text += (
            f"User: {chat.get('user','')}\n"
            f"Assistant: {chat.get('assistant','')}\n\n"
        )

    # =====================================================
    # Gemini Prompt
    # =====================================================

    prompt = f"""
You are InsightPilot AI.

You are a professional business data analyst.

Rules:

- Use simple English.
- Keep answers short.
- Never make up information.
- Use only the uploaded dataset.
- Explain why the answer matters for business.
- Maximum 150 words.

==================================================

PREVIOUS CHAT

{history_text}

==================================================

DATASET INFORMATION

{json.dumps(analysis, indent=2)}

==================================================

AI SUMMARY

{summary}

==================================================

BUSINESS STORY

{story}

==================================================

KPI CARDS

{json.dumps(kpis, indent=2)}

==================================================

KEY FINDINGS

{json.dumps(findings, indent=2)}

==================================================

RECOMMENDATIONS

{json.dumps(recommendations, indent=2)}

==================================================

CHARTS

{json.dumps(charts, indent=2)}

==================================================

DATA PREVIEW

{json.dumps(preview, indent=2)}

==================================================

USER QUESTION

{question}

Return only the answer.
"""

    # =====================================================
    # Gemini Call
    # =====================================================

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()

    except Exception as e:

        error = str(e)

        if "429" in error or "RESOURCE_EXHAUSTED" in error:

            return (
                "⚠️ AI limit reached temporarily.\n\n"
                "You can still use the dashboard, KPIs, charts and recommendations.\n"
                "Please try again later."
            )

        return "Sorry, I couldn't generate an answer right now."