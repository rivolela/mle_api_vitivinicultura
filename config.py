import os

class Config:
    DEBUG = False
    BASE_URL_PRODUCTS = "http://vitibrasil.cnpuv.embrapa.br/index.php?&opcao=opt_02"
    BASE_URL_PROCESSAMENTO = "http://vitibrasil.cnpuv.embrapa.br/index.php?opcao=opt_03"


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    BASE_URL_PRODUCTS = "http://localhost:52330/tests/pages_html_tests/products.html"
    BASE_URL_PROCESSAMENTO = "http://localhost:52330/tests/pages_html_tests/processamento.html"


# Dependency to provide the appropriate configuration based on the environment
def get_config():
    if os.environ.get('ENVIRONMENT') == 'production':
        return Config()
    else:
        return TestConfig()