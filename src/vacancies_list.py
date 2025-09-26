import re
from typing import Any

from src.vacancies import Vacancy


class VacanciesList:
    """Класс для работы со списком вакансий"""

    __slots__ = ("__vacancies", "index")

    def __init__(self, vacancies: list[Any] = None) -> None:
        """Конструктор для инициализации экземпляра класса."""
        if vacancies is None:
            self.__vacancies = []
        else:
            self.__vacancies = vacancies
        self.index = 0

    @property
    def vacancies(self):
        """Геттер для корректного вывода списка вакансий"""
        vacancy_str = ''
        for vacancy in self.__vacancies:
            vacancy_str += f'{str(vacancy)}\n'
        return vacancy_str

    def __len__(self):
        """Метод для подсчета количества вакансий в списке"""
        return len(self.__vacancies)

    def __iter__(self):
        """Возвращает итератор."""
        self.index = 0
        return self

    def __next__(self):
        """Возвращает следующую вакансию из списка вакансий"""
        if self.index < len(self.__vacancies):
            vacancy = self.__vacancies[self.index]
            self.index += 1
            return vacancy
        else:
            raise StopIteration

    def __getitem__(self, item):
        """Возвращает вакансию из списка по указанному индексу"""
        return self.__vacancies[item]

    def add_vacancy(self, vacancy: Vacancy) -> list:
        """Метод для добавления вакансии в список"""
        if isinstance(vacancy, Vacancy):
            try:
                if vacancy.id in (vac.id for vac in self.__vacancies):
                    raise ValueError("Такая вакансия уже есть")
            except ValueError:
                print("Такая вакансия уже есть")
            else:
                self.__vacancies.append(vacancy)
                print("Вакансия добавлена")
                return self.__vacancies
        else:
            raise TypeError

    def delete_vacancy(self, vacancy: Vacancy) -> list:
        """Метод для удаления вакансии из списка"""
        if isinstance(vacancy, Vacancy):
            try:
                if vacancy.id not in (vac.id for vac in self.__vacancies):
                    raise AttributeError("Вакансия не была удалена, т.к. не была найдена")
            except AttributeError as e:
                print(e)
            else:
                self.__vacancies.remove(vacancy)
                print("Вакансия удалена")
                return self.__vacancies
        else:
            raise TypeError

    def get_top_vacancies(self, count_vacancies: int = 10) -> list:
        """Метод для вывода заданного количества вакансий"""
        if len(self.__vacancies) < count_vacancies:
            return self.__vacancies
        return self.__vacancies[0:count_vacancies]

    def sort_vacancies(self) -> None:
        """Метод сортировки списка вакансий по salary_from"""
        self.__vacancies = sorted(self.__vacancies, reverse=True)

    def filter_vacancies(self, word: str) -> None:
        """Метод фильтрации вакансия по заданным словам в имени и требованиях"""
        new_vacan = VacanciesList()
        try:
            for vacancy in self.__vacancies:
                if re.findall(word, vacancy.name, flags=re.IGNORECASE) or re.findall(
                    word, vacancy.requirements, flags=re.IGNORECASE
                ):
                    new_vacan.add_vacancy(vacancy)

            self.__vacancies = new_vacan
            if len(self.__vacancies) == 0:
                raise Exception("По вашему запросу ничего не найдено")
        except Exception as e:
            print(e)
        else:
            print(f"По Вашему запросу найдено {len(self.__vacancies)} вакансий")

    def get_vacancies_by_salary(self, salary_from: int | float, salary_to: int | float) -> None:
        """Метод фильтрации вакансий по зарплате"""
        if salary_from > salary_to:
            n = salary_from
            salary_from = salary_to
            salary_to = n
        new_vacan = VacanciesList()
        try:
            for vacancy in self.__vacancies:
                if vacancy.salary_from is not None and salary_from <= vacancy.salary_from <= salary_to:
                    new_vacan.add_vacancy(vacancy)

            self.__vacancies = new_vacan
            if len(self.__vacancies) == 0:
                raise ValueError("По вашему запросу ничего не найдено")
        except ValueError as e:
            print(str(e))
        else:
            print(f"По Вашему запросу найдено {len(self.__vacancies)} вакансий")
