import requests
import unittest
from unittest.mock import patch, Mock
from src.api_hh_ru import HeadHunterAPI  # замените your_module на имя вашего файла без .py


class TestHeadHunterAPI(unittest.TestCase):

    @patch("src.api_hh_ru.requests.get")
    def test_get_vacancies_success_single_page(self, mock_get):
        # Мокаем успешный ответ API с одной страницей вакансий
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {
            "items": [
                {"id": "1", "name": "Python Developer"},
                {"id": "2", "name": "Java Developer"}
            ]
        }
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Python", page_count=1)

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[0]["name"], "Python Developer")
        mock_get.assert_called_once()

    @patch("src.api_hh_ru.requests.get")
    def test_get_vacancies_success_multiple_pages(self, mock_get):
        # Мокаем два ответа API для двух страниц
        mock_response_page1 = Mock()
        mock_response_page1.raise_for_status.return_value = None
        mock_response_page1.json.return_value = {
            "items": [{"id": "1", "name": "Python Developer"}]
        }

        mock_response_page2 = Mock()
        mock_response_page2.raise_for_status.return_value = None
        mock_response_page2.json.return_value = {
            "items": [{"id": "2", "name": "Java Developer"}]
        }

        mock_get.side_effect = [mock_response_page1, mock_response_page2]

        api = HeadHunterAPI()
        vacancies = api.get_vacancies("Developer", page_count=2)

        self.assertEqual(len(vacancies), 2)
        self.assertEqual(vacancies[1]["name"], "Java Developer")
        self.assertEqual(mock_get.call_count, 2)

    @patch("src.api_hh_ru.requests.get")
    def test_get_vacancies_no_vacancies(self, mock_get):
        # Мокаем ответ API без вакансий
        mock_response = Mock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"items": []}
        mock_get.return_value = mock_response

        api = HeadHunterAPI()
        with self.assertRaises(ValueError) as context:
            api.get_vacancies("NonexistentJob", page_count=1)
        self.assertIn("нет вакансий", str(context.exception))

    @patch("src.api_hh_ru.requests.get")
    def test_get_vacancies_request_exception(self, mock_get):
        # Мокаем исключение при запросе
        mock_get.side_effect = requests.RequestException("Ошибка сети")

        api = HeadHunterAPI()
        with self.assertRaises(ConnectionError) as context:
            api.get_vacancies("Python", page_count=1)
        self.assertIn("Ошибка при подключении к API", str(context.exception))


if __name__ == "__main__":
    unittest.main()