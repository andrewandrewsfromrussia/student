import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        (1234123412341234, "1234 12** **** 1234"),
        (123412341234, "Введите 16 значный номер карты."),
        (12341234123412341234, "Введите 16 значный номер карты."),
        (None, "Ввод не может быть пустым."),
    ],
)
def test_get_mask_card_number(card_number: int, expected: str) -> None:
    assert get_mask_card_number(card_number) == expected  # Тест на правильность работы.
    assert get_mask_card_number(card_number) == expected  # Тест на длинну номера карты №1.
    assert get_mask_card_number(card_number) == expected  # Тест на длинну номера карты №2.
    assert get_mask_card_number(card_number) == expected  # Тест на наличие переданных данных.


@pytest.mark.parametrize(
    "account_number, expected",
    [
        (12341234123412341234, "**1234"),
        (123412341234, "Введите 20-ти значный номер счета."),
        (1234123412341234123412341234, "Введите 20-ти значный номер счета."),
        (None, "Ввод не может быть пустым."),
    ],
)
def test_get_mask_account(account_number: int, expected: str) -> None:
    assert get_mask_account(account_number) == expected  # Тест на правильность работы.
    assert get_mask_account(account_number) == expected  # Тест на длинну номера счета №1.
    assert get_mask_account(account_number) == expected  # Тест на длинну номера счета №2.
    assert get_mask_account(account_number) == expected  # Тест на наличие переданных данных.
