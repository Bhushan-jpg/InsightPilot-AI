from fastapi import APIRouter, UploadFile, File
import pandas as pd
import io

from services.analyzer import analyze_dataset
from services.chart_generator import generate_ai_charts
from services.insight_generator import generate_insights
from services.ai_summary import generate_ai_summary
from services.ai_story import generate_business_story
from services.kpi_generator import generate_kpis
from services.dataset_detector import detect_dataset_type
from services.schema_detector import detect_schema

from routes import chat

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...)):

    contents = await file.read()

    # ====================================================
    # Read CSV / Excel
    # ====================================================

    if file.filename.endswith(".csv"):
        df = pd.read_csv(io.BytesIO(contents))
    else:
        df = pd.read_excel(io.BytesIO(contents))

    # ====================================================
    # Dataset Analysis
    # ====================================================

    analysis = analyze_dataset(df)
    schema = detect_schema(df)
    chat.CURRENT_SCHEMA = schema

    # ====================================================
    # Dataset Type
    # ====================================================

    dataset_type = detect_dataset_type(df)

    # ====================================================
    # KPI Cards
    # ====================================================

    kpis = generate_kpis(df)

    # ====================================================
    # Smart Charts
    # ====================================================

    charts = generate_ai_charts(df)

    # ====================================================
    # Insights
    # ====================================================

    insights = generate_insights(df)

    # ====================================================
    # AI Summary
    # ====================================================

    ai_output = generate_ai_summary(analysis)

    # ====================================================
    # Business Story
    # ====================================================

    business_story = generate_business_story(analysis)

    # ====================================================
    # Store everything for AI Chat
    # ====================================================

    # Store DataFrame (Required for Smart Query Engine)
    chat.CURRENT_DF = df

    # Store Analysis
    chat.CURRENT_ANALYSIS = analysis
    chat.CURRENT_PREVIEW = analysis.get("preview", [])

    # Store AI Outputs
    chat.CURRENT_SUMMARY = ai_output.get("ai_summary", "")
    chat.CURRENT_STORY = business_story

    # Store Dashboard Components
    chat.CURRENT_KPIS = kpis
    chat.CURRENT_FINDINGS = ai_output.get("key_findings", [])
    chat.CURRENT_RECOMMENDATIONS = ai_output.get("recommendations", [])
    chat.CURRENT_CHARTS = charts

    # Reset chat history when a new dataset is uploaded
    chat.CHAT_HISTORY = []

    # ====================================================
    # Final Response
    # ====================================================

    return {

        "filename": file.filename,

        # Dataset Analysis
        **analysis,

        # Dataset Type
        "dataset_type": dataset_type,

        # KPI Cards
        "kpis": kpis,

        # Smart Charts
        "charts": charts,

        # Insights
        "insights": insights,

        # AI Summary
        "ai_summary": ai_output.get("ai_summary", ""),

        # Key Findings
        "key_findings": ai_output.get("key_findings", []),

        # Recommendations
        "recommendations": ai_output.get("recommendations", []),

        # Business Story
        "business_story": business_story

    }