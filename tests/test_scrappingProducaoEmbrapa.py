from unittest.mock import MagicMock
import pytest
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoEmbrapa
from src.webscrapping.scrappingProducaoEmbrapa import get_year_item
from src.webscrapping.scrappingProducaoEmbrapa import parse_html
import os
from config import get_config
from bs4 import BeautifulSoup


def test_scrappingProducaoEmbrapa():

    # Call get_config function

    # Call the function to be tested
    produtos = scrappingProducaoEmbrapa("2023")

    # Assertions
    assert produtos is not None  # Check if produtos is not None
    assert isinstance(produtos, list)  # Check if produtos is a list

    # Assertions
    assert len(produtos) > 0  # Check if produtos array is not empty
    assert produtos[0]['item'] == 'VINHO DE MESA'  # Check if item of the first element is 'VINHO DE MESA'
    assert produtos[0]['quantidade'] == '169.762.429'  # Check if quantidade of the first element is '169.762.429'
    assert produtos[0]['ano'] == '2023'  # Check if item of the first element is 'VINHO DE MESA'



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

if __name__ == "__main__":
    pytest.main()



