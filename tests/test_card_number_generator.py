import pytest

from src.generators import card_number_generator


@pytest.mark.parametrize("start, stop", [(5, 10)])
def test_card_number_generator(start: int, stop: int) -> None:
    case = card_number_generator(start, stop)
    assert next(case) == "0000 0000 0000 0005"
    assert next(case) == "0000 0000 0000 0006"
    assert next(case) == "0000 0000 0000 0007"
    assert next(case) == "0000 0000 0000 0008"
    assert next(case) == "0000 0000 0000 0009"
    assert next(case) == "0000 0000 0000 0010"


def test_card_number_generator_empty() -> None:
    case = card_number_generator()
    assert next(case) == "0000 0000 0000 0000"
