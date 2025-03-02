import re
from collections import Counter


def find_transactions(transactions: list, search_string: str) -> list:
    """
    Функция поиска по строке.
    :param transactions: список словарей с операциями.
    :param search_string: строка поиска.
    :return: список словарей по ключу.
    """
    return [
        transaction
        for transaction in transactions
        if "description" in transaction
        and isinstance(transaction["description"], str)
        and re.search(re.escape(search_string), transaction["description"], re.IGNORECASE)
    ]


def count_transaction_types(transactions: list, categories: dict) -> dict:
    """
    Подсчитывает количество банковских операций определенного типа.
    :param transactions: Список словарей с операциями.
    :param categories: Категории операций.
    :return:
    """

    category_counts = Counter()

    for transaction in transactions:
        description = transaction.get("description", "").lower()

        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1

    return dict(category_counts)
