import pytest

from src.generators import transaction_descriptions


def test_transaction_descriptions(test_dict: list) -> None:
    case = transaction_descriptions(test_dict)
    assert next(case) == "Перевод организации"
    assert next(case) == "Перевод со счета на счет"
    assert next(case) == "Перевод со счета на счет"
    assert next(case) == "Перевод организации"


@pytest.mark.parametrize("list_dict", [([])])
def test_transaction_descriptions_empty(list_dict: list) -> None:
    case = list(transaction_descriptions(list_dict))
    assert case == []
