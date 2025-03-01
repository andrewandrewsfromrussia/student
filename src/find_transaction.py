import re
from collections import Counter


def find_transactions(transactions, search_string):
    """
    Поиск транзакций по описанию.
    """
    return [
        transaction
        for transaction in transactions
        if "description" in transaction
        and isinstance(transaction["description"], str)
        and re.search(re.escape(search_string), transaction["description"], re.IGNORECASE)
    ]


def count_transaction_types(transactions):
    """
    Подсчитывает количество банковских операций определенного типа.
    """

    transaction_types = [transaction.get("description", "Неизвестный тип") for transaction in transactions]
    return Counter(transaction_types)
