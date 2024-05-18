from typing import Optional
from fastapi import HTTPException


def normalize_whitespace(input):
    return " ".join(input.split())


def get_qtdade_value(item):
    value_without_periods = item.replace(".", "")
    value = value_without_periods.replace("-", "0")
    try:
        return float(value)
    except ValueError:
        return None  # Return None for non-float items


def is_string(value):
    # Check if the value is a strig and not a number (integer or float).
    if isinstance(value, (int, float)):
        return False
    elif isinstance(value, str) and value.strip().replace('.', '').isdigit():
        return False
    return True


def validate_year(year: Optional[str] = None):
    if year is None or year.strip() == "" or is_string(year):
        raise HTTPException(status_code=400, detail="Year product must be provided:YYYY")
    return year



def validate_suboption(suboption: Optional[str] = None):
    # Define the set of valid suboptions
    VALID_SUBOPTIONS = {
        'subopt_01': 'Viníferas',
        'subopt_02': 'Americanas e híbridas',
        'subopt_03': 'Uvas de mesa',
        'subopt_04': 'Sem classificação'
    }
    if suboption is None or suboption.strip() == "" or suboption not in VALID_SUBOPTIONS:
        raise HTTPException(status_code=400, detail="""Invalid suboption. Valid options are:'subopt_01': 'Viníferas','subopt_02': 'Americanas e híbridas','subopt_03': 'Uvas de mesa','subopt_04': 'Sem classificação'""")
    return suboption
 

def get_year_item(html_content):

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