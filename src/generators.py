from typing import Any


def filter_by_currency(transactions: Any, currency: str) -> Any:
    """Возвращает операции в которых указана заданная валюта"""

    currency_filter = (x for x in transactions if x["operationAmount"]["currency"]["code"] == currency)
    return currency_filter


def transaction_descriptions(transactions: Any) -> Any:
    """Возвращает описание каждой операции по очереди"""

    description = (x["description"] for x in transactions)
    return description


def card_number_generator(start: int, end: int) -> Any:
    """Генерирует номер карты в заданном диапазоне"""

    while start <= end:
        card_number = str(start)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:16]}"
        yield formatted_card_number
        start += 1
