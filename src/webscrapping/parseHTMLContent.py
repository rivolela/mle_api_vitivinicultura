from bs4 import BeautifulSoup

def parse_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract information using BeautifulSoup methods like find(), find_all(), etc.
    # Example: titles = soup.find_all('h2')
    return soup
