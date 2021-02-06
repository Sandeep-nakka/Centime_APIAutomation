from TestData import Contants
from utilities.BaseClass import get, get_params, customLogger


class TestAPI4:

    def test_api_test4(self):
        log = customLogger()
        log.info("========Validating Test Case 4 ============")
        data = get_params(function='TIME_SERIES_DAILY', symbol='IBM', apikey=Contants.APIKEY)
        output = get(Contants.URL, params=data)
        response = output['result']['Time Series (Daily)']['2021-02-05']
        assert "121.0000" in response.values(), "Assertion Failed - Values doesnt match"
        assert "121.8100" in response.values(), "Assertion Failed - Values doesnt match"
        assert "120.5200" in response.values(), "Assertion Failed - Values doesnt match"
        assert "4565727" in response.values(), "Assertion Failed - Values doesnt match"
