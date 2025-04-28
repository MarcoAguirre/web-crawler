from bs4 import BeautifulSoup
from models import NewsItem

class EntryParser:
    def __init__(self, limit: int, parsed_html: BeautifulSoup):
        self.limit = limit
        self.parsed_html = parsed_html

    def parse_news(self) -> list[NewsItem]:
        try:
            news = []
            table = self.parsed_html.select('.athing')[:self.limit]

            for row in table:
                number = row.select_one('.rank').get_text().strip('.')
                title = row.select_one('.titleline > a').get_text()
                subtext = row.find_next_sibling('tr').select_one('.subtext')
                points_element = subtext.select_one('.score') if subtext else None
                points = points_element.get_text().split()[0] if points_element else '0'
                comments = subtext.select('a')[-1].get_text().split()[0]

                if number and title:
                    news.append(NewsItem(
                        number=int(number),
                        title=title,
                        points=int(points) if points.isdigit() else 0,
                        number_of_comments=int(comments) if comments.isdigit() else 0,
                    ))

            return news
        except (AttributeError, ValueError) as e:
            raise ValueError(f"Error parsing entries: {e}")
