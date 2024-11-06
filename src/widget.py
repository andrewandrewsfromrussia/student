from datetime import datetime
from typing import List

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str):
    """
    Возвращает строку с замаскированным номером.
    :param
        card: Номер карты или счета в формате ВИЗА ХХХХХХХХХХХХХХХХХ.
    :return:
        Строка с зашифрованным номером.
    """
    if "Счет" in card:
        mask_acc_list = card.split()
        mask_acc: str = mask_acc_list[0] + " " + get_mask_account(int(mask_acc_list[1]))
        return str(mask_acc)
    else:
        mask_card_list = card.split()
        if len(mask_card_list) < 3:
            mask_card = (
                mask_card_list[0] + " " + get_mask_card_number(int(mask_card_list[1]))
            )
            return mask_card
        else:
            mask_card = (
                mask_card_list[0]
                + " "
                + mask_card_list[1]
                + " "
                + get_mask_card_number(int(mask_card_list[2]))
            )
            return mask_card


def get_date(date_str: str) -> str:
    """
    Возвращает дату в формате ДД.ММ.ГГГГ.
    :param
        date: Строка с датой в формате "2024-03-11T02:26:18.671407".
    :return:
        Строка с датой в формате "ДД.ММ.ГГГГ".
    """
    data_object = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    formatted_date = data_object.strftime("%d.%m.%Y")
    return formatted_date
