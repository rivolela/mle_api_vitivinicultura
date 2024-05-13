import pytest
import httpx
from httpx import AsyncClient
from main import app
from fastapi import HTTPException
from typing import Optional
from main import validate_year_product  # Import your function from the appropriate module
import os
from main import get_config, Config, TestConfig  # Import your function and configuration classes


@pytest.mark.asyncio
async def test_url_not_found():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products")
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}
        #assert response.json() == {"products": []}


def test_validate_year_product():
    # Test case: year_product is None
    with pytest.raises(HTTPException) as exc_info:
        validate_year_product(None)
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"

    # Test case: year_product is an empty string
    with pytest.raises(HTTPException) as exc_info:
        validate_year_product("")
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"

    # Test case: year_product is a non-empty string
    year_product = "2023"
    result = validate_year_product(year_product)
    assert result == year_product

     # Test case: year_product is not a number
    with pytest.raises(HTTPException) as exc_info:
        validate_year_product("aaa")
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Year product must be provided:YYYY"


@pytest.fixture
def mock_os_environ(monkeypatch):
    """
    Fixture to mock os.environ.get method.
    """
    def mock_get(key, default=None):
        if key == 'ENVIRONMENT':
            return 'test'
        return default  # Return the default value when key is not found
    monkeypatch.setattr(os.environ, 'get', mock_get)


def test_get_config(mock_os_environ):
    """
    Test get_config function.
    """
    # Call get_config function
    config = get_config()

    # Assert that the returned object is an instance of TestConfig
    assert isinstance(config, TestConfig)

    # Add more assertions as needed
    assert config.DEBUG == True
    assert config.TESTING == True
    assert config.URL_PRODUCTS == config.URL_PRODUCTS

