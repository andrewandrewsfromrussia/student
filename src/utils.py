import json
import logging
import os
from typing import Any

PATH_JSON = os.path.join("..", "data", "operations.json")

logger = logging.getLogger("utils")

logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..\\logs\\utils.log", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s -%(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_json_file(path_json: str) -> list[Any] | Any:
    """
    Функция чтения JSON файлов.
    :param path_json: путь к файлу JSON
    :return: список словарей с данными о финансовых транзакциях.
    """
    result: list[Any] = []
    if not os.path.exists(path_json):
        logger.error("ОШИБКА! Файл не найден.")
        print("ОШИБКА! Файл не найден.")
        return result

    try:
        with open(path_json, "r", encoding="utf-8") as file:
            data = json.load(file)
            logger.info("Чтение файла...")
            return data
    except FileNotFoundError:
        logger.error(f"ОШИБКА! Файл не найден по пути {path_json}")
        print(f"ОШИБКА! Файл не найден по пути {path_json}")
        return result
    except json.JSONDecodeError:
        logger.error(f"ОШИБКА! Неверный формат JSON в файле {path_json}")
        print(f"ОШИБКА! Неверный формат JSON в файле {path_json}")
        return result
    except Exception as e:
        logger.error(f"Неизвестная ошибка! {e}")
        print(f"Неизвестная ошибка! {e}")
        return result
