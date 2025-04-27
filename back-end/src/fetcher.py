import requests

class PageFetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.content
        else:
            raise Exception(f'Failed with status code: {response.status_code}')