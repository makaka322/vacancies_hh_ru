from unittest.mock import Mock, patch

import pytest

from src.api_hh_ru import HeadHunterAPI


def test_get_vacancies_not_connect():
    """Тестирование запроса на вакансии при получении ошибки соединения"""
    mock_response = Mock()
    mock_response.status_code = 400

    with patch("src.api_hh_ru.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="Не удалось получить информацию по вакансиям"):
            vac = HeadHunterAPI()
            vac.get_vacancies("python")


def test_get_vacancies_not_found_vacancy():
    """Тестирование запроса на получение информации по вакансиям, если вакансия не найдена"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": [], "found": 0, "pages": 1, "page": 0, "per_page": 100}

    with patch("src.api_hh_ru.requests.get", return_value=mock_response):
        with pytest.raises(ValueError, match="По указанному запросу нет вакансий"):
            vac = HeadHunterAPI()
            vac.get_vacancies("dsgfdgfgh")


def test_get_vacancies():
    """Тестирование запроса на получение информации по вакансиям"""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "items": [
            {
                "id": "108453823",
                "premium": False,
                "name": "Python Backend Developer",
                "department": None,
                "has_test": False,
                "response_letter_required": True,
            }
        ]
    }

    with patch("src.api_hh_ru.requests.get", return_value=mock_response):
        vac = HeadHunterAPI()
        assert vac.get_vacancies("python")[0] == {
            "id": "108453823",
            "premium": False,
            "name": "Python Backend Developer",
            "department": None,
            "has_test": False,
            "response_letter_required": True,
        }
