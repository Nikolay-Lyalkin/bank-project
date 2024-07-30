import json
import logging
import re
from collections import Counter
from typing import Any

import pandas

from src.external_api import convertation

filepath_logger = "C:\\Users\\sereg\\OneDrive\\Рабочий стол\\bank_project\\logs\\utils.log"
logger = logging.getLogger("utils")
file_handler = logging.FileHandler(filepath_logger, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_data_by_operations(filename: str) -> list[dict]:
    """Принимает путь к файлам json, csv, xlsx и возвращает список c вложенными
    словарями с информацией о транзакциях"""
    data_transaction = []
    try:
        if filename.endswith(".json"):
            with open(filename, "r", encoding="utf-8") as f_obg:
                data_transaction = json.load(f_obg)
                logger.info("Спискок с вложенными словарями с информацией о транзакциях успешно создан")
                return data_transaction
        elif filename.endswith(".csv"):
            data_csv = pandas.read_csv(filename, delimiter=";")
            data_transaction = data_csv.to_dict(orient="records")
            logger.info("Спискок с вложенными словарями с информацией о транзакциях успешно создан")
            return data_transaction
        elif filename.endswith(".xlsx"):
            data_xlsx = pandas.read_excel(filename)
            data_transaction = data_xlsx.to_dict(orient="records")
            logger.info("Спискок с вложенными словарями с информацией о транзакциях успешно создан")
            return data_transaction
    except json.JSONDecodeError as ex:
        logger.error(f"{filename} вызывает {ex}")
        return data_transaction
    except FileNotFoundError as ex:
        logger.error(f"{filename} вызывает {ex}")
        return data_transaction


def amount_transaction(transaction: dict) -> Any:
    """Принимает на вход словарь с информацией о транзакции и возвращает сумму транзакции в рублях, если сумма
    транзакции в USD, EUR, то сумма будет конвертирована в RUB"""
    if transaction["operationAmount"]["currency"]["code"] in ["USD", "EUR"]:
        from_currency = transaction["operationAmount"]["currency"]["code"]
        to_currency = "RUB"
        amount = transaction["operationAmount"]["amount"]
        convert = convertation(to_currency, from_currency, amount)
        logger.info("Конвертация выполнена!")
        return convert
    logger.info(f"Конвертация из валюты {transaction['operationAmount']['currency']['code']} выполнена!")
    return transaction["operationAmount"]["amount"]


def search_info(data_transactions: list[dict], search_string: str) -> list[dict]:
    """Принимает на вход список словарией с информацией о транзакциях и строку поиска с описанием транзакции,
    возвращает список словарей с результатом поиска"""

    result_search = [
        i for i in data_transactions if re.search(search_string, str(i["description"]), flags=re.IGNORECASE)
    ]
    return result_search


def counter_description(data_transactions: list[dict], categories: list) -> dict:
    """Принимает на вход список словарией с информацией о транзакциях и список категорий транзакций, возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории"""
    if not isinstance(categories, list):
        raise ValueError("Categories should be a list of strings")
    list_categories = [i["description"] for i in data_transactions if i["description"] in categories]
    counted_category = Counter(list_categories)
    return dict(counted_category)
