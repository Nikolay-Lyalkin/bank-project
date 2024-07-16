from datetime import datetime as dt

from src import masks


def mask_account_card(account_card: str) -> str:
    """Общая маскировка карты и счета"""

    list_account_card = " ".join(account_card.split(" ")[0:-1])
    if list_account_card[0] == "Счет" or list_account_card[0] == "Счёт":
        return f"{list_account_card[0]}: {masks.get_mask_account(list_account_card[1])}"
    else:
        return f"{list_account_card[0]}: {masks.get_mask_card_number(list_account_card[1])}"


def get_data(data: str) -> str:
    """Возвращает строку с датой"""

    type_datetime = dt.strptime(data, "%Y-%m-%dT%H:%M:%S.%f")
    correct_data = type_datetime.strftime("%d.%m.%Y")
    return correct_data
