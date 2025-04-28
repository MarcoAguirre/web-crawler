from bs4 import BeautifulSoup
from app.parser import EntryParser
from app.models import NewsItem

def test_news_parser_success():
    html_content = """
    <tr class='athing'>
        <td class='title'>
            <span class='rank'>1.</span>
        </td>
        <td class='titleline'>
            <a>Test Title</a>
        </td>
    </tr>
    <tr>
        <td class='subtext'>
            <span class='score'>100 points</span>
            <a>50 comments</a>
        </td>
    </tr>
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    parser = EntryParser(limit=1, parsed_html=soup)
    news_item = parser.parse_news()

    assert len(news_item) > 0
    assert isinstance(news_item[0], NewsItem)
    assert news_item[0].number == 1
    assert news_item[0].title.replace('\n', '') == 'Test Title'
    assert news_item[0].points == 100
    assert news_item[0].number_of_comments == 50
