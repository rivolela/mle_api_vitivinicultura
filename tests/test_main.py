import pytest
from httpx import AsyncClient
from main import app
from fastapi import HTTPException

from webscrapping.scrappingEmbrapaCommons import validate_year


@pytest.mark.asyncio
async def test_get_products_without_year():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products")
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}


@pytest.mark.asyncio
async def test_get_products_with_year():
    async with AsyncClient(app=app,base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products/2023")

        assert response.status_code == 200

        # Parse the JSON data
        data = response.json()

        # Extract the list of products
        produtos = data.get('products')
        
        # Assertions
        assert isinstance(produtos, list)  # Check if produtos is a list
        assert len(produtos) > 0  # Check if produtos array is not empty

        # Check the attributes of the first object in the list
        first_product = produtos[0]
        assert first_product['product'] == 'VINHO DE MESA'  # Check if item of the first element is 'VINHO DE MESA'
        assert first_product['quantidade'] == '169.762.429'  # Check if quantidade of the first element is '169.762.429'
        assert first_product['ano'] == '2023'  # Check if yeear of the first element is 2023
        assert first_product['type'] == 'item'  # Check if product type is item or subitem
        assert produtos[1]['quantidade'] == '139.320.884'  # Check if subitem quantity is '169.762.429'
        assert produtos[1]['ano'] == '2023'  # Check if subitem year is 2023
        assert produtos[1]['type'] == 'subitem'  # Check if type is subitem
        assert produtos[1]['item'] == 'VINHO DE MESA'  # Check if item of subitem is 'VINHO DE MESA'


@pytest.mark.asyncio
async def test_get_processing_with_year():
    async with AsyncClient(app=app,base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/processings/2022/subopt_01")

        assert response.status_code == 200

        # Parse the JSON data
        data = response.json()

        # Extract the list of products
        processings = data.get('processings')  
        
        # Assertions
        assert isinstance(processings, list)  # Check if produtos is a list
        assert len(processings) > 0  # Check if produtos array is not empty

        # Check the attributes of the first object in the list
        assert processings[0]['cultivar'] == 'TINTAS'  
        assert processings[0]['quantidade'] == '*: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]'
        assert processings[0]['ano'] == '2022'  
        assert processings[0]['type'] == 'item' 
        assert processings[1]['cultivar'] == 'Bacarina' 
        assert processings[1]['quantidade'] == '*: Os dados disponibilizados pelo SISDEVIN no ano de 2022 estão agregados [Uvas viníferas: 99.738.086; Uvas americanas ou híbridas: 565.243.922]'
        assert processings[1]['ano'] == '2022' 
        assert processings[1]['type'] == 'subitem' 
        assert processings[1]['item'] == 'TINTAS' 




def test_validate_year_product():
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

