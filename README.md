# API Vitivinicultura
API from Embrapa vitivinicultura website (v.2)

## Site Embrapa
- [Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

## Proposal
This API was developed for the first tech challenge in FIAP's Machine Learning Engineering Course 2024. The objective was to create a webscraping script for Embrapa's Vitivinicultura website and build an API to render this data for a Machine Learning model. All data are from Rio Grande do Sul, which represents 90% of Brazil's wine production, and were collected between 1970 to 2023.


## Deploy Diagram
```
+-------------------+                 +----------------------------+             +--------------------+
|                   |  HTTP/HTTPS     |                            | Internal    |                    |
| Client API        | <-------------> |  API Rest: Vitivinicultura | Network     |  Database (TBD)    |
| Requests          |                 |  Embrapa                   | <---------> |    (IasS: AWS)     |
|                   |                 |  (Web Server: Render)      |             |                    |
+-------------------+                 +----------------------------+             +--------------------+
                                             ^   |                                       |
                                             |   | Internal Network                      | Internal
                                 HTTP/HTTPS  |   |                                       | Network
                                             |   v                                       v
                                     +----------------------------+             +-------------------+
                                     |                            |             |                   |
                                     |   Web Scraping:            |             |      ML (TBD)     |
                                     |   Vitivinicultura Embrapa  |             |   (IasS:  AWS     |
                                     |   (Web Server: Render)     |             |                   |
                                     +----------------------------+             +-------------------+
                                             ^
                                             |
                                Internal Network
                                             |
                                             v
                                     +-------------------+
                                     |                   |
                                     |      Website      |
                                     | (Vitivinicultura  |
                                     |     Embrapa)      |
                                     +-------------------+
```

## Test

## Endpoints
- API documentation and endpoints: [API Documentation](https://mle-api-vitivinicultura.onrender.com/docs)
  - This API was delivered on a Free Web Service in the Render Platform. As it is free, the instance will spin down with inactivity, which can delay requests by 50 seconds or more.

- **Endpoints:**
  1. **Rio Grande do Sul's Wine Production, Juices, and Derivatives**
     - Endpoint: `/products/{year}`
  2. **Rio Grande do Sul's Wine Quantity of Grapes Processed**
     - Endpoint: `/processings/{year}/{suboption}`
     - Valid suboptions:
       ```python
       VALID_SUBOPTIONS = {
           'subopt_01': 'Viníferas',
           'subopt_02': 'Americanas e híbridas',
           'subopt_03': 'Uvas de mesa',
           'subopt_04': 'Sem classificação'
       }
       ```
  3. **Rio Grande do Sul's Wine Production and Derivatives Traded**
    - Endpoint: `/trades/{year}`
  4. **Rio Grande do Sul's Importation of Grape Derivatives**
    - Endpoint: `/importations/{year}/{suboption}`
    - Valid suboptions:
       ```python
       VALID_SUBOPTIONS = {
           'subopt_01': 'Vinhos de mesa',
           'subopt_02': 'Espumantes',
           'subopt_03': 'Uvas frescas',
           'subopt_04': 'Uvas passas',
           'subopt_05': 'Suco de uva',
       }
       ```
  5. **Rio Grande do Sul's Exportation of Grape Derivatives**
    - Endpoint: `/exportations/{year}/{suboption}`
    - Valid suboptions:
       ```python
       VALID_SUBOPTIONS = {
           'subopt_01': 'Vinhos de mesa',
           'subopt_02': 'Espumantes',
           'subopt_03': 'Uvas frescas',
           'subopt_04': 'Suco de uva',
       }
       ```

## Install Dependencies
```bash
cd /path/to/your/project
pip install -r requirements.txt
```

## Test
```bash
cd /path/to/your/project
pytest
```

