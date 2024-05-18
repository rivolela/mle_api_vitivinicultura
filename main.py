from fastapi import FastAPI, HTTPException, Depends
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoEmbrapa
from src.webscrapping.scrappingProcessamentoEmbrapa import scrappingProcessamentoEmbrapa
from src.webscrapping.scrappingEmbrapaCommons import validate_year,validate_suboption


app = FastAPI()

list=[]


@app.get("/")
async def hello_api():
    return 'API Vitivinicultura Embrapa'


@app.get("/products/{year}")
async def get_products(year: str = Depends(validate_year)):
    try:
        list = scrappingProducaoEmbrapa(year)
        return {'products':list}
    except HTTPException as e:
        return e


@app.get("/processings/{year}/{suboption}")
async def get_processings(year: str = Depends(validate_year),suboption: str = Depends(validate_suboption)):
    try:
        list = scrappingProcessamentoEmbrapa(year,suboption)
        return {'processings':list}
    except HTTPException as e:
       # Handle specific HTTPException with status code 404
        if e.status_code == 404:
            return {"error": "Data not found for the given year and suboption"}
        # For other HTTPExceptions, return the error detail
        return {"error": e.detail}
  
