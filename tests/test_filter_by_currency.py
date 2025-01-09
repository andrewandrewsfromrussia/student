import pytest

from src.generators import filter_by_currency


@pytest.mark.parametrize("value", [("USD")])
def test_filter_by_currency_usd(test_dict: list, value: str, test_dict_usd: list) -> None:
    usd_transactions = list(filter_by_currency(test_dict, value))
    assert usd_transactions == test_dict_usd


@pytest.mark.parametrize("value", [("EUR")])
def test_filter_by_currency_eur(test_dict: list, value: str, test_dict_eur: list) -> None:
    eur_transactions = list(filter_by_currency(test_dict, value))
    assert eur_transactions == test_dict_eur


@pytest.mark.parametrize("value", [("")])
def test_filter_by_currency_empty_value(test_dict: list, value: str) -> None:
    empty_value_transactions = list(filter_by_currency(test_dict, value))
    assert empty_value_transactions == []


@pytest.mark.parametrize("value", [("EUR")])
def test_filter_by_currency_empty_dict(empty_list: list, value: str) -> None:
    empty_dict_transactions = list(filter_by_currency(empty_list, value))
    assert empty_dict_transactions == []
