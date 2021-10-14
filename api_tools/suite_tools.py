from const_for_test_rail import *
import requests


class SuiteTools(object):
    @staticmethod
    def add_suite(test_suite, project_number):
        action = 'add_suite/' + str(project_number)
        data = {"name": test_suite.name,
                "description": test_suite.description}
        response = requests.post(url=RESULT_URL + action,
                                 json=data, auth=AUTH)
        test_suite.suite_id = response.json().get('id')
        return response.status_code

    @staticmethod
    def delete_suite(test_suite, number_suite=0):
        if number_suite == 0:
            number_suite = test_suite.suite_id
        action = 'delete_suite/' + str(number_suite)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=RESULT_URL + action, auth=AUTH, headers=headers)
        return response.status_code

    @staticmethod
    def get_suite(test_suite, id_suite=0):
        if id_suite == 0:
            id_suite = test_suite.suite_id
        action = 'get_suite/' + str(id_suite)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=RESULT_URL + action, auth=AUTH, headers=headers)
        return response.status_code
