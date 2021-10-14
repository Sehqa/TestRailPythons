import os

URL_TEST_RAIL = 'https://tr.a1qa.com/'
CONST_API = 'index.php?/api/v2/'
AUTH = (os.environ.get('API_LOGIN'), os.environ.get('API_PASS'))
PROJECT_ID = '140'
RESULT_URL = URL_TEST_RAIL + CONST_API
