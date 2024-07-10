from unittest.mock import patch

from src.external_api import convertation


@patch("requests.get")
def test_convertation(mock_get):
    """Проверка функции конвертирующей сумму транзакции в рубли"""
    mock_get.return_value.json.return_value = {"result": 2500}
    assert convertation("USD", "RUB", "2500") == 2500
