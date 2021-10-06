import unittest
from unittest.mock import patch

import corona
from tests.test_html import html


class TestCoronaAPI(unittest.TestCase):
    class MockRequests(object):
        @property
        def content(self):
            return html

    @patch('corona.requests.get', return_value=MockRequests())
    def test_total_stats(self, mock_requests):
        expected_result = 'Total<br>------------------<br>Total cases: 500,000<br>Total recovered: 5<br>Total deaths: 5,000<br>'
        actual_result = corona.CoronaAPI().total_stats
        self.assertEqual(expected_result, actual_result)

    @patch('corona.requests.get', return_value=MockRequests())
    def test_country_stats(self, mock_requests):
        mock_country = 'Ireland'
        expected_result = f'{mock_country}<br>------------------<br>Total cases: 300,000<br>Total recovered: 30<br>Total deaths: 30,000'
        actual_result = corona.CoronaAPI(mock_country).country_stats.strip()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
