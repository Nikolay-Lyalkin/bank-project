import logging

filepath_logger = "C:\\Users\\sereg\\OneDrive\\Рабочий стол\\bank_project\\logs\\masks.log"
logger = logging.getLogger("masks")
file_handler = logging.FileHandler(filepath_logger, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_card_number(num_card: str) -> str:
    """возвращает маску карты"""

    num_card = str(num_card)
    if len(num_card) != 16 or not num_card.isdigit():
        logger.info(f"Номер карты - {num_card} не соответствует требованиям")
        return "Вы ввели неверный номер карты"
    logger.info(f"Была выполнена маскировка номера карты {num_card}")
    return f"{num_card[0:4]} {num_card[4:6]}** **** {num_card[-4:]}"


def get_mask_account(num_account: str) -> str:
    """возвращает маску банковского счёта"""

    num_account = str(num_account)
    if len(num_account) != 20 or not num_account.isdigit():
        logger.info(f"Номер счёта - {num_account} не соответствует требованиям")
        return "Вы ввели неверный номер счёта"
    logger.info(f"Была выполнена маскировка номера счёта {num_account}")
    return f"**{num_account[-4:]}"


print(get_mask_card_number("1234123412341234"))
