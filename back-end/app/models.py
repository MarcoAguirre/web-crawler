from pydantic import BaseModel

class NewsItem(BaseModel):
    title: str
    number: int
    points: int
    number_of_comments: int
