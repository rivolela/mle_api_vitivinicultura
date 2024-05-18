
import os

from fastapi import HTTPException
from config import Config, TestConfig
from src.webscrapping.scrappingEmbrapaCommons import get_qtdade_value, get_year_item
from src.webscrapping.fetchWebPage import fetch_page
from src.webscrapping.parseHTMLContent import parse_html
from src.webscrapping.scrappingProducaoEmbrapa import extract_item_tableData
import re


def scrappingProcessamentoEmbrapa(year,suboption):
    url = get_url(year,suboption)
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        processamentos = extract_item_tableData(soup) 
        return processamentos
    else:
        raise HTTPException(status_code=404, detail="Data not found")


def extract_item_tableData(soup):
    tableData = soup.find('table', {'class': 'tb_base tb_dados'})   
    ano = get_year_item(soup)

    # Initialize an empty list to store the extracted text
    extracted_text = []

    if tableData:
        for child in tableData.find_all('td'):  

            value = child.text.strip() 

            if get_qtdade_value(value) is not None:
                dict["quantidade"] = value
                extracted_text.append(dict) 
            elif get_qtdade_legend(child):
                qtdade_legend = extract_legend_text(value,soup)
                dict["quantidade"] = qtdade_legend
                extracted_text.append(dict)
            else:
                dict = {}
                dict["cultivar"] = value
                dict["ano"] = ano

                # Find the <td> element with class "tb_item"
                class_name = child.get('class')

                if class_name:
                    # Remove the 'tb_' prefix 
                    class_name = class_name[0].replace('tb_', '')
                    # set type as subitem or item
                    dict["type"] = class_name
                    # is type==item add it as an attrubute subitem
                    if class_name == 'item':                   
                        nameItem = value
                    else:
                        dict["item"] = nameItem

        return extracted_text
    else:
        print("Failed to extract_item_tableData.")


def get_url(year_product,suboption):
    if os.environ.get('ENVIRONMENT') == 'production':
        url = Config.BASE_URL_PROCESSAMENTO + "&ano=" + year_product + "&suboption=" + suboption
    else:
        url = TestConfig.BASE_URL_PROCESSAMENTO   
    return url


# funtion to extract text from legend in case of quantity == '*', (1) or (2)
# r'\*|\(1\)|\(2\)' is the regular expression pattern:
# \* matches the literal * character.
# \(1\) matches the literal (1) string.
# \(2\) matches the literal (2) string.

def get_qtdade_legend(s):
    return bool(re.search(r'\*|\(1\)|\(2\)', s.text))



def extract_legend_text(parameter,soup):
    div_element = soup.find('div', class_='tb_font')

    if not div_element:
        return []
    
    texts = []
    for child in div_element.children:
        if child.name == 'br':
            continue
        if isinstance(child, str):
            texts.append(child.strip())
        else:
            texts.append(child.get_text().strip())


    lookup_dict = {
        '1': '(1)',
        '2': '(2)',
        '*': '*'
    }

    prefix = lookup_dict.get(parameter, '')
    if not prefix:
        return None

    for item in texts:
        item = item.strip()
        if item.startswith(prefix):
            return item
        
    return None

    # Example usage:
    # print(extract_text('1'))  # Output: (1) Tambem conhecida como Santiago e Zeperina.
    # print(extract_text('2'))  # Output: (2) Seibel 2, Dut Chess, Seyve Villard 5276.
    # print(extract_text('*'))  # Output: *: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]
