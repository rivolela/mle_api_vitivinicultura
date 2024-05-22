from fastapi import FastAPI, HTTPException, Depends
from src.webscrapping.scrappingProducaoEmbrapa import scrappingProducaoPage
from src.webscrapping.scrappingProcessamentoEmbrapa import scrappingProcessamentoPage,validate_suboption_processamento
from src.webscrapping.scrappingComercializacaoEmbrapa import scrappingComercializacaoPage
from src.webscrapping.scrappingImportacaoEmbrapa import scrappingImportationsPage, validate_suboption_importations
from src.webscrapping.scrappingEmbrapaCommons import  validate_year
from src.webscrapping.scrappingExportacaoEmbrapa import scrappingExportacaoPage,validate_suboption_exportations

app = FastAPI()

list=[]


@app.get("/")
async def hello_api():
    return 'API Vitivinicultura Embrapa'


@app.get("/products/{year}")
async def get_products(year: str = Depends(validate_year)):
    try:
        list = scrappingProducaoPage(year)
        return {'products':list}
    except HTTPException as e:
        return e


@app.get("/processings/{year}/{suboption}")
async def get_pprocessings(year: str = Depends(validate_year),suboption: str = Depends(validate_suboption_processamento)):
    try:
        list = scrappingProcessamentoPage(year,suboption)
        return {'processings':list}
    except HTTPException as e:
       # Handle specific HTTPException with status code 404
        if e.status_code == 404:
            return {"error": "Data not found for the given year and suboption"}
        # For other HTTPExceptions, return the error detail
        return {"error": e.detail}
  

@app.get("/trades/{year}")
async def get_trades(year: str = Depends(validate_year)):
    try:
        list = scrappingComercializacaoPage(year)
        return {'products':list}
    except HTTPException as e:
        return e
    

@app.get("/importations/{year}/{suboption}")
async def get_importations(year: str = Depends(validate_year),suboption: str = Depends(validate_suboption_importations)):
    try:
        list = scrappingImportationsPage(year,suboption)
        return {'importations':list}
    except HTTPException as e:
       # Handle specific HTTPException with status code 404
        if e.status_code == 404:
            return {"error": "Data not found for the given year and suboption"}
        # For other HTTPExceptions, return the error detail
        return {"error": e.detail}
    

@app.get("/exportations/{year}/{suboption}")
async def get_exportations(year: str = Depends(validate_year),suboption: str = Depends(validate_suboption_exportations)):
    try:
        list = scrappingExportacaoPage(year,suboption)
        return {'exportations':list}
    except HTTPException as e:
       # Handle specific HTTPException with status code 404
        if e.status_code == 404:
            return {"error": "Data not found for the given year and suboption"}
        # For other HTTPExceptions, return the error detail
        return {"error": e.detail}