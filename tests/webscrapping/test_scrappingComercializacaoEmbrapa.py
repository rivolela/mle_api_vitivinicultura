from bs4 import BeautifulSoup

from src.webscrapping.scrappingComercializacaoEmbrapa import scrappingComercializacaoPage



def test_scrappingComercializacaoPage():

    # Call the function to be tested
    comercializacao = scrappingComercializacaoPage("2023")

    # Assertions
    assert comercializacao is not None  # Check if comercializacao is not None
    assert isinstance(comercializacao, list)  # Check if comercializacao is a list

    # Assertions
    assert len(comercializacao) > 0  # Check if comercializacao array is not empty
    assert comercializacao[0]['product'] == 'VINHO DE MESA' 
    assert comercializacao[0]['quantidade'] == '187.016.848'  
    assert comercializacao[0]['ano'] == '2023'  
    assert comercializacao[0]['type'] == 'item'  
    assert comercializacao[1]['product'] == 'Tinto'  
    assert comercializacao[1]['quantidade'] == '165.097.539' 
    assert comercializacao[1]['ano'] == '2023' 
    assert comercializacao[1]['type'] == 'subitem'  
    assert comercializacao[1]['item'] == 'VINHO DE MESA'  