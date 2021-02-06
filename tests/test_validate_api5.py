from TestData import Contants
from utilities.BaseClass import get, get_params, customLogger


class TestAPI5:

    def test_api_test5(self):
        log = customLogger()
        log.info("========Validating Test Case 5 ============")
        data = get_params(function='TIME_SERIES_DAILY', symbol='IBM2', apikey=Contants.APIKEY)
        output = get(Contants.URL, params=data)
        assert "Invalid" in output['result']['Error Message'], "Assertion Failed"

