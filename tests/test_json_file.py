from unittest.mock import patch

import pytest

from src.json_file import JsonFile


def test_json_file_init(json_file):
    """Тестирование инициации экземпляра класса JsonFile"""
    assert json_file.file_name == r"C:\Users\natal\PycharmProjects\my_pro\vacancies_hh_ru\date\vacancies.json"


@patch("src.json_file.json.load")
def test_read_file(mock_reader, json_file, json_data):
    """Тестирование чтения данных из json - файла"""
    mock_reader.return_value = json_data
    result = json_file.read_file()
    assert result == json_data
    mock_reader.assert_called_once()


def test_read_json_not_found_file():
    """Тестирует, если файл не найден"""
    file = JsonFile("vac.json")
    with pytest.raises(FileNotFoundError):
        file.read_file()


def test_write_file(vacan_list):
    """Тестирование добавления новых вакансий в json - файла"""
    file = JsonFile("C:/Users/natal/PycharmProjects/my_pro/vacancies_hh_ru/tests/test_vacancies.json")
    file.write_file(vacan_list)
    with open(
        r"C:\Users\natal\PycharmProjects\my_pro\vacancies_hh_ru\date\vacancies.json", "r+", encoding="UTF-8"
    ) as f:
        line = f.readlines()
        assert line[0:16] == [
            "[\n",
            "  {\n",
            '    "id": "108444291",\n',
            '    "premium": false,\n',
            '    "name": "Младший Back-end разработчик",\n',
            '    "department": null,\n',
            '    "has_test": false,\n',
            '    "response_letter_required": false,\n',
            '    "area": {\n',
            '      "id": "1",\n',
            '      "name": "Москва",\n',
            '      "url": "https://api.hh.ru/areas/1"\n',
            "    },\n",
            '    "salary": {\n',
            '      "from": 80000,\n',
            '      "to": 100000,\n',
        ]


def test_write_file_not_found_file():
    """Тестирует, если файл не найден"""
    file = JsonFile("vac.json")
    with pytest.raises(FileNotFoundError):
        file.write_file([])


def test_delete_info_from_file_not_found(capsys):
    """Тестирование удаление указанной вакансии, если она не была найдена"""
    file = JsonFile("C:/Users/natal/PycharmProjects/my_pro/vacancies_hh_ru/tests/test_vacancies.json")
    file.delete_info_from_file(
        "Python Developer, зарплата 10000 - 60000 руб. Требования: опыт работы от 3 лет. "
        "Полная информация по ссылке: <https://hh.ru/vacancy/123456>"
    )
    message = capsys.readouterr()
    assert message.out == "Вакансия не была удалена, т.к. она не была найдена\n"


def test_delete_info_from_file_(capsys, vacancy_json):
    """Тестирование удаление указанной вакансии, если она не была найдена"""
    file = JsonFile("C:/Users/natal/PycharmProjects/my_pro/vacancies_hh_ru/tests/test_vacancies.json")
    file.delete_info_from_file(vacancy_json)
    message = capsys.readouterr()
    assert message.out == "Вакансия удалена из файла\n"
