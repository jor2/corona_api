import requests
from bs4 import BeautifulSoup
import re


class CoronaAPI(object):
    def __init__(self, country='Ireland'):
        self.country = country
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.response = requests.get(self.url)
        self.soup = BeautifulSoup(self.response.content, 'html.parser')

    @property
    def all_country_statistics(self):
        return self.soup.find_all('tr', style="")[1:]

    @property
    def total_stats(self):
        numbers = []
        for result in self.all_country_statistics:
            if 'Total:' in result.text:
                numbers = result.text.split('\n')
        return f'Total\n------------------\nTotal cases: {numbers[2]}\nTotal recovered: {numbers[6]}\nTotal deaths: {numbers[4]}\n'

    @property
    def country_stats(self):
        numbers = []
        for result in self.all_country_statistics:
            if self.country in result.text:
                numbers = result.text.split('\n')
        return f'{self.country}\n------------------\nTotal cases: {numbers[2]}\nTotal recovered: {numbers[6]}\nTotal deaths: {numbers[4]}\n'


print(CoronaAPI().total_stats)
print(CoronaAPI().country_stats)
