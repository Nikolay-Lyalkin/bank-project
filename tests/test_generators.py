from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions):
    usd_transactions = filter_by_currency(transactions, "USD")
    assert next(usd_transactions)["id"] == 939719570
    assert next(usd_transactions)["id"] == 142264268


def test_transaction_descriptions(transactions):
    descriptions = transaction_descriptions(transactions)
    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"


def test_card_number_generator():
    result = card_number_generator(1, 5)
    assert next(result) == "0000 0000 0000 0001"
    assert next(result) == "0000 0000 0000 0002"
