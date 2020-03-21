import requests
from bs4 import BeautifulSoup
from flask import Flask


class CoronaAPI(object):
    def __init__(self, country='Ireland'):
        self.country = ' '.join([word.capitalize() for word in country.split()])
        self.url = 'https://www.worldometers.info/coronavirus/'
        self.response_html = requests.get(self.url).content
        self.soup = BeautifulSoup(self.response_html, 'html.parser')

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
        return f'{numbers[1]}\n------------------\nTotal cases: {numbers[2]}\nTotal recovered: {numbers[6]}\nTotal deaths: {numbers[4]}\n'


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return CoronaAPI().total_stats


@app.route('/<string:country>', methods=['GET', 'POST'])
def corona_filtered(country):
    return CoronaAPI(country).country_stats


if __name__ == '__main__':
    # print(CoronaAPI('IrelaN').country_stats)
    app.run(debug=True, use_reloader=True)
