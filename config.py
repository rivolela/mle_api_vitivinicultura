import os

class Config:
    DEBUG = False
    URL_PRODUCTS = "http://vitibrasil.cnpuv.embrapa.br/index.php?&opcao=opt_02&ano="


class TestConfig(Config):
    DEBUG = True
    TESTING = True
    URL_PRODUCTS = "http://localhost:52330/tests/pages_html_tests/products.html"


# Dependency to provide the appropriate configuration based on the environment
def get_config():
    if os.environ.get('ENVIRONMENT') == 'production':
        return Config()
    else:
        return TestConfig()