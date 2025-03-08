import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "bank_account, expected",
    [
        ("Счет 64686473678894779589", "Счет **9589"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("MasterCard 7158300734726758122", "Введите 16 значный номер карты."),
        ("Visa Classic 68319824767376", "Введите 16 значный номер карты."),
        ("Счет 6468647367889477958912", "Введите 20-ти значный номер счета."),
        ("Счет 646864736477958912", "Введите 20-ти значный номер счета."),
        ("", "Ошибка: введите номер карты или счета."),
        (646864736477958912, "Ошибка данных."),
    ],
)
def test_mask_account_card(bank_account: str, expected: str) -> None:
    assert mask_account_card(bank_account) == expected  # Тест счетов.
    assert mask_account_card(bank_account) == expected  # Тест с Maestro.
    assert mask_account_card(bank_account) == expected  # Тест с MasterCart.
    assert mask_account_card(bank_account) == expected  # Тест с Visa Classic.
    assert mask_account_card(bank_account) == expected  # Тест с Visa Gold.
    assert mask_account_card(bank_account) == expected  # Тест с Visa Platinum.
    assert mask_account_card(bank_account) == expected  # Тест на длинну номера карты.
    assert mask_account_card(bank_account) == expected  # Тест на длинну номера карты.
    assert mask_account_card(bank_account) == expected  # Тест на длинну номера счета.
    assert mask_account_card(bank_account) == expected  # Тест на длинну номера счета.
    assert mask_account_card(bank_account) == expected  # Тест на наличие данных.
    assert mask_account_card(bank_account) == expected  # Тест на тип данных.


@pytest.mark.parametrize(
    "date, expected",
    [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "Введите дату."), (20240311, "Ошибка типа данных.")],
)
def test_get_date(date: str, expected: str) -> None:
    assert get_date(date) == expected  # Тест правильности работы.
    assert get_date(date) == expected  # Тест на наличие данных.
    assert get_date(date) == expected  # Тест типа данных
