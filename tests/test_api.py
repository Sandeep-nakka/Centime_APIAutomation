import pytest

from TestData import Contants
from utilities import BaseClass
from utilities.BaseClass import get, get_params, customLogger


class TestAPI:

    def test_api_test1(self):
        log = customLogger()
        log.info("========Validating Test Case 1 ============")
        data = get_params(function='TIME_SERIES_DAILY', symbol='IBM', apikey=Contants.APIKEY)
        output = get(Contants.URL, params=data)
        assert output['result']['Meta Data']['2. Symbol'] == 'IBM', "Assertion Failed -Symbol doesnt match "
