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


def test_all_scenaries():
    new_suite = TestSuite()
    # Добавили сьюту
    SuiteTools.add_suite(new_suite, PROJECT_ID)
    # Проверка через get запрос что она существует
    assert (SuiteTools.get_suite(new_suite, new_suite.suite_id) == 200)
    # Создаем новый обьект секции
    section = Sections(new_suite.suite_id)
    # Добавляем в сьюту секцию
    SectionTools.add_sections(section)
    # Проверяем создана ли секция при помощи get запроса
    assert(SectionTools.get_section(section) == 200)
    # Добавляем кейс в секцию
    test_case = TestCase()
    CaseTools.add_case(test_case, section)
    # Проверяем что кейс создан
    assert((CaseTools.get_case(test_case)).status_code == 200)
    # Проверяем что данные в кейсе соответствуют
    soft_assert(CaseTools.get_case(test_case).json().get('title') == test_case.title)
    soft_assert(CaseTools.get_case(test_case).json().get('template_id') == 1)
    # Создаем тест ран в нашей сьюте
    test_run = TestRun()
    RunTools.add_run(test_run, new_suite)
    # Проверяем что ран создан
    assert(RunTools.get_run(test_run.run_id) == 200)
    # Добавляем случайный результат кейсу
    CaseTools.add_result_for_case(test_case, test_run.run_id)
    # Удаляем тест ран
    RunTools.delete_run(test_run)
    # Удаляем кейс
    CaseTools.delete_case(test_case)
    # Удаляем секцию
    SectionTools.delete_section(section)
    # Удаляем сьюту
    SuiteTools.delete_suite(new_suite)
