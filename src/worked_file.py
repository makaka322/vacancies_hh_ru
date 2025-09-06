from abc import ABC, abstractmethod


class WorkedFile(ABC):
    """Абстрактый класс для работы с файлами"""

    @abstractmethod
    def read_file(self) -> dict | str:
        """Абстрактный метод для чтения файла"""
        pass

    @abstractmethod
    def write_file(self, vacancy: list[dict]) -> None:
        """Абстрактный метод для добавления данных в файл"""
        pass

    @abstractmethod
    def delete_info_from_file(self, vacancy_del: dict) -> None:
        """Абстрактный метод для удаления данных из файла"""
        pass
