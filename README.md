# API Vitivinicultura (Machine Learning Engineering - Pos Tech FIAP)
API from Embrapa vitivinicultura website (v.2)

## Site Embrapa
[Embrapa Vitivinicultura](http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_01)

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
                                     |   Vitivinicultura Embrapa  |             |   (IasS:  AWS)    |
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

## Vitinicultura API

- [API documentation and endpoints](https://mle-api-vitivinicultura.onrender.com/docs)
- This API was delivered on a Free Web Service in the Render Platform. As it is free, the instance will spin down with inactivity, which can delay requests by 50 seconds or more.


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

