import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize(
    "number, expected",
    [
        ("1234123412341234", "1234 12** **** 1234"),
        ("", "Вы ввели неверный номер карты"),
        ("1234asdf12341234", "Вы ввели неверный номер карты"),
    ],
)
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "account, expected",
    [
        ("123456", "**3456"),
        ("", "Вы ввели неверный номер счёта"),
        ("1234as", "Вы ввели неверный номер счёта"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
