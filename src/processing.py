def filter_by_state(records: list, state: str = "EXECUTED") -> list:
    """
    Возвращает новый список словарей, у которых ключ state соответствует указанному значению.
    :param records: Принимает на вход список словарей с данными о банковских операциях.
    :param state: EXECUTED(default) or CANCELED.
    :return: Возвращает новый список словарей.
    """

    new_records = []

    for record in records:
        if state == record["state"]:
            new_records.append(record)

    return new_records


def sort_by_date(records: list, sort_option: bool = True) -> list:
    """
    Сортирует список словарей по убыванию(default) или возрастанию.
    :param records: принимает список словарей с данными о бансковских операциях.
    :param sort_option: True(default), отвечает за направление сортировки (на убывание по умолчанию).
    :return: Отсортированный по дате список словарей.
    """

    sorted_records = []

    if sort_option:
        sorted_records = sorted(records, key=lambda record: record["date"], reverse=True)
    elif sort_option is not True:
        sorted_records = sorted(records, key=lambda record: record["date"])

    return sorted_records
