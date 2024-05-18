from bs4 import BeautifulSoup
from src.webscrapping.scrappingProcessamentoEmbrapa import scrappingProcessamentoEmbrapa
from src.webscrapping.scrappingProcessamentoEmbrapa import extract_legend_text
from src.webscrapping.fetchWebPage import trata_html
from src.webscrapping.parseHTMLContent import parse_html

def test_scrappingProcessamentoEmbrapa():

    # Call the function to be tested
    processamentos = scrappingProcessamentoEmbrapa("2022","suboption_01")

    # Assertions
    assert processamentos is not None  # Check if produtos is not None
    assert isinstance(processamentos, list)  # Check if produtos is a list

    # Assertions
    assert len(processamentos) > 0  
    assert processamentos[0]['cultivar'] == 'TINTAS'  
    assert processamentos[1]['quantidade'] == '*: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]'
    assert processamentos[0]['ano'] == '2022'  
    assert processamentos[0]['type'] == 'item' 
    assert processamentos[1]['cultivar'] == 'Bacarina' 
    assert processamentos[1]['quantidade'] == '*: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]'
    assert processamentos[1]['ano'] == '2022' 
    assert processamentos[1]['type'] == 'subitem' 
    assert processamentos[1]['item'] == 'TINTAS' 


 # The test cases to extract text from legen


def test_extract_text_1():
    html_content = """
    <div class="tb_font">
          Fonte: Secretaria da Agricultura, Pecuária e Desenvolvimento Rural <br> Elaboração: EMBRAPA/CNPUV <br> (1) Tambem conhecida como Santiago e Zeperina. <br> (2) Seibel 2, Dut Chess, Seyve Villard 5276. <br> *: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922] <br>  
    </div>"""
    soup = parse_html(html_content)
    result = extract_legend_text('1',soup)
    assert result == '(1) Tambem conhecida como Santiago e Zeperina.'


def test_extract_text_2():
    html_content = """
    <div class="tb_font">
          Fonte: Secretaria da Agricultura, Pecuária e Desenvolvimento Rural <br> Elaboração: EMBRAPA/CNPUV <br> (1) Tambem conhecida como Santiago e Zeperina. <br> (2) Seibel 2, Dut Chess, Seyve Villard 5276. <br> *: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922] <br>  
    </div>"""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = extract_legend_text('2',soup)
    assert result == '(2) Seibel 2, Dut Chess, Seyve Villard 5276.'


def test_extract_text_star():
    html_content = """
    <div class="tb_font">
          Fonte: Secretaria da Agricultura, Pecuária e Desenvolvimento Rural <br> Elaboração: EMBRAPA/CNPUV <br> (1) Tambem conhecida como Santiago e Zeperina. <br> (2) Seibel 2, Dut Chess, Seyve Villard 5276. <br> *: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922] <br>  
    </div>"""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = extract_legend_text('*',soup)
    assert result == '*: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]'


def test_extract_text_invalid():
    html_content = """
    <div class="tb_font">
          Fonte: Secretaria da Agricultura, Pecuária e Desenvolvimento Rural <br> Elaboração: EMBRAPA/CNPUV <br> (1) Tambem conhecida como Santiago e Zeperina. <br> (2) Seibel 2, Dut Chess, Seyve Villard 5276. <br> *: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922] <br>  
    </div>"""
    soup = BeautifulSoup(html_content, 'html.parser')
    result = extract_legend_text('invalid',soup)
    assert result is None

# if __name__ == '__main__':
#     pytest.main()