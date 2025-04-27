from constants import Constants
from fetcher import PageFetcher
from parser import EntryParser

def run():
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    parser = EntryParser(Constants.NUMBER_OF_NEWS, page_content)
    parsed_page = parser.parse_news()

    print(parsed_page)

if __name__ == "__main__":
    run()
