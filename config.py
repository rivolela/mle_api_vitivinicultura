import os

class Config:
    DEBUG = False
    BASE_URL_PRODUCTS = "http://vitibrasil.cnpuv.embrapa.br/index.php?&opcao=opt_02"
    BASE_URL_PROCESSAMENTO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"
    BASE_URL_COMERCIALIZACAO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_04"
    BASE_URL_IMPORTACAO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_05"

class TestConfig(Config):
    DEBUG = True
    TESTING = True
    BASE_URL_PRODUCTS = "http://localhost:52330/tests/pages_html_tests/products.html"
    BASE_URL_PROCESSAMENTO = "http://localhost:52330/tests/pages_html_tests/processamento.html"
    BASE_URL_COMERCIALIZACAO = "http://localhost:52330/tests/pages_html_tests/comercializacao.html"
    BASE_URL_IMPORTACAO = "http://localhost:52330/tests/pages_html_tests/importacao.html"


# Dependency to provide the appropriate configuration based on the environment
def get_config():
    if os.environ.get('ENVIRONMENT') == 'production':
        return Config()
    else:
        return TestConfig()