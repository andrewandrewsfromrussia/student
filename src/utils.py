import json
from typing import Any
import os

PATH_JSON = os.path.join("..", "data", "operations.json")

def read_json_file(path_json:str) -> list[Any] | Any:
    """
    Функция чтения JSON файлов.
    :param path_json: путь к файлу JSON
    :return: список словарей с данными о финансовых транзакциях.
    """
    result = []
    if not os.path.exists(path_json):
        print(f'Ошибка: Файл не найден.')
        return result

    try:
        with open(path_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except:
        return result
