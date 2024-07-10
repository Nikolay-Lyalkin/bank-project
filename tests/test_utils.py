from unittest.mock import mock_open, patch

from src.utils import amount_transaction, get_data_by_operations


def test_get_data_by_operations():
    """Функуия-тест для проверки. что json-файл читается корректно"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": "2019-08-26T10:50:58.294041", "operationAmount": '
        '{"amount": "31957.58", "currency": '
        '{"name": "руб.", "code": "RUB"}}}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_by_operations("path_to_file.json")
        assert data == [
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
            }
        ]


def test_get_data_by_operations_json_JSONDecodeError():
    """Функуия-тест для проверки. что исключение json.JSONDecodeError обрабатывается корректно"""
    mock_data = (
        '[{"id": 441945886, "state": "EXECUTED", "date": 2019-08-26T10:50:58.294041, "operationAmount": '
        '{"amount": "31957.58", "currency": '
        '{"name": "руб.", "code": "RUB"}}}]'
    )
    with patch("builtins.open", mock_open(read_data=mock_data)):
        data = get_data_by_operations("path_to_file.json")
        assert data == []


def test_get_data_by_operations_FileNotFoundError():
    """Функуия-тест для проверки. что исключение FileNotFoundError обрабатывается корректно"""
    assert get_data_by_operations("filename") == []


@patch("requests.get")
def test_amount_transaction_usd(mock_get):
    """Проверка функционала, что функция принимает сумму в USD и возвращает в рублях"""
    transaction = {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    mock_get.return_value.json.return_value = {"result": 2500}
    assert amount_transaction(transaction) == 2500


def test_amount_transaction_rub():
    """Проверка функционала, что функция принимает сумму в RUB и возвращает сумму"""
    transaction = {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
    assert amount_transaction(transaction) == "31957.58"
