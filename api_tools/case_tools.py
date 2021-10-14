from const_for_test_rail import *
import requests
from random import randint


class CaseTools(object):
    @staticmethod
    def add_case(case, section):
        action = 'add_case/' + str(section.section_id)
        data = {"title": case.title,
                "template_id": case.template_id}
        response = requests.post(url=RESULT_URL + action,
                                 json=data, auth=AUTH)
        case.case_id = (response.json().get('id'))
        return response.status_code

    @staticmethod
    def get_case(case):
        action = 'get_case/' + str(case.case_id)
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url=RESULT_URL + action, headers=headers,
                                auth=AUTH)
        return response

    @staticmethod
    def add_result_for_case(case, run_id):
        random_status = randint(1, 5)
        action = 'add_result_for_case/' + str(run_id) + "/" + str(case.case_id)
        data = {"status_id": random_status,
                "comment": case.title}
        response = requests.post(url=RESULT_URL + action,
                                 json=data, auth=AUTH)
        return response.status_code

    @staticmethod
    def delete_case(case):
        action = 'delete_case/' + str(case.case_id)
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url=RESULT_URL + action,
                                 headers=headers, auth=AUTH)
        return response.status_code
