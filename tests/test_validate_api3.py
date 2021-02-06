from TestData import Contants
from utilities.BaseClass import get, get_params, customLogger


class TestAPI3:

    def test_api_test3(self):
        log = customLogger()
        log.info("========Validating Test Case 3 ============")
        data = get_params(function='TIME_SERIES_DAILY2', symbol='IBM', apikey=Contants.APIKEY)
        output = get(Contants.URL, params=data)
        assert "does not exist" in output['result']['Error Message'], "Assertion Failed"
