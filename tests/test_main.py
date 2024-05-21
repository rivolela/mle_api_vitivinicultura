import pytest
from httpx import AsyncClient
from main import app



@pytest.mark.asyncio
async def test_get_products_without_year():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/products")
        assert response.status_code == 404
        assert response.json() == {"detail": "Not Found"}

@pytest.mark.asyncio
async def test_get_url_imcomplete():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/prodts")
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


@pytest.mark.asyncio
async def test_get_comercializacao_with_year():
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
async def test_get_importation_with_year():
    async with AsyncClient(app=app,base_url="http://127.0.0.1:8000") as ac:
        response = await ac.get("/importations/2023/subopt_01")

        assert response.status_code == 200

        # Parse the JSON data
        data = response.json()

        # Extract the list of products
        importations = data.get('importations')  
        
        # Assertions
        assert isinstance(importations, list)  # Check if produtos is a list
        assert len(importations) > 0  # Check if produtos array is not empty

        # Check the attributes of the first object in the list
        assert len(importations) > 0  
        assert importations[0]['country'] == 'Africa do Sul' 
        assert importations[0]['quantity (Kg)'] == '522.733'
        assert importations[0]['value (US$)'] == '1.732.850'
        assert importations[0]['year'] == '2023'   
        assert importations[1]['country'] == 'Alemanha' 
        assert importations[1]['quantity (Kg)'] == '102.456'
        assert importations[1]['value (US$)'] == '557.947'
        assert importations[1]['year'] == '2023'     
        assert importations[2]['country'] == 'Argélia' 
        assert importations[2]['quantity (Kg)'] == '-'
        assert importations[2]['value (US$)'] == '-'
        assert importations[2]['year'] == '2023'       

        

@pytest.mark.asyncio
async def test_importations_suboption_null():
    async with AsyncClient(app=app,base_url="http://127.0.0.1:8000") as ac:

         # Simulate a request with suboption as None
        year = "2023"
        response = await ac.get(f"/importations/{year}/None")

        # Validate the response
        assert response.status_code == 400
        assert response.json() == {"detail":{"error":{"status_code":400,"detail":"Invalid suboption. Valid options are: \'subopt_01\': \'Vinhos de mesa\', \'subopt_02\': \'Espumantes\', \'subopt_03\': \'Uvas frescas\', \'subopt_04\': \'Uvas passas\', \'subopt_05\': \'Suco de uva\'"}}}