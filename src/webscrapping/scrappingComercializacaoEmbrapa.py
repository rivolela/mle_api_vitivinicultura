import os
from bs4 import BeautifulSoup
from config import Config, TestConfig
from src.webscrapping.fetchWebPage import fetch_page
from src.webscrapping.parseHTMLContent import parse_html
from src.webscrapping.scrappingEmbrapaCommons import get_qtdade_value, get_year_item, normalize_whitespace


def scrappingComercializacaoPage(year):
    url = get_url(year)
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        produtos = extract_item_tableData(soup) 
        return produtos
    else:
        print("Failed to fetch web page.")



def extract_item_tableData(soup):
    tableData = soup.find('table', {'class': 'tb_base tb_dados'})   
    ano = get_year_item(soup)

    # Initialize an empty list to store the extracted text
    extracted_text = []

    if tableData:
        for child in tableData.find_all('td'):          
            value = normalize_whitespace(child.text)
            if get_qtdade_value(value) is not None:
                dict["quantidade"] = value
                extracted_text.append(dict) 
            else:
                dict = {}
                dict["product"] = value
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


def get_url(year_product):
    if os.environ.get('ENVIRONMENT') == 'production':
        url = Config.BASE_URL_COMERCIALIZACAO + "&ano=" + year_product
    else:
        url = TestConfig.BASE_URL_COMERCIALIZACAO   
    return url


# if __name__ == "__main__":
#     scrappingProducaoEmbrapa(url)