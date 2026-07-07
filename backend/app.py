from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.users import router as user_router
from routes.upload import router as upload_router
from routes.chat import router as chat_router
from routes.report import router as report_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:3001"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user_router)

app.include_router(upload_router)

app.include_router(chat_router)

app.include_router(report_router)



@app.get("/")
def home():

    return {
        "message": "AI Business Intelligence Backend Running"
    }