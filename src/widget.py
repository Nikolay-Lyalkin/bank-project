import masks


def mask_account_card(account_card: str) -> str:
    """общая маскировка карты и счета"""

    list_account_card = account_card.split(" ")
    if list_account_card[0] == "Счет":
        return f"{list_account_card[0]} {masks.get_mask_account(int(list_account_card[1]))}"
    else:
        return f"{list_account_card[0]} {masks.get_mask_card_number(int(list_account_card[1]))}"
