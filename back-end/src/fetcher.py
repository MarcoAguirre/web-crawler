import requests
from bs4 import BeautifulSoup

class PageFetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self) -> BeautifulSoup:
        response = requests.get(self.url)
        if response.status_code == 200:
            return BeautifulSoup(response.content, 'html.parser')
        else:
            raise Exception(f'Failed with status code: {response.status_code}')