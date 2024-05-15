from bs4 import BeautifulSoup
from src.webscrapping.fetchWebPage import fetch_page
from src.webscrapping.parseHTMLContent import parse_html
from fastapi import FastAPI, HTTPException, Depends
from typing import Optional
from config import Config, TestConfig
import os


def scrappingProducaoEmbrapa(year):
    url = get_url(year)
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        produtos = extract_product_item(soup) 
        return produtos
    else:
        print("Failed to fetch web page.")



def extract_product_item(soup):
    tableProducts = soup.find('table', {'class': 'tb_base tb_dados'}) 
    
    ano = get_year_item(soup)

    # Initialize an empty list to store the extracted text
    extracted_text = []

    if tableProducts:
        for child in tableProducts.find_all('td'):          
            value = trata_item(child)
            if check_item_float(value) is not None:
                product["quantidade"] = value
                extracted_text.append(product) 
            else:
                product = {}
                product["item"] = value
                product["ano"] = ano
        return extracted_text
    else:
        print("Failed to extract_product_item.")


def get_year_item(html_content):

    #soup = BeautifulSoup(html_content, 'html.parser')

    # Find the <div> element with class 'content_center'
    div_tag = html_content.find('div', class_='content_center')
                        
    # Extract the text content of the <p> tag inside the <div>
    if div_tag:
        p_tag = div_tag.find('p', class_='text_center') # type: ignore
        if p_tag:
            # Extract the year from the text
            text = p_tag.get_text()
            year = text.strip().split('[', 1)[1].split(']', 1)[0]
            return year
        else:
            print("No <p> tag with class 'text_center' found inside <div>")
            return None
    else:
        print("No <div> tag with class 'content_center' found")
        return None


def trata_item(input):
    value = input.text.replace("-", "0")
    return " ".join(value.split())


def check_item_float(item):
    value_without_periods = item.replace(".", "")
    try:
        return float(value_without_periods)
    except ValueError:
        return None  # Return None for non-float items


def is_string(value):
    # Check if the value is a strig and a not number (integer or float).
    if isinstance(value, (int, float)):
        return False
    elif isinstance(value, str) and value.strip().replace('.', '').isdigit():
        return False
    return True


def validate_year_product(year_product: Optional[str] = None):
    if year_product is None or year_product.strip() == "" or is_string(year_product):
        raise HTTPException(status_code=400, detail="Year product must be provided:YYYY")
    return year_product



def get_url(year_product):
    if os.environ.get('ENVIRONMENT') == 'production':
        url = Config.URL_PRODUCTS + year_product
    else:
        url = TestConfig.URL_PRODUCTS   
    return url


# if __name__ == "__main__":
#     scrappingProducaoEmbrapa(url)