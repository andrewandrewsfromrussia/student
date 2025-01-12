import json
import os
from typing import Any

PATH_JSON = os.path.join("..", "data", "operations.json")


def read_json_file(path_json: str) -> list[Any] | Any:
    """
    Функция чтения JSON файлов.
    :param path_json: путь к файлу JSON
    :return: список словарей с данными о финансовых транзакциях.
    """
    result: list[Any] = []
    if not os.path.exists(path_json):
        print("Ошибка: Файл не найден.")
        return result

    try:
        with open(path_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути {path_json}")
        return result
    except json.JSONDecodeError:
        print(f"Ошибка: Неверный формат JSON в файле {path_json}")
        return result
    except Exception as e:
        print(f"Неизвестная ошибка {e}")
        return result
