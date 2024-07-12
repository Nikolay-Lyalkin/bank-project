import json
from typing import Any

from src.external_api import convertation


def get_data_by_operations(filename: str) -> list[dict]:
    """Принимает путь к json файлу и возвращает словарь с данными"""
    json_data_transaction = []
    try:
        with open(filename, "r", encoding="utf-8") as f_obg:
            json_data_transaction = json.load(f_obg)
            return json_data_transaction
    except json.JSONDecodeError:
        return json_data_transaction
    except FileNotFoundError:
        return json_data_transaction


def amount_transaction(transaction: dict) -> Any:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        from_currency = transaction["operationAmount"]["currency"]["code"]
        to_currency = "RUB"
        amount = transaction["operationAmount"]["amount"]
        convert = convertation(to_currency, from_currency, amount)
        return convert
    return transaction["operationAmount"]["amount"]
