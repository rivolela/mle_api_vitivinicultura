
import os
from typing import Optional

from fastapi import HTTPException
from config import Config, TestConfig
from src.webscrapping.fetchWebPage import fetch_page
from src.webscrapping.parseHTMLContent import parse_html



def scrappingExportacaoPage(year,suboption):
    url = get_url(year,suboption)
    html_content = fetch_page(url)
    if html_content:
        soup = parse_html(html_content)
        rows = extract_table_data(soup) 
        processed_data = process_rows(rows,year)
        return processed_data
    else:
        raise HTTPException(status_code=404, detail="Data not found")
    

def extract_table_data(html_content):
    tableData = html_content.find('table', {'class': 'tb_base tb_dados'})  
    if tableData:
        tr_elements = tableData.find_all('tr')

        # Extract values from each <tr> element
        rows = []
        for tr in tr_elements:
            td_elements = tr.find_all('td')
            values = [td.get_text(strip=True) for td in td_elements]
            if values and all(values):  # Ensure values is not None and does not contain any empty strings
                rows.append(values)
        return rows
    else:
        print("Failed to extract_item_tableData.")
 

def process_rows(rows,year):
    processed_data = []
    for row in rows:
        country, value1, value2 = row
        data_dict = {
            "country": country,
            "quantity (Kg)": value1,
            "value (US$)": value2,
            "year": year
        }
        processed_data.append(data_dict)
    return processed_data


def get_url(year_product,suboption):
    if os.environ.get('ENVIRONMENT') == 'production':
        url = Config.BASE_URL_EXPORTACAO + "&ano=" + year_product + "&subopcao=" + suboption
    else:
        url = TestConfig.BASE_URL_EXPORTACAO   
    return url


def validate_suboption_exportations(suboption: Optional[str] = None):
    # Define the set of valid suboptions
    VALID_SUBOPTIONS = {
        'subopt_01': 'Vinhos de mesa',
        'subopt_02': 'Espumantes',
        'subopt_03': 'Uvas frescas',
        'subopt_04': 'Suco de uva',
    }
   
    if suboption is None or suboption.strip() == "" or suboption not in VALID_SUBOPTIONS:
        raise HTTPException(
            status_code=400, 
            detail={
                "error": {
                    "status_code": 400,
                    "detail": "Invalid suboption. Valid options are: " + ', '.join([f"'{key}': '{value}'" for key, value in VALID_SUBOPTIONS.items()])
                }
            }
        )
    return suboption
