def get_mask_card_number(num_card: int) -> str:
    """возвращает маску карты"""

    num_card = str(num_card)
    return f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"


def get_mask_account(num_account: int) -> str:
    """возвращает максу банковского счёта"""

    num_account = str(num_account)
    return f"**{num_account[-4:]}"
