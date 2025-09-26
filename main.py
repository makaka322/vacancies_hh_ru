from src.api_hh_ru import HeadHunterAPI
from src.vacancies import Vacancy
from src.vacancies_list import VacanciesList
from src.json_file import JsonFile

hh_api = HeadHunterAPI()


def main():
    """Главная функция приложения"""
    answer_user = input("""Добро пожаловать в программу получения вакансий с сайта hh.ry по заданному запросу. "
Введите запрос (например: python junior):\n""")

    file_vacancy = JsonFile("../vacancies_hh_ru/date/vacancies.json")
    file_vacancy.write_file(hh_api.get_vacancies(answer_user))

    hh_vacancies = file_vacancy.read_file()

    vacancies = Vacancy.cast_to_object_list(hh_vacancies)

    vacancies_list = VacanciesList(vacancies)

    print('Вакансии были успешно получены.')

    answer_word = input('Отфильтровать вакансии по ключевому слову(да/нет)?')
    if answer_word.lower() == 'да':
        ans_word = input('Введите слово или фразу для фильтрации вакансий: ')
        vacancies_list.filter_vacancies(ans_word)

    answer_filter = input('Отфильтровать вакансии по диапазону зарплат(да/нет)?')
    if answer_filter.lower() == 'да':

        flag_answer = True
        while flag_answer:
            ans_filt = input('Введите диапазон зарплат через запятую: ').split(', ')

            if ans_filt[0].isdigit() and ans_filt[1].isdigit():
                vacancies_list.get_vacancies_by_salary(int(ans_filt[0]), int(ans_filt[1]))
                flag_answer = False
            else:
                print('Некорректный ввод. Введите числа')

    answer_sort = input('Отсортировать вакансии по зарплате(да/нет)?')
    if answer_sort.lower() == 'да':
        vacancies_list.sort_vacancies()

    if len(vacancies_list) == 0:
        print("Не найдено ни одной вакансии, подходящей под Ваши условия фильтрации")
    else:
        print(f"Всего вакансий в выборке: {len(vacancies_list)}\n")

        flag_answer = True
        while flag_answer:
            answer_count_vacan = input("""Введите количество вакансий для вывода в топ N:\n""")
            if answer_count_vacan.isdigit():
                flag_answer = False
            else:
                print('Некорректный ввод. Введите число')

        print("Распечатываю итоговый список вакансий...\n")
        top_vacancies = vacancies_list.get_top_vacancies(int(answer_count_vacan))
        for vacancy in top_vacancies:
            print(vacancy)


if __name__ == "__main__":
    main()
