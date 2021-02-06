import inspect
import json
import logging
import requests
from ratelimit import limits, sleep_and_retry

from TestData import Contants


def get_params(function, symbol, apikey, outputsize='compact'):
    data = {'function': function, 'symbol': symbol, 'apikey': apikey, 'outputsize': outputsize}
    return data


@sleep_and_retry
@limits(calls=5, period=60)
@limits(calls=500, period=86400)
def get(url, headers=None, params=None):
    log = customLogger()
    if headers is None:
        headers = {'Content-Type': 'application/json'}
    response = dict()
    log.info("API URL: " + url)
    log.info("Params:  " + str(params))
    res = requests.get(url, headers=headers, params=params)
    log.info("Response code: " + str(res.status_code))
    if res.status_code == 200:
        try:
            response_json = json.loads(res.text)
        except Exception:
            raise Exception("API Response is not a JSON Object ")
        response['result'] = response_json
    else:
        response['result'] = res.text
    log.info("Response: " + str(response))
    return response


def customLogger():
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)  # filehandler object
    logger.setLevel(logging.DEBUG)
    return logger
