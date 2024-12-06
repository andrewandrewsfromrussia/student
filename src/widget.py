from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    """
    Возвращает строку с замаскированным номером.
    :param
        card: Номер карты или счета в формате ВИЗА ХХХХХХХХХХХХХХХХХ.
    :return:
        Строка с зашифрованным номером.
    """
    # Проверка соответствия типа данных:
    if not isinstance(card, str):
        return "Ошибка данных."

    # Проверка на наличие данных:
    if not card:
        return "Ошибка: введите номер карты или счета."

    if "Счет" in card:
        mask_acc_list = card.split()
        if len(mask_acc_list[1]) == 20:  # Проверка на правильность длинны номера счета.
            mask_acc: str = mask_acc_list[0] + " " + get_mask_account(int(mask_acc_list[1]))
            return str(mask_acc)
        return "Введите 20-ти значный номер счета."
    else:
        mask_card_list = card.split()
        if len(mask_card_list) < 3:
            if len(mask_card_list[1]) == 16:  # Проверка на правильность длинны номера карты.
                mask_card = mask_card_list[0] + " " + get_mask_card_number(int(mask_card_list[1]))
                return mask_card
            return "Введите 16 значный номер карты."
        else:
            if len(mask_card_list[2]) == 16:  # Проверка на правильность длинны номера карты.
                mask_card = (
                    mask_card_list[0] + " " + mask_card_list[1] + " " + get_mask_card_number(int(mask_card_list[2]))
                )
                return mask_card
            return "Введите 16 значный номер карты."


def get_date(date_str: str) -> str:
    """
    Возвращает дату в формате ДД.ММ.ГГГГ.
    :param
        date: Строка с датой в формате "2024-03-11T02:26:18.671407".
    :return:
        Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    # Проверка соответствия типа данных:
    if not isinstance(date_str, str):
        return "Ошибка типа данных."

    # Проверка на наличие данных:
    if not date_str:
        return "Введите дату."

    data_object = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = data_object.strftime("%d.%m.%Y")
    return formatted_date
