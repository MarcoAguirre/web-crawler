from fastapi.testclient import TestClient
from app.api.sorted_news import router

from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_news_by_comments_route(mocker):
    mock_fetcher = mocker.patch("app.api.sorted_news.PageFetcher.fetch")
    mock_parser = mocker.patch("app.api.sorted_news.EntryParser.parse_news")
    mock_sorter = mocker.patch("app.api.sorted_news.Sorter.sort_by_comments")

    mock_fetcher.return_value = "<html>Mocked Content</html>"
    mock_parser.return_value = []
    mock_sorter.return_value = []

    response = client.get("/news/comments")
    assert response.status_code == 200
    assert response.json() == []

def test_news_by_points_route(mocker):
    mock_fetcher = mocker.patch("app.api.sorted_news.PageFetcher.fetch")
    mock_parser = mocker.patch("app.api.sorted_news.EntryParser.parse_news")
    mock_sorter = mocker.patch("app.api.sorted_news.Sorter.sort_by_points")

    mock_fetcher.return_value = "<html>Mocked Content</html>"
    mock_parser.return_value = []
    mock_sorter.return_value = []

    response = client.get("/news/points")
    assert response.status_code == 200
    assert response.json() == []
