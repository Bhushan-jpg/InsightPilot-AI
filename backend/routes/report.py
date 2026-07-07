from fastapi import APIRouter
from fastapi.responses import FileResponse

from services.report_generator import generate_pdf

import base64

router = APIRouter()

REPORT_DATA = None


@router.post("/report")
async def create_report(data: dict):

    global REPORT_DATA

    REPORT_DATA = data

    # -------------------------
    # Save Chart Image
    # -------------------------

    chart = data.get("chart_image")

    if chart:

        if "," in chart:

            chart = chart.split(",")[1]

        with open("chart.png", "wb") as f:

            f.write(base64.b64decode(chart))

    # -------------------------
    # Generate PDF
    # -------------------------

    generate_pdf(REPORT_DATA)

    return {

        "message": "Report Created"

    }


@router.get("/download-report")
async def download_report():

    return FileResponse(

        "InsightPilot_Report.pdf",

        media_type="application/pdf",

        filename="InsightPilot_Report.pdf"

    )