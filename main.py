from typing import List, Dict, Any


# Заглушка для API hh.ru — в реальности нужно реализовать запросы к API
class HHVacancyAPI:
    def __init__(self):
        # Пример данных
        self.vacancies = [
            {
                "id": "1",
                "name": "Python Developer",
                "salary_from": 120000,
                "salary_to": 150000,
                "description": "Разработка на Python, Django, Flask",
            },
            {
                "id": "2",
                "name": "Java Developer",
                "salary_from": 100000,
                "salary_to": 130000,
                "description": "Опыт работы с Java и Spring",
            },
            {
                "id": "3",
                "name": "Frontend Developer",
                "salary_from": 90000,
                "salary_to": 110000,
                "description": "JavaScript, React, Vue",
            },
            {
                "id": "4",
                "name": "Data Scientist",
                "salary_from": 150000,
                "salary_to": 180000,
                "description": "Анализ данных, Python, машинное обучение",
            },
            {
                "id": "5",
                "name": "Python Junior",
                "salary_from": 70000,
                "salary_to": 90000,
                "description": "Начинающий Python разработчик",
            },
        ]

    def search_vacancies(self, query: str) -> List[Dict[str, Any]]:
        # Имитируем поиск по названию вакансии
        return [vac for vac in self.vacancies if query.lower() in vac["name"].lower()]

    def get_top_n_by_salary(self, n: int) -> List[Dict[str, Any]]:
        # Сортируем по максимальной зарплате (salary_to)
        sorted_vac = sorted(
            self.vacancies, key=lambda v: v.get("salary_to", 0), reverse=True
        )
        return sorted_vac[:n]

    def search_by_keyword_in_description(self, keyword: str) -> List[Dict[str, Any]]:
        return [
            vac
            for vac in self.vacancies
            if keyword.lower() in vac["description"].lower()
        ]


def interactive_console():
    api = HHVacancyAPI()

    print("Добро пожаловать в поиск вакансий hh.ru!")
    while True:
        print("\nВыберите действие:")
        print("1 - Ввести поисковый запрос для вакансий")
        print("2 - Получить топ N вакансий по зарплате")
        print("3 - Получить вакансии с ключевым словом в описании")
        print("4 - Выход")

        choice = input("Введите номер действия: ").strip()

        if choice == "1":
            query = input("Введите поисковый запрос (название вакансии): ").strip()
            results = api.search_vacancies(query)
            if results:
                print(f"Найдено {len(results)} вакансий:")
                for vac in results:
                    print(
                        f"- {vac['name']} (от {vac['salary_from']} до {vac['salary_to']} руб.)"
                    )
            else:
                print("Вакансии не найдены.")

        elif choice == "2":
            n_str = input("Введите количество вакансий для вывода (N): ").strip()
            if not n_str.isdigit() or int(n_str) <= 0:
                print("Пожалуйста, введите положительное число.")
                continue
            n = int(n_str)
            results = api.get_top_n_by_salary(n)
            print(f"Топ {n} вакансий по зарплате:")
            for vac in results:
                print(
                    f"- {vac['name']} (от {vac['salary_from']} до {vac['salary_to']} руб.)"
                )

        elif choice == "3":
            keyword = input("Введите ключевое слово для поиска в описании: ").strip()
            results = api.search_by_keyword_in_description(keyword)
            if results:
                print(f"Найдено {len(results)} вакансий с ключевым словом '{keyword}':")
                for vac in results:
                    print(
                        f"- {vac['name']} (от {vac['salary_from']} до {vac['salary_to']} руб.)"
                    )
            else:
                print("Вакансии не найдены.")

        elif choice == "4":
            print("Выход из программы. До свидания!")
            break

        else:
            print("Некорректный ввод. Пожалуйста, выберите действие из списка.")


if __name__ == "__main__":
    interactive_console()