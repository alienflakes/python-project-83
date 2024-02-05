import requests
from bs4 import BeautifulSoup


def get_response(url_name):
    response = requests.get(url_name)
    response.raise_for_status()
    return response


def get_url_data(response):
    url_data = {
        'description': '',
        }
    url_data['status_code'] = response.status_code
    soup = BeautifulSoup(response.text, 'html.parser')
    url_data['h1'] = soup.h1.text if soup.h1 else ''
    url_data['title'] = soup.title.text if soup.title else ''
    if soup.meta.get('name') == 'description':
        url_data['description'] = soup.meta.get('content', '')
    return url_data
