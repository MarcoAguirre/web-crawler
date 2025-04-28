from app.models import NewsItem
from app.sorter import Sorter

mock_news_items = [
    NewsItem(number=1, title='Largest Test Title of all the titles', points=100, number_of_comments=50),
    NewsItem(number=2, title='Mid range of Test Titles', points=200, number_of_comments=20),
    NewsItem(number=3, title='Shortest Test Title', points=150, number_of_comments=30),
]
def test_sort_by_points():
    sorter = Sorter(mock_news_items)
    sorted_items = sorter.sort_by_points()

    assert len(sorted_items) > 0
    assert sorted_items[0].points == 200
    assert sorted_items[1].points == 150

def test_sort_by_comments():
    sorter = Sorter(mock_news_items)
    sorted_items = sorter.sort_by_comments()

    assert len(sorted_items) > 0
    assert sorted_items[0].number_of_comments == 50
