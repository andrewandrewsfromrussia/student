def get_mask_card_number(card_number: int) -> str:
    """
    Возвращает маску введенного номера карты.

    Args:
        card_number: Номер карты.

    Returns:
        Маскированный номер карты в формате ХХХХ ХХ** **** ХХХХ.
    """
    if card_number is not None:
        card_number_check = len(str(card_number))  # Длинна номера карты
        if card_number_check == 16:  # Проверка длинны номера карты
            masked_num = str(card_number)[:6]  # Первые 6 цифр
            masked_num += "******"  # Маска из звездочек
            masked_num += str(card_number)[12:]  # Последние 4 цифры
            masked_num = " ".join(masked_num[i : i + 4] for i in range(0, len(masked_num), 4))  # Добавляем пробелы

            return masked_num  # Возвращаем замаскированный номер карты в виде строки

        return "Введите 16 значный номер карты."  # Возвращаем сообщение об ошибке.

    return "Ввод не может быть пустым."


def get_mask_account(account_number: int) -> str:
    """
    Возвращает маску введенного номера счета

    Args:
        account_number: Номер аккаунта.

    Returns:
        Замаскированный номер аккаунта в формате **ХХХХ.
    """

    if account_number is not None:
        account_number_check = len(str(account_number))  # Длинна номера счета.
        if account_number_check == 20:  # Проверка длинны номера счета.
            masked_acc = "**"  # Новая переменная
            masked_acc += str(account_number)[16:]  # Добавляем последние 4 цифры.

            return masked_acc

        return "Введите 20-ти значный номер счета."  # Возвращаем сообщение об ошибке.

    return "Ввод не может быть пустым."
