import json
from typing import Any
from external_api import convertation

filename = "C:/Users/sereg/OneDrive/Рабочий стол/bank_project/data/operations.json"

def get_data_by_operations(filename: str) -> list[dict]:
    """Принимает путь к json файлу и возвращает словарь с данными"""
    try:
        with open(filename) as f_obj:
            data_json = json.load(f_obj)
    except FileNotFoundError:
        return []
    else:
        data = json.loads(data_json)
        if type(data) is not list:
            return []
        return data


def amount_transaction(id_transaction: int, filename: str) -> Any:
    """Принимает на вход id транзакции и возвращает сумму транзакции в рублях"""
    data = get_data_by_operations(filename)
    for d in data:
        if d["id"] == id_transaction:
            if d["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
                from_currency = d["operationAmount"]["currency"]["code"]
                to_currency = "RUB"
                amount = d["operationAmount"]["amount"]
                convert = convertation(to_currency, from_currency, amount)
                return convert
            return d["operationAmount"]["amount"]


# print(get_data_by_operations(filename))

# print(amount_transaction(939719570, filename))
