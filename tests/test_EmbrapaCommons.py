
from fastapi import HTTPException
import pytest
from src.webscrapping.scrappingEmbrapaCommons import validate_year


def test_validate_year():
    # Test case: year_product is None
    with pytest.raises(HTTPException) as exc_info:
        validate_year(None)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"

    # Test case: year_product is an empty string
    with pytest.raises(HTTPException) as exc_info:
        validate_year("")
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"

    # Test case: year_product is a non-empty string
    year_product = "2023"
    result = validate_year(year_product)
    assert result == year_product

     # Test case: year_product is not a number
    with pytest.raises(HTTPException) as exc_info:
        validate_year("aaa")
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"

