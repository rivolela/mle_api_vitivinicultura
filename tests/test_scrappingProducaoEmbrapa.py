from unittest.mock import MagicMock
import pytest
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoEmbrapa
import os
from config import get_config

# Test the function
def test_scrappingProducaoEmbrapa():

    # Call get_config function
    config = get_config()
    
    if os.environ.get('ENVIRONMENT') == 'production':
        url = config.URL_PRODUCTS + "2023"
    else:
        url = config.URL_PRODUCTS

    # Call the function to be tested
    produtos = scrappingProducaoEmbrapa(url)

    # Assertions
    assert produtos is not None  # Check if produtos is not None
    assert isinstance(produtos, list)  # Check if produtos is a list

    # Assertions
    assert len(produtos) > 0  # Check if produtos array is not empty
    assert produtos[0]['item'] == 'VINHO DE MESA'  # Check if item of the first element is 'VINHO DE MESA'
    assert produtos[0]['quantidade'] == '169.762.429'  # Check if quantidade of the first element is '169.762.429'
