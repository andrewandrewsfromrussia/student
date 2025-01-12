import os
from typing import Any

import requests
from dotenv import load_dotenv

from src.utils import read_json_file

load_dotenv()
api_key = os.getenv("API_KEY")
path_json = os.path.join("..", "data", "operations.json")
transaction = read_json_file(path_json)


def get_exchange(transaction: dict) -> Any:
    """
    Функция для конвертации валюты в рубли.
    :param transaction: список словарей с данными об операциях.
    :return: сумма в рублях.
    """
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code != "RUB":
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}"
        headers = {"apikey": f"{api_key}"}
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        return round(result["result"], 2)
    else:
        return f"Валюта уже в рублях! {amount}"
