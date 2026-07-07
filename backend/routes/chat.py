from fastapi import APIRouter
from pydantic import BaseModel

from services.chat_service import ask_ai

router = APIRouter()

# =====================================================
# Current Uploaded Dataset Context
# =====================================================

CURRENT_DF = None

CURRENT_ANALYSIS = None
CURRENT_PREVIEW = None

CURRENT_SUMMARY = None
CURRENT_STORY = None
CURRENT_KPIS = None
CURRENT_FINDINGS = None
CURRENT_RECOMMENDATIONS = None
CURRENT_CHARTS = None

CURRENT_SCHEMA = None

# =====================================================
# Chat Memory
# =====================================================

CHAT_HISTORY = []

# =====================================================
# Request Model
# =====================================================

class ChatRequest(BaseModel):
    question: str


# =====================================================
# Chat Endpoint
# =====================================================

@router.post("/chat")
async def chat(request: ChatRequest):

    if CURRENT_DF is None:

        return {
            "success": False,
            "answer": "Please upload a dataset first.",
            "confidence": 0,
            "source": "System"
        }

    answer = ask_ai(

        question=request.question,

        df=CURRENT_DF,

        analysis=CURRENT_ANALYSIS,

        preview=CURRENT_PREVIEW,

        summary=CURRENT_SUMMARY,

        story=CURRENT_STORY,

        kpis=CURRENT_KPIS,

        findings=CURRENT_FINDINGS,

        recommendations=CURRENT_RECOMMENDATIONS,

        charts=CURRENT_CHARTS,

        

        history=CHAT_HISTORY

    )

    # Save Chat History

    CHAT_HISTORY.append({

        "user": request.question,

        "assistant": answer

    })

    # Keep only last 10 conversations

    if len(CHAT_HISTORY) > 10:
        CHAT_HISTORY.pop(0)

    return {

        "success": True,

        "answer": answer,

        "confidence": 95,

        "source": "Uploaded Dataset"

    }