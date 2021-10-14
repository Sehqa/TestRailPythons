import requests
from const_for_test_rail import *


class RunTools(object):
    @staticmethod
    def add_run(run, suite):
        action = 'add_run/' + str(PROJECT_ID)
        data = {"name": run.name,
                "description": run.description,
                "suite_id": suite.suite_id,
                "include_all": True}
        response = requests.post(url=RESULT_URL + action,
                                 json=data, auth=AUTH)
        run.run_id = (response.json().get('id'))
        return response.status_code

    @staticmethod
    def get_run(run_id):
        action = 'get_run/' + str(run_id)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=RESULT_URL + action, json=headers,
                                auth=AUTH)
        return response.status_code

    @staticmethod
    def delete_run(test_run, test_run_id=0):
        if test_run_id == 0:
            test_run_id = test_run.run_id
        action = 'delete_run/' + str(test_run_id)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=RESULT_URL + action, json=headers,
                                 auth=AUTH)
        return response.status_code
