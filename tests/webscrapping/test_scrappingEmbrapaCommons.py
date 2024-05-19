from src.webscrapping.parseHTMLContent import parse_html
from webscrapping.scrappingEmbrapaCommons import get_year_item


def test_extract_year_from_html():
    
    # Test case with a valid HTML content
    # Given HTML content
    html_content = '''
    <div class="content_center"> 
        <p class="text_center"> Produção de vinhos, sucos e derivados  [2023] </p>
    </div>
    '''
    soup = parse_html(html_content)
    assert get_year_item(soup) == '2023'

    # Test case with a missing tag
    html_content = '<p>Some other content</p>'
    soup = parse_html(html_content)
    assert get_year_item(soup) is None

    # Test case with missing year inside the tag
    html_content = '<p class="text_center"> Produção de vinhos, sucos e derivados  </p>'
    soup = parse_html(html_content)
    assert get_year_item(soup) is None
