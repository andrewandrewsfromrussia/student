import csv
import os
from typing import Any, Dict, List

import openpyxl


def read_csv(csv_path: str) -> List[Dict[str, Any]]:
    """
    Функция для чтения csv файлов.
    :param csv_path: путь к csv файлу.
    :return: список словарей с операциями.
    """
    result = []
    try:
        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                result.append(row)
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {csv_path}")
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
        return result
    return result


def read_xlsx(xlsx_path: str) -> List[Dict[str, Any]]:
    """
    Функция для чтения Excel файлов.
    :param xlsx_path: путь к xlsx файлу.
    :return: список словарей с операциями.
    """
    result: list = []
    try:
        workbook = openpyxl.load_workbook(xlsx_path)
        sheet = workbook.active
        if sheet is None:
            print(f"Ошибка: нет активного листа в файле {xlsx_path}")
            return result
        header = [cell.value for cell in sheet[1]]
        for row in sheet.iter_rows(min_row=2):
            row_dict = {}
            for i, cell in enumerate(row):
                row_dict[header[i]] = cell.value
                result.append(row_dict)
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {xlsx_path}")
        return result
    except Exception as e:
        print(f"Ошибка: {e}")
    return result


csv_path = os.path.join("..", "data", "transactions.csv")
xlsx_path = os.path.join("..", "data", "transactions_excel.xlsx")
