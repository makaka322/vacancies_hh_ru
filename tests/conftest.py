import pytest

from src.json_file import JsonFile
from src.vacancies import Vacancy
from src.vacancies_list import VacanciesList


@pytest.fixture
def vacancy_1():
    return Vacancy("0011", "Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет", 10000, 60000)


@pytest.fixture
def vacancy_2():
    return Vacancy("0022", "Python backend", "<https://hh.ru/vacancy/123489>", "Опыт от 1 года", 10000, 30000)


@pytest.fixture
def json_file():
    return JsonFile(r"C:\Users\Chiri\PycharmProjects\vacancies_hh_ru\date\vacancies.json")


@pytest.fixture
def json_data():
    """Фикстура, создающая тестовый json"""

    test_dict = {
        "items": [{"id": "93353083", "premium": False, "name": "Тестировщик комфорта квартир", "department": None}]
    }
    return test_dict


@pytest.fixture
def vacan_list():
    """Фикстура, создающая список словарей с вакансиями"""
    test_list = [
        {
            "id": "108453823",
            "premium": False,
            "name": "Python Backend Developer",
            "department": None,
            "salary": {"from": 200000, "to": 250000, "currency": "KZT", "gross": False},
            "response_url": None,
            "archived": False,
            "apply_alternate_url": "https://hh.ru/applicant/vacancy_response?vacancyId=108453823",
            "url": "https://api.hh.ru/vacancies/108453823?host=hh.ru",
            "alternate_url": "https://hh.ru/vacancy/108453823",
            "snippet": {
                "requirement": "Уверенные знания <highlighttext>Python</highlighttext> (3.10) и "
                "опыт разработки на нем от менее 6 месяцев. ⦁ Опыт работы с фреймворками: Flask, FastApi...",
                "responsibility": "Разработка и поддержка серверной части для WhatsApp ботов на"
                " <highlighttext>Python</highlighttext>. ⦁ Интеграция с внешними API и базами данных (PostgreSQL). ⦁ ",
            },
            "working_time_modes": [],
            "accept_temporary": False,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
        {
            "id": "108424453",
            "premium": False,
            "name": "Python Developer (Remote)",
            "department": None,
            "salary": None,
            "alternate_url": "https://hh.ru/vacancy/108424453",
            "relations": [],
            "snippet": {
                "requirement": "Коммерческий опыт создания веб-приложений с использованием "
                "<highlighttext>Python</highlighttext>-фреймворков (Django, FastAPI, Flask) "
                "от 1 года. Знание <highlighttext>Python</highlighttext> Core и встроенной...",
                "responsibility": None,
            },
            "contacts": None,
            "schedule": {"id": "fullDay", "name": "Полный день"},
            "working_days": [],
            "working_time_intervals": [],
            "working_time_modes": [],
            "accept_temporary": False,
            "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
            "accept_incomplete_resumes": False,
            "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
            "employment": {"id": "full", "name": "Полная занятость"},
            "adv_response_url": None,
            "is_adv_vacancy": False,
            "adv_context": None,
        },
    ]
    return test_list


@pytest.fixture
def vacancy_json():
    vacancy = {
        "id": "108424453",
        "premium": False,
        "name": "Python Developer (Remote)",
        "department": None,
        "salary": None,
        "alternate_url": "https://hh.ru/vacancy/108424453",
        "relations": [],
        "snippet": {
            "requirement": "Коммерческий опыт создания веб-приложений с использованием "
            "<highlighttext>Python</highlighttext>-фреймворков (Django, FastAPI, Flask)"
            " от 1 года. Знание <highlighttext>Python</highlighttext> Core и встроенной...",
            "responsibility": None,
        },
        "contacts": None,
        "schedule": {"id": "fullDay", "name": "Полный день"},
        "working_days": [],
        "working_time_intervals": [],
        "working_time_modes": [],
        "accept_temporary": False,
        "professional_roles": [{"id": "96", "name": "Программист, разработчик"}],
        "accept_incomplete_resumes": False,
        "experience": {"id": "between1And3", "name": "От 1 года до 3 лет"},
        "employment": {"id": "full", "name": "Полная занятость"},
        "adv_response_url": None,
        "is_adv_vacancy": False,
        "adv_context": None,
    }
    return vacancy


@pytest.fixture
def list_vacancies(vacancy_1, vacancy_2):
    list_vac = VacanciesList()
    list_vac.add_vacancy(vacancy_1)
    list_vac.add_vacancy(vacancy_2)
    list_vac.add_vacancy(Vacancy("0012", "Python", "<https://hh.ru/vacancy/123456>", "опыт работы от 2 лет", 15000))
    list_vac.add_vacancy(Vacancy("0013", "Python", "<https://hh.ru/vacancy/123456>", "опыт от 1 года"))
    return list_vac
