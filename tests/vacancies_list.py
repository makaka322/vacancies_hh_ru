import pytest

from src.vacancies import Vacancy
from src.vacancies_list import VacanciesList


def test_vacancies_list_init(vacan_list):
    """Тестирование инициализации объекта класса VacanciesList"""
    list_vac = VacanciesList(vacan_list)
    assert len(list_vac) == 2
    assert list_vac[1] == {
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
    }


def test_vacancies_list_iterator(vacan_list):
    """Тестирование работы итератора"""
    list_vac = VacanciesList(vacan_list)
    iter(list_vac)

    assert list_vac.index == 0
    assert next(list_vac)["name"] == "Python Backend Developer"
    assert next(list_vac)["name"] == "Python Developer (Remote)"
    assert list_vac.index == 2

    with pytest.raises(StopIteration):
        next(list_vac)


def test_add_vacancy(capsys, vacancy_1, vacancy_2):
    """Тестирование добавления новой вакансии в список"""
    list_vac = VacanciesList()
    list_vac.add_vacancy(vacancy_1)
    list_vac.add_vacancy(vacancy_2)
    assert len(list_vac) == 2
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Вакансия добавлена"
    assert list_vac[0] == vacancy_1

    list_vac.add_vacancy(vacancy_2)
    assert len(list_vac) == 2
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Такая вакансия уже есть"


def test_add_vacancy_other_type():
    """Тестирование попытки добавления не объекта класса Вакансия"""
    list_vac = VacanciesList()
    with pytest.raises(TypeError):
        list_vac.add_vacancy("dfgfgf")


def test_delete_vacancy(capsys, list_vacancies, vacancy_1):
    """Тестирование добавления новой вакансии в список"""
    assert len(list_vacancies) == 4

    list_vacancies.delete_vacancy(vacancy_1)
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Вакансия удалена"
    assert len(list_vacancies) == 3

    list_vacancies.delete_vacancy(vacancy_1)
    assert len(list_vacancies) == 3
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Вакансия не была удалена, т.к. не была найдена"


def test_get_top_vacancies(list_vacancies, vacancy_1):
    """Тестирование вывода указанного количества вакансий"""
    test_list = list_vacancies.get_top_vacancies(2)
    assert len(test_list) == 2
    assert test_list[0] == vacancy_1
    test_list = list_vacancies.get_top_vacancies()
    assert len(test_list) == 4


def test_sort_vacancies(list_vacancies, vacancy_1, vacancy_2):
    list_vacancies.sort_vacancies()
    assert len(list_vacancies) == 4
    assert list_vacancies[0] == Vacancy(
        "0012", "Python", "<https://hh.ru/vacancy/123456>", "опыт работы от 2 лет", 15000
    )
    assert list_vacancies[1] == vacancy_1
    assert list_vacancies[2] == vacancy_2
    assert list_vacancies[3] == Vacancy("0013", "Python", "<https://hh.ru/vacancy/123456>", "опыт работы от 0 лет")


def test_filter_vacancies_in_name(list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному слову в имени"""
    list_vacancies.filter_vacancies("developer")
    assert len(list_vacancies) == 1
    assert list_vacancies[0].name == "Python Developer"


def test_filter_vacancies_in_requirements(capsys, list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному слову в имени"""
    list_vacancies.filter_vacancies("опыт от 1")
    assert len(list_vacancies) == 2
    assert list_vacancies[0].name == "Python backend"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "По Вашему запросу найдено 2 вакансий"


def test_filter_vacancies_not_found(capsys, list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному слову в имени"""
    list_vacancies.filter_vacancies("pyton")
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "По вашему запросу ничего не найдено"


def test_get_vacancies_by_salary(capsys, list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному диапазону зарплаты"""
    list_vacancies.get_vacancies_by_salary(10000, 15000)
    assert len(list_vacancies) == 3
    assert list_vacancies[0].name == "Python Developer"
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "По Вашему запросу найдено 3 вакансий"


def test_get_vacancies_by_salary_not_found(capsys, list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному сдиапазону зарплаты"""
    list_vacancies.get_vacancies_by_salary(6000000, 1000000)
    assert len(list_vacancies) == 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "По вашему запросу ничего не найдено"


def test_get_vacancies_by_salary_exchange(capsys, list_vacancies):
    """Тестирование фильтрации списка вакансий по заданному диапазону зарплаты"""
    list_vacancies.get_vacancies_by_salary(15000, 10000)
    assert len(list_vacancies) == 3
