import requests
from bs4 import BeautifulSoup


class Networker:
    @staticmethod
    def get_soup(link):
        response = requests.get(link)
        response.raise_for_status()

        data = response.text
        soup = BeautifulSoup(data, "html.parser")
        return soup
