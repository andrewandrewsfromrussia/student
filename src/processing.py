def filter_by_state(records: list, state: str = "EXECUTED") -> list:
    """
    Фильтрует записи по статусу (state).
    """
    filtered_records = []
    for record in records:
        if record.get("state", "").upper() == state.upper():
            filtered_records.append(record)
    return filtered_records


def sort_by_date(records: list, sort_option: bool = True) -> list:
    """
    Сортирует список словарей по убыванию(default) или возрастанию.
    :param records: принимает список словарей с данными о бансковских операциях.
    :param sort_option: True(default), отвечает за направление сортировки (на убывание по умолчанию).
    :return: Отсортированный по дате список словарей.
    """
    # Проверка соответствия типа данных:
    if not isinstance(records, list):
        return "Ошибка данных."

    # Основная структура:
    sorted_records = []
    if sort_option:
        sorted_records = sorted(records, key=lambda record: record["date"], reverse=True)
    elif sort_option is not True:
        sorted_records = sorted(records, key=lambda record: record["date"])
    return sorted_records
