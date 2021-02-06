from TestData import Contants
from utilities.BaseClass import get, get_params, customLogger


class TestAPI2:

    def test_api_test2(self):
        log = customLogger()
        log.info("========Validating Test Case 2 ============")
        data = get_params(function='TIME_SERIES_DAILY', symbol='IBM', apikey=Contants.APIKEY)
        output = get(Contants.URL, params=data)
        assert output['result']['Meta Data']['5. Time Zone'] == 'US/Eastern', "Assertion Failed- Timezone doesnt match"
