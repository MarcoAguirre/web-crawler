import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.sorted_news import router as sorted_news_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sorted_news_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8080, reload=True)