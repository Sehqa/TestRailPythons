import requests
from const_for_test_rail import *


class SectionTools(object):
    @staticmethod
    def add_sections(section, project_id=PROJECT_ID):
        action = 'add_section/' + str(project_id)
        data = {"name": section.name,
                "description": section.description,
                "suite_id": section.suite_id}
        response = requests.post(url=RESULT_URL + action,
                                 json=data, auth=AUTH)
        section.section_id = (response.json().get('id'))
        return response.status_code

    @staticmethod
    def delete_section(section, section_id=0):
        if section_id == 0:
            section_id = section.section_id
        headers = {'Content-Type': 'application/json'}
        action = 'delete_section/' + str(section_id)
        response = requests.post(url=RESULT_URL + action, headers=headers, auth=AUTH)
        return response.status_code

    @staticmethod
    def get_section(section, section_id=0):
        if section_id == 0:
            section_id = section.section_id
        headers = {'Content-Type': 'application/json'}
        action = 'get_section/' + str(section_id)
        response = requests.get(url=RESULT_URL + action, headers=headers, auth=AUTH)
        return response.status_code
