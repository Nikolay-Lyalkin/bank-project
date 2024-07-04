import json
from unittest.mock import patch, mock_open

from src.utils import get_data_by_operations



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