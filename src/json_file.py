import json
import os
from typing import Any

from src.worked_file import WorkedFile


class JsonFile(WorkedFile):
    """Класс для работы с JSON-файлами"""

    __file_name: str

    def __init__(self, file_name: str = "vacancies.json") -> None:
        """Инициация экземпляров класса JsonFile"""
        self.__file_name = file_name

    @property
    def file_name(self) -> str:
        """Геттер для просмотра пути файла"""
        return self.__file_name

    def __is_exists_file(self) -> bool:
        if os.path.exists(self.__file_name):
            return True
        raise FileNotFoundError("Файл не найден")

    def read_file(self) -> list[Any]:
        """Метод для чтения данных из json-файла"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            with open(full_path, "r", encoding="UTF-8") as json_file:
                try:
                    data = json.load(json_file)
                except Exception as e:
                    print(f"Произошла ошибка {e}")
                    data = []
            return data

    def write_file(self, vacancy: list[dict]) -> None:
        """Метод для добавления данных в файл"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            vacan_data = self.read_file()

            for vacancy_add in vacancy:
                if vacancy_add not in vacan_data:
                    vacan_data.append(vacancy_add)

            with open(full_path, "r+", encoding="UTF-8") as json_file:
                json.dump(vacan_data, json_file, indent=2, ensure_ascii=False)

    def delete_info_from_file(self, vacancy_del: dict) -> None:
        """Метод для удаления данных из файла"""
        if self.__is_exists_file():
            full_path = os.path.abspath(self.__file_name)
            vacan_data = self.read_file()
            try:
                vacan_data.remove(vacancy_del)
            except ValueError:
                print("Вакансия не была удалена, т.к. она не была найдена")
            else:
                with open(full_path, "w", encoding="UTF-8") as json_file:
                    json.dump(vacan_data, json_file, indent=2, ensure_ascii=False)
                print("Вакансия удалена из файла")
