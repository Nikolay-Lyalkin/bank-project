import pytest

from src.masks import get_mask_account, get_mask_card_number


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
        ("12345678901234567890", "**7890"),
        ("", "Вы ввели неверный номер счёта"),
        ("1234as12121234567890", "Вы ввели неверный номер счёта"),
    ],
)
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
