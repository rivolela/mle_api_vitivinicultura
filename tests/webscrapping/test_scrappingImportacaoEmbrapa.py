from config import TestConfig
from webscrapping.fetchWebPage import fetch_page
from src.webscrapping.scrappingImportacaoEmbrapa import scrappingImportationsPage, extract_table_data, process_rows
from src.webscrapping.parseHTMLContent import parse_html


def test_scrappingImportacaoEmbrapa():

    # Call the function to be tested
    importations = scrappingImportationsPage("2023","suboption_01")

    # Assertions
    assert importations is not None  # Check if produtos is not None
    assert isinstance(importations, list)  # Check if produtos is a list

    # Assertions
    assert len(importations) > 0  
    assert importations[0]['country'] == 'Africa do Sul' 
    assert importations[0]['quantity (Kg)'] == '522.733'
    assert importations[0]['value (US$)'] == '1.732.850'
    assert importations[0]['year'] == '2023'    
    assert importations[1]['country'] == 'Alemanha' 
    assert importations[1]['quantity (Kg)'] == '102.456'
    assert importations[1]['value (US$)'] == '557.947'  
    assert importations[1]['year'] == '2023' 
    assert importations[2]['country'] == 'Argélia' 
    assert importations[2]['quantity (Kg)'] == '-'
    assert importations[2]['value (US$)'] == '-'
    assert importations[2]['year'] == '2023'   



def test_extract_table_data():
    url = TestConfig.BASE_URL_IMPORTACAO
    html_content = fetch_page(url)
    soup = parse_html(html_content)
    importations = extract_table_data(soup)

    # Test the extraction function
    # Assertions
    assert importations is not None  # Check if list is not None
    assert isinstance(importations, list)  # Check if importations is a list
    assert len(importations) > 0  
    assert importations[0] == ['Africa do Sul', '522.733', '1.732.850']
    assert importations[1] == ['Alemanha', '102.456', '557.947']


def test_process_rows():
    # Define the input data
    input_data = [
        ['Alemanha', '102.456', '557.947'],
        ['França', '200.123', '678.345']
    ]

    # Define the expected output
    expected_output = [
        {
            "country": 'Alemanha',
            "quantity (Kg)": '102.456',
            "value (US$)": '557.947',
            "year": '2023'
        },
        {
            "country": 'França',
            "quantity (Kg)": '200.123',
            "value (US$)": '678.345',
            "year": '2023'
            
        }
    ]

    # Call the function with the input data
    result = process_rows(input_data,year="2023")

    # Assert that the result matches the expected output
    assert result == expected_output
