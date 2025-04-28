import pytest
from unittest.mock import patch, Mock
from app.fetcher import PageFetcher
from bs4 import BeautifulSoup

@patch('app.fetcher.requests.get')
def test_fetch_page_success(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.content = b'<html><body>Page successfully fetched</body></html>'
    mock_get.return_value = mock_response

    fetcher = PageFetcher('http://urlfortest.com')
    result = fetcher.fetch()

    assert isinstance(result, BeautifulSoup)
    assert 'Page successfully fetched' in result.text


@patch('app.fetcher.requests.get')
def test_fetch_page_failure(mock_get):
    mock_response = Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    fetcher = PageFetcher('http://urlfortest.com')
    with pytest.raises(Exception) as excinfo:
        fetcher.fetch()

    assert str(excinfo.value) == 'Failed with status code: 404'
