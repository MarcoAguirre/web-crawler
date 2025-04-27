from constants import Constants
from fetcher import PageFetcher
from parser import EntryParser
from utils import count_words

def run() -> None:
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    parser = EntryParser(Constants.NUMBER_OF_NEWS, page_content)
    parsed_news = parser.parse_news()

    for entry in parsed_news:
        news_title = getattr(entry, 'title', "")
        word_count = count_words(news_title)
        print(f"Title: {news_title}, Word Count: {word_count}")

if __name__ == "__main__":
    run()
