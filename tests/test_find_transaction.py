from collections import Counter

import pytest

from src.find_transaction import count_transaction_types, find_transactions


@pytest.fixture
def transaction_data():
    transactions = [
        {'id': 1, 'description': 'Покупка в магазине Пятерочка'},
        {'id': 2, 'description': 'Перевод Иванову'},
        {'id': 3, 'description': 'Оплата коммунальных услуг'},
        {'id': 4, 'description': 'Пополнение счета мобильного телефона'},
        {'id': 5, 'description': 'Снятие наличных в банкомате'},
        {'id': 6, 'description': 'Покупка в интернет-магазине OZON'},
        {'id': 7, 'description': 'Перевод Петрову'},
        {'id': 8, 'description': 'Оплата интернета'},
    ]
    return transactions


def test_find_transactions_empty_search(transaction_data):
    """Тест: Поиск транзакций с пустой строкой поиска."""
    result = find_transactions(transaction_data, "")
    assert len(result) == 8


def test_find_transactions_positive_search(transaction_data):
    """Тест: Поиск транзакций с существующей строкой поиска."""
    search_string = "покупка"
    result = find_transactions(transaction_data, search_string)
    assert len(result) == 2
    assert result[0]['description'] == 'Покупка в магазине Пятерочка'
    assert result[1]['description'] == 'Покупка в интернет-магазине OZON'


def test_find_transactions_case_insensitive_search(transaction_data):
    """Тест: Поиск транзакций без учета регистра."""
    search_string = "ПЕРЕВОД"
    result = find_transactions(transaction_data, search_string)
    assert len(result) == 2


def test_find_transactions_no_match(transaction_data):
    """Тест: Поиск транзакций со строкой, которой нет в описаниях."""
    search_string = "несуществующая строка"
    result = find_transactions(transaction_data, search_string)
    assert len(result) == 0


def test_find_transactions_special_characters(transaction_data):
    """Тест: Поиск транзакций со специальными символами."""
    search_string = "Пятерочка."
    result = find_transactions(transaction_data, search_string)
    assert len(result) == 0

    search_string = "Пятерочка"
    result = find_transactions(transaction_data, search_string)
    assert len(result) == 1


def test_count_transaction_types_basic(transaction_data):
    """Тест: Базовый подсчет типов транзакций."""
    expected_counts = Counter({
        'Покупка в магазине Пятерочка': 1,
        'Перевод Иванову': 1,
        'Оплата коммунальных услуг': 1,
        'Пополнение счета мобильного телефона': 1,
        'Снятие наличных в банкомате': 1,
        'Покупка в интернет-магазине OZON': 1,
        'Перевод Петрову': 1,
        'Оплата интернета': 1,
    })
    result = count_transaction_types(transaction_data)
    assert result == expected_counts


def test_count_transaction_types_empty_list():
    """Тест: Подсчет типов транзакций для пустого списка."""
    result = count_transaction_types([])
    assert result == Counter()


def test_count_transaction_types_missing_description():
    """Тест: Подсчет типов транзакций с отсутствующим описанием."""
    transactions_with_missing_description = [
        {'id': 1, 'description': 'Покупка в магазине'},
        {'id': 2},
        {'id': 3, 'description': 'Перевод Иванову'}
    ]
    expected_counts = Counter({
        'Покупка в магазине': 1,
        'Неизвестный тип': 1,
        'Перевод Иванову': 1
    })
    result = count_transaction_types(transactions_with_missing_description)
    assert result == expected_counts