import pytest
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoEmbrapa


def test_scrappingProducaoEmbrapa():

    # Call the function to be tested
    produtos = scrappingProducaoEmbrapa("2023")

    # Assertions
    assert produtos is not None  # Check if produtos is not None
    assert isinstance(produtos, list)  # Check if produtos is a list

    # Assertions
    assert len(produtos) > 0  # Check if produtos array is not empty
    assert produtos[0]['product'] == 'VINHO DE MESA'  # Check if item of the first element is 'VINHO DE MESA'
    assert produtos[0]['quantidade'] == '169.762.429'  # Check if quantidade of the first element is '169.762.429'
    assert produtos[0]['ano'] == '2023'  # Check if item year is 2023
    assert produtos[0]['type'] == 'item'  # Check if type is item
    assert produtos[1]['product'] == 'Tinto'  # Check if subitem is 'Tinto'
    assert produtos[1]['quantidade'] == '139.320.884'  # Check if subitem quantity is '169.762.429'
    assert produtos[1]['ano'] == '2023'  # Check if subitem year is 2023
    assert produtos[1]['type'] == 'subitem'  # Check if type is subitem
    assert produtos[1]['item'] == 'VINHO DE MESA'  # Check if item of subitem is 'VINHO DE MESA'


if __name__ == "__main__":
    pytest.main()



