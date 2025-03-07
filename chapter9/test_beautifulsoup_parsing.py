from bs4 import BeautifulSoup

# BeautifulSoup 테스트
from beautifulsoup_parsing import (
    parse_html, extract_title_and_headings, find_all_links,
    extract_table_data, scrape_news_articles
)

def test_beautifulsoup_parsing():
    # HTML 샘플
    html = """
    <html>
        <head><title>Test Page</title></head>
        <body>
            <h1>Main Heading</h1>
            <h2>Sub Heading</h2>
            <a href="https://example.com">Example Link</a>
            <a href="https://test.com">Test Link</a>
            <table id="data">
                <tr><th>Name</th><th>Age</th></tr>
                <tr><td>John</td><td>25</td></tr>
                <tr><td>Jane</td><td>24</td></tr>
            </table>
        </body>
    </html>
    """
    
    # parse_html 테스트
    soup = parse_html(html)
    assert soup.title.text == "Test Page"
    
    # extract_title_and_headings 테스트
    result = extract_title_and_headings(soup)
    assert result["title"] == "Test Page"
    assert "Main Heading" in result["headings"]
    assert "Sub Heading" in result["headings"]
    
    # find_all_links 테스트
    links = find_all_links(soup)
    assert len(links) == 2
    assert any(link["text"] == "Example Link" for link in links)
    assert any(link["url"] == "https://test.com" for link in links)
    
    # extract_table_data 테스트
    table_data = extract_table_data(soup, "data")
    assert len(table_data) == 2
    assert table_data[0]["Name"] == "John"
    assert table_data[1]["Age"] == "24"
    
    # 실제 뉴스 사이트 테스트는 건너뜀 (의존성 문제)