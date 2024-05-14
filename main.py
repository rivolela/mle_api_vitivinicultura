from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
import httpx
from typing import Optional
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoEmbrapa
from src.webscrapping.scrappingProducaoEmbrapa import validate_year_product
from config import Config, TestConfig
import os

app = FastAPI()

produtos=[]



@app.get("/")
async def hello_api():
    return 'API Vitivinicultura Embrapa'


@app.get("/products/{year_product}")
async def get_list_products(year_product: str = Depends(validate_year_product)):
    try:
        produtos = scrappingProducaoEmbrapa(year_product)
        print(produtos)
        return {'produtos':produtos}
    except HTTPException as e:
        return e
