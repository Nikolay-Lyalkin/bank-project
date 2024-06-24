def get_mask_card_number(num_card: str) -> str:
    """возвращает маску карты"""

    num_card = str(num_card)
    if len(num_card) != 16 or num_card.isdigit() == False:
        return "Вы ввели неверный номер карты"
    return f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"


def get_mask_account(num_account: str) -> str:
    """возвращает максу банковского счёта"""

    num_account = str(num_account)
    if len(num_account) != 6 or num_account.isdigit() == False:
        return "Вы ввели неверный номер счёта"
    return f"**{num_account[-4:]}"
