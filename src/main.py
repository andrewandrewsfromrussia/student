import os

import openpyxl

from src.find_transaction import find_transactions
from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.reader_csv_xlsx import read_csv, read_xlsx
from src.utils import read_json_file

PATH_JSON = os.path.join("..", "data", "operations.json")


def main():
    """
    Основная логика программы.
    """

    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    while True:
        try:
            choice = int(input())
            if choice in [1, 2, 3]:
                break
            else:
                print("Некорректный ввод. Пожалуйста, выберите 1, 2 или 3.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")

    if choice == 1:
        print("Для обработки выбран JSON-файл.")
        filename = os.path.join("..", "data", "operations.json")
        try:
            transactions = read_json_file(filename)
            print("Файл успешно загружен.")
        except FileNotFoundError:
            print("Файл не найден.")
            return
        except json.JSONDecodeError:
            print("Ошибка декодирования JSON.")
            return

    elif choice == 2:
        print("Для обработки выбран CSV-файл.")
        filename = os.path.join("..", "data", "transactions.csv")
        try:
            transactions = read_csv(filename)
            print("Файл успешно загружен.")
        except FileNotFoundError:
            print("Файл не найден.")
            return
    elif choice == 3:
        print("Для обработки выбран XLSX-файл.")
        filename = os.path.join("..", "data", "transactions_excel.xlsx")
        try:
            transactions = read_xlsx(filename)
            print("Файл успешно загружен.")
        except FileNotFoundError:
            print("Файл не найден.")
            return
        except openpyxl.utils.exceptions.InvalidFileException:
            print("Ошибка открытия XLSX файла.")
            return
        except KeyError:
            print("Ошибка чтения XLSX файла. Проверьте заголовки столбцов.")
            return

    # Фильтрация по статусу
    available_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
        if status.upper() in available_statuses:
            transactions = filter_by_state(transactions, status)
            print(f'Операции отфильтрованы по статусу "{status.upper()}"')
            break
        else:
            print(f'Статус операции "{status}" недоступен.')

    # Сортировка по дате
    sort_by_date_prompt = input("Отсортировать операции по дате? y/n\n").lower()
    if sort_by_date_prompt == "y":
        sort_order = input("Отсортировать по убыванию? y/n\n").lower()
        if sort_order == "y":
            transactions = sort_by_date(transactions)
        else:
            transactions = sort_by_date(transactions, False)

    # Фильтрация по валюте
    only_rub = input("Выводить только рублевые тразакции? y/n\n").lower()
    if only_rub == "y":
        transactions = filter_by_currency(transactions, "RUB")

    # Фильтрация по ключевому слову
    filter_by_keyword_prompt = input(
        "Отфильтровать список транзакций по определенному слову в описании? y/n\n"
    ).lower()
    if filter_by_keyword_prompt == "y":
        keyword = input("Введите ключевое слово для фильтрации:\n")
        transactions = find_transactions(transactions, keyword)

    print("Распечатываю итоговый список транзакций...")
    print(transactions)


if __name__ == "__main__":
    main()
