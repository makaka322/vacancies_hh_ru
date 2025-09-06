import pytest

from src.vacancies import Vacancy


def test_vacancies_init(vacancy_1):
    """Тестирование корректности инициализации объектов класса Vacancies"""
    assert vacancy_1.name == "Python Developer"
    assert vacancy_1.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy_1.requirements == "опыт работы от 3 лет"
    assert vacancy_1.salary_from == 10000
    assert vacancy_1.salary_to == 60000


def test_vacancies_init_salary_zero():
    """Тестирование корректности инициализации объектов класса Vacancies c неуказанной зарплатой"""
    vacancy = Vacancy("001", "Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy.name == "Python Developer"
    assert vacancy.url == "<https://hh.ru/vacancy/123456>"
    assert vacancy.requirements == "опыт работы от 3 лет"
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    assert vacancy.currency == "RUB"
    assert vacancy.id == "001"


def test_vacancies_init_salary_negative(capsys):
    """Тестирование корректности инициализации объектов класса Vacancies c неуказанной зарплатой"""
    vacancy = Vacancy("001", "Python Developer", "<https://hh.ru/vacancy/123456>",
                      "опыт работы от 3 лет", -2, -10000)
    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-1] == "Отрицательное значение salary_to заменено на 0"


def test_vacancies_str(vacancy_1):
    """Тестирование магического метода str"""
    assert str(vacancy_1) == (
        "Python Developer, зарплата 10000 - 60000 RUB. Требования: опыт работы от 3 лет. "
        "Полная информация по ссылке: <https://hh.ru/vacancy/123456>"
    )


def test_cast_to_object_list(vacan_list):
    """Тестирование метода преобразования списка словарей вакансия в список объектов класса Vacancy"""
    result = Vacancy.cast_to_object_list(vacan_list)
    assert str(result[0]) == (
        "Python Backend Developer, зарплата 200000 - 250000 KZT. Требования: "
        "Уверенные знания <highlighttext>Python</highlighttext> (3.10) и опыт разработки"
        " на нем от менее 6 месяцев. ⦁ Опыт работы с фреймворками: Flask, FastApi.... "
        "Полная информация по ссылке: https://hh.ru/vacancy/108453823"
    )


def test_equality_vacancies_other_type(vacancy_1):
    """Тестирование сравнения экземпляра класса Вакансия с другим типом"""
    with pytest.raises(TypeError):
        vacancy_1 == 10000


def test_equality_vacancies(vacancy_1, vacancy_2):
    """Тестирование сравнения на равенство по зарплате"""
    assert vacancy_1 == vacancy_2


def test_not_equality_vacancies(vacancy_1):
    """Тестирование сравнения на неравенство по зарплате"""
    vacancy = Vacancy("001", "Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy_1 != vacancy


def test_less_vacancies(vacancy_1):
    """Тестирование сравнения на меньшее"""
    vacancy = Vacancy("001", "Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy < vacancy_1


def test_more_vacancies(vacancy_1):
    """Тестирование сравнения на большее"""
    vacancy = Vacancy("001", "Python Developer", "<https://hh.ru/vacancy/123456>", "опыт работы от 3 лет")
    assert vacancy_1 > vacancy


def test_convert_to_json(vacancy_2):
    """Тестирование преобразования объекта класса Вакансия в словарь"""
    dict_vacan = vacancy_2.convert_to_json()
    assert dict_vacan == {
        "id": "0022",
        "name": "Python backend",
        "url": "<https://hh.ru/vacancy/123489>",
        "requirements": "Опыт от 1 года",
        "salary_from": 10000,
        "salary_to": 30000,
        "currency": "RUB",
    }


