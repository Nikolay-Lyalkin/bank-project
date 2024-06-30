import pytest
import json
from unittest.mock import Mock, patch
from src.utils import get_data_by_operations, amount_transaction, convertation

patch("builtins.open")
def test_get_data_by_operations(mock_open):
    mock_file = mock_open.return_value.__enter__.return_value
    mock_file.loads.return_value = 'test data'
    assert get_data_by_operations('test.txt') == 'test data'


