from constants import Constants
from fetcher import PageFetcher

def run():
    # Fetch the page
    fetcher = PageFetcher(Constants.NEWS_PAGE_URL)
    page_content = fetcher.fetch()

    print(page_content)

if __name__ == "__main__":
    run()