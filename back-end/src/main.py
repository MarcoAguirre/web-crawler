from constants import Constants
from fetcher import PageFetcher
from parser import EntryParser
from sorter import Sorter

def run() -> None:
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    parser = EntryParser(Constants.NUMBER_OF_NEWS, page_content)
    parsed_news = parser.parse_news()

    sorter = Sorter(parsed_news)

    news_by_comments = sorter.sort_by_comments()
    news_by_points = sorter.sort_by_points()

if __name__ == "__main__":
    run()
