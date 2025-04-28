import uvicorn
from fastapi import FastAPI
from app.api.sorted_news import router as sorted_news_router

app = FastAPI()
app.include_router(sorted_news_router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="localhost", port=8080, reload=True)