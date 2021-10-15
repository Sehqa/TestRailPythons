from smart_assertions import soft_assert, verify_expectations
from const_for_test_rail import *
from framework.test_suite import TestSuite
from framework.sections import Sections
from framework.test_cases import TestCase
from framework.test_run import TestRun
from api_tools.suite_tools import SuiteTools
from api_tools.section_tools import SectionTools
from api_tools.case_tools import CaseTools
from api_tools.run_tools import RunTools


def teardown():
    verify_expectations()


def test_all_action():
    new_suite = TestSuite()
    # Добавили сьюту
    assert (SuiteTools.add_suite(new_suite, PROJECT_ID).status_code == 200)
    # Проверка через get запрос что она существует
    assert (SuiteTools.get_suite(new_suite, new_suite.suite_id).status_code == 200)
    # Создаем новый обьект секции
    section = Sections(new_suite.suite_id)
    # Добавляем в сьюту секцию
    assert (SectionTools.add_sections(section).status_code == 200)
    # Проверяем создана ли секция при помощи get запроса
    assert (SectionTools.get_section(section).status_code == 200)
    # Добавляем кейс в секцию
    test_case = TestCase()
    assert (CaseTools.add_case(test_case, section).status_code == 200)
    # Проверяем что кейс создан
    assert ((CaseTools.get_case(test_case)).status_code == 200)
    # Проверяем что данные в кейсе соответствуют
    soft_assert(CaseTools.get_case(test_case).json().get('title') == test_case.title)
    soft_assert(CaseTools.get_case(test_case).json().get('template_id') == 1)
    # Создаем тест ран в нашей сьюте
    test_run = TestRun()
    assert (RunTools.add_run(test_run, new_suite).status_code == 200)
    # Проверяем что ран создан
    assert (RunTools.get_run(test_run.run_id).status_code == 200)
    # Добавляем случайный результат кейсу
    assert (CaseTools.add_result_for_case(test_case, test_run.run_id).status_code == 200)
    # Удаляем тест ран
    assert (RunTools.delete_run(test_run).status_code == 200)
    # Удаляем кейс
    assert (CaseTools.delete_case(test_case).status_code == 200)
    # Удаляем секцию
    assert (SectionTools.delete_section(section).status_code == 200)
    # Удаляем сьюту
    assert (SuiteTools.delete_suite(new_suite).status_code == 200)
