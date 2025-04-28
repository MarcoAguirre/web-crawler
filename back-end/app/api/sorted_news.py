from fastapi import APIRouter

from ..constants import Constants
from ..fetcher import PageFetcher
from ..parser import EntryParser
from ..sorter import Sorter

router = APIRouter()

@router.get("/")
async def index() -> dict:
    return {"web-crawler api version": "0.0"}

@router.get("/news/comments")
async def get_news_by_comments():
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    parser = EntryParser(Constants.NUMBER_OF_NEWS, page_content)
    parsed_news = parser.parse_news()

    sorter = Sorter(parsed_news)

    news_by_comments = sorter.sort_by_comments()

    return news_by_comments

@router.get("/news/points")
async def get_news_by_points():
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    parser = EntryParser(Constants.NUMBER_OF_NEWS, page_content)
    parsed_news = parser.parse_news()

    sorter = Sorter(parsed_news)

    news_by_points = sorter.sort_by_points()

    return news_by_points