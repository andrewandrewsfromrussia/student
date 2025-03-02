from typing import Any, Dict, Generator


def filter_by_currency(transactions: list[dict], value: str) -> Generator[Dict[str, Any], None, None]:
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == value:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int = 0, stop: int = 0) -> Generator[str, Any, None]:
    for _ in range(start, stop + 1):
        card_num = "0" * (16 - len(str(_))) + str(_)
        result = card_num[:4] + " " + card_num[4:8] + " " + card_num[8:12] + " " + card_num[12:16]
        yield result
