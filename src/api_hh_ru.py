from abc import ABC, abstractmethod
from typing import Any, List, Dict
import requests


class BaseHH(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword: str, page_count: int = 1) -> List[Dict[str, Any]]:
        """Абстрактный метод для получения вакансий"""
        pass


class HeadHunterAPI(BaseHH):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Инициализация экземпляра класса HeadHunterAPI"""
        self._url = "https://api.hh.ru/vacancies"
        self._vacancies: List[Dict[str, Any]] = []

    def get_vacancies(self, keyword: str, page_count: int = 1) -> List[Dict[str, Any]]:
        """Получение вакансий с сайта hh.ru"""
        params = {"text": keyword, "page": 0, "per_page": 100}
        self._vacancies.clear()

        for page in range(page_count):
            params["page"] = page
            try:
                response = requests.get(self._url, params=params)
                response.raise_for_status()
            except requests.RequestException as e:
                raise ConnectionError(f"Ошибка при подключении к API: {e}")

            data = response.json()
            items = data.get("items", [])
            if not items:
                # Если вакансий нет, можно прервать цикл
                break
            self._vacancies.extend(items)

        if not self._vacancies:
            raise ValueError("По указанному запросу нет вакансий")

        return self._vacancies


# Пример использования
if __name__ == "__main__":
    hh_api = HeadHunterAPI()
    try:
        vacancies = hh_api.get_vacancies("Python developer", page_count=2)
        for vac in vacancies:
            print(vac["name"], "-", vac["employer"]["name"])
    except Exception as e:
        print("Ошибка:", e)
