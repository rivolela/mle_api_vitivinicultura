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
        return extracted_text
    else:
        print("Failed to extract_product_item.")


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