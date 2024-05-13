import requests
import urllib.request

def fetch_page(url):
    response = urllib.request.urlopen(url)
    if response.getcode() == 200:
        html = response.read().decode('utf-8')
        html = trata_html(html)
        return html
    else:
        return None


def trata_html(input):
    return " ".join(input.split()).replace('> <', '><')

