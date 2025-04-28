from app.models import NewsItem
from app.utils import count_words
from app.constants import Constants

class Sorter:
    def __init__(self, data: list[NewsItem]):
        self.data = data

    def sort_by_comments(self) -> list[NewsItem]:
        filtered_news = [
            entry for entry in self.data
            if count_words(getattr(entry, 'title', "")) > Constants.LIMIT_FOR_WORDS_IN_TITLE
        ]
        return sorted(filtered_news, key=lambda x: x.number_of_comments, reverse=True)

    def sort_by_points(self) -> list[NewsItem]:
        filtered_news = [
            entry for entry in self.data
            if count_words(getattr(entry, 'title', "")) <= Constants.LIMIT_FOR_WORDS_IN_TITLE
        ]
        return sorted(filtered_news, key=lambda x: x.points, reverse=True)