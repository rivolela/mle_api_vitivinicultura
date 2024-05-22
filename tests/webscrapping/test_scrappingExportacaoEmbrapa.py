from config import TestConfig
from webscrapping.fetchWebPage import fetch_page
from src.webscrapping.scrappingExportacaoEmbrapa import scrappingExportacaoPage, extract_table_data, process_rows
from src.webscrapping.parseHTMLContent import parse_html


def test_scrappingExportacaoEmbrapa():

    # Call the function to be tested
    exportations = scrappingExportacaoPage("2023","suboption_01")

    # Assertions
    assert exportations is not None  # Check if produtos is not None
    assert isinstance(exportations, list)  # Check if produtos is a list

    # Assertions
    assert len(exportations) > 0  
    assert exportations[0]['country'] == 'Afeganistão' 
    assert exportations[0]['quantity (Kg)'] == '-'
    assert exportations[0]['value (US$)'] == '-'
    assert exportations[0]['year'] == '2023'    
    assert exportations[1]['country'] == 'África do Sul' 
    assert exportations[1]['quantity (Kg)'] == '117'
    assert exportations[1]['value (US$)'] == '698'  
    assert exportations[1]['year'] == '2023' 
    assert exportations[2]['country'] == 'Alemanha, República Democrática' 
    assert exportations[2]['quantity (Kg)'] == '4.806'
    assert exportations[2]['value (US$)'] == '31.853'
    assert exportations[2]['year'] == '2023'   



def test_extract_table_data():
    url = TestConfig.BASE_URL_EXPORTACAO
    html_content = fetch_page(url)
    soup = parse_html(html_content)
    exportations = extract_table_data(soup)
  
    # Test the extraction function
    # Assertions
    assert exportations is not None  # Check if list is not None
    assert isinstance(exportations, list)  # Check if exportations is a list
    assert len(exportations) > 0  
    assert exportations[0] == ['Afeganistão', '-', '-']
    assert exportations[1] == ['África do Sul', '117', '698']


def test_process_rows():
    # Define the input data
    input_data = [
        ['Afeganistão', '-', '-'],
        ['África do Sul', '117', '698']
    ]

    # Define the expected output
    expected_output = [
        {
            "country": 'Afeganistão',
            "quantity (Kg)": '-',
            "value (US$)": '-',
            "year": '2023'
        },
        {
            "country": 'África do Sul',
            "quantity (Kg)": '117',
            "value (US$)": '698',
            "year": '2023'
            
        }
    ]

    # Call the function with the input data
    result = process_rows(input_data,year="2023")

    # Assert that the result matches the expected output
    assert result == expected_output
