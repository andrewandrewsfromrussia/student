import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "state_option, expected",
    [
        (
            "EXECUTED",
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07wsdw-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": ""},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 594226727, "state": "CANCELED", "date": "20180912T21:27:25.241689"},
            ],
        ),
    ],
)
def test_filter_by_state(list_dict: list, state_option: str, expected: list) -> None:
    assert filter_by_state(list_dict, state_option) == expected  # Тест с параметром state == "EXECUTE".
    assert filter_by_state(list_dict, state_option) == expected  # Тест с параметром state == "CANCELED".


@pytest.mark.parametrize(
    "sort_option, expected",
    [
        (
            True,
            [
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07wsdw-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 594226727, "state": "CANCELED", "date": "20180912T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": ""},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": ""},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "20180912T21:27:25.241689"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 41428829, "state": "EXECUTED", "date": "2019-07wsdw-03T18:35:29.512364"},
            ],
        ),
    ],
)
def test_sort_by_date(list_dict: list, expected: list, sort_option: bool) -> None:
    assert sort_by_date(list_dict, sort_option) == expected  # Тест с параметром True.
    assert sort_by_date(list_dict, sort_option) == expected  # Тест с параметром False.
