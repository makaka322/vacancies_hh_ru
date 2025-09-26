from abc import ABC, abstractmethod
from typing import Any
import requests


class BaseHH(ABC):
    """Абстрактный класс для работы с API сервиса с вакансиями"""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict[Any, Any]]:
        """Абстрактный метод для получения вакансии"""
        pass


class HeadHunterAPI(BaseHH):
    """Класс для работы с API HeadHunter"""

    __url: str
    __params: dict
    __vacancies: list

    def __init__(self) -> None:
        """Инициализация экземпляров класса HeadHunterAPI"""

        self.__url = "https://api.hh.ru/vacancies"
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies = []

    def __is_connect(self) -> bool:
        """Метод для подключения к API"""
        response = requests.get(self.__url)
        if response.status_code == 200:
            return True
        raise ValueError("Не удалось получить информацию по вакансиям")

    def get_vacancies(self, keyword: str, page_count: int = 1) -> list[dict[Any, Any]]:
        """Метод получения вакансия с сайта hh.ry"""
        self.__params["text"] = keyword

        while self.__params.get("page") != page_count and self.__is_connect():
            response = requests.get(self.__url, params=self.__params)
            if len(response.json()["items"]) <= 0:
                raise ValueError("По указанному запросу нет вакансий")
            else:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
        return self.__vacancies