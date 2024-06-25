import pytest

from src.widget import get_data, mask_account_card


@pytest.mark.parametrize(
    "account_card, expected",
    [
        ("Счет 12345678901234567890", "Счет: **7890"),
        ("Счёт 12345678901234567890", "Счёт: **7890"),
        ("Счет 1234567890123456ww90", "Счет: Вы ввели неверный номер счёта"),
        ("Master Card 1234123412341234", "Master Card: 1234 12** **** 1234"),
        ("Visa 123412341234123a", "Visa: Вы ввели неверный номер карты"),
    ],
)
def test_mask_account_card(account_card, expected):
    mask_account_card(account_card) == expected


def test_get_data(date):
    assert get_data(date) == "11.07.2018"
