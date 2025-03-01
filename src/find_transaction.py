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

    category_counts = Counter()

    for transaction in transactions:
        description = transaction.get("description", "").lower()

        for category in categories:
            if category.lower() in description:
                category_counts[category] += 1

    return dict(category_counts)
