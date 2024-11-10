def filter_by_state(records: list, state="EXECUTED") -> list:
    """
    Возвращает новый список словарей, у которых ключ state соответствует указанному значению.
    :param records: Принимает на вход список словарей с данными о банковских операциях.
    :param state: EXECUTED(default) or CANCELED.
    :return: Возвращает новый список словарей.
    """

    new_records = []

    for record in records:
        if state in record["state"]:
            new_records.append(dir)

    return new_records
