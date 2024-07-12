import json
import logging
from typing import Any

from src.external_api import convertation

filepath_logger = "C:\\Users\\sereg\\OneDrive\\Рабочий стол\\bank_project\\logs\\utils.log"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(filepath_logger, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_by_operations(filename: str) -> list[dict]:
    """Принимает путь к json файлу и возвращает список с вложенными словарями с информацией о транзакциях"""
    json_data_transaction = []
    try:
        with open(filename, "r", encoding="utf-8") as f_obg:
            json_data_transaction = json.load(f_obg)
            logger.info("Спискок с вложенными словарями с информацией о транзакциях успешно создан")
            return json_data_transaction
    except json.JSONDecodeError as ex:
        logger.error(f"{filename} вызывает {ex}")
        return json_data_transaction
    except FileNotFoundError as ex:
        logger.error(f"{filename} вызывает {ex}")
        return json_data_transaction


def amount_transaction(transaction: dict) -> Any:
    """Принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        from_currency = transaction["operationAmount"]["currency"]["code"]
        to_currency = "RUB"
        amount = transaction["operationAmount"]["amount"]
        convert = convertation(to_currency, from_currency, amount)
        logger.info("Конвертация выполнена!")
        return convert
    logger.info(f"Конвертация из валюты {transaction['operationAmount']['currency']['code']} выполнена!")
    return transaction["operationAmount"]["amount"]
