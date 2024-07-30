from datetime import datetime as dt

from src.processing import filter_by_state, sort_by_date
from src.utils import get_data_by_operations, search_info
from src.widget import get_data, mask_account_card

if __name__ == "__main__":
    # Приветствие и выбор файла с которым пользователь будет работать
    print(
        """Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
    )
    file_number = int(input())

    while file_number not in [1, 2, 3]:
        print(
            """Вы ввели неверный пункт меню.
        Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла"""
        )
        file_number = int(input())

    if file_number == 1:
        print("Для обработки выбран JSON-файл.")
        data = get_data_by_operations("C:/Users/sereg/OneDrive/Рабочий стол/bank_project/data/operations.json")
    elif file_number == 2:
        print("Для обработки выбран CSV-файл.")
        data = get_data_by_operations("C:/Users/sereg/OneDrive/Рабочий стол/bank_project/data/transactions.csv")
    elif file_number == 3:
        print("Для обработки выбран XLSX-файл.")
        data = get_data_by_operations("C:/Users/sereg/OneDrive/Рабочий стол/bank_project/data/transactions_excel.xlsx")

    # Фильтр по статусу транзакции
    filter_by_status = input(
        "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки \
статусы: EXECUTED, CANCELED, PENDING\n"
    ).upper()
    while filter_by_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f'Статус операции "{filter_by_status}" недоступен.')
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию.\
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )
    result_filter = filter_by_state(data, state=filter_by_status)

    # Сортировка по дате
    sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
    while sort_date not in ["да", "нет"]:
        sort_date = input("Отсортировать операции по дате? Да/Нет\n").lower()
    if sort_date == "да":
        increase_or_decrease = input("'по возрастанию' или 'по убыванию'\n").lower()
        while increase_or_decrease not in ["по возрастанию", "по убыванию"]:
            increase_or_decrease = input("Введите верно данные: 'по убыванию' или 'по возрастанию'\n")
        if increase_or_decrease == "по убыванию":
            result_filter = sort_by_date(result_filter, reverse=True)
        else:
            result_filter = sort_by_date(result_filter, reverse=False)

    # Фильтр по валюте
    filter_by_rub_transactions = input("Выводить только рублевые тразакции? Да/Нет\n")
    while filter_by_rub_transactions not in ["да", "нет"]:
        filter_by_rub_transactions = input("Выводить только рублевые тразакции? Да/Нет\n")
    if filter_by_rub_transactions == "да":
        if file_number == 1:
            result_filter = [i for i in result_filter if i["operationAmount"]["currency"]["code"] == "RUB"]
        else:
            result_filter = [i for i in result_filter if i["currency_code"] == "RUB"]

    # Фильтр по определенному слову в описании транзакции
    filter_by_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    while filter_by_word not in ["да", "нет"]:
        filter_by_word = input(
            "Ответьте, пожалуйста, праильно! Отфильтровать список транзакций по определенному\
    слову в описании? Да/Нет\n"
        )
    if filter_by_word == "да":
        result_filter = search_info(
            result_filter,
            search_string=input(
                "Введите слово или сочетание слов по которому\
 хотите отфильтровать\n"
            ),
        )

    # Результат
    if result_filter:
        for result in result_filter:
            if file_number == 1:
                print(f"{get_data(result['date'])} {result['description']}")
            else:
                type_datetime = dt.strptime(result["date"], "%Y-%m-%dT%H:%M:%SZ")
                correct_data = type_datetime.strftime("%d.%m.%Y")
                print(f"{correct_data} {result['description']}")
            if result["description"] == "Открытие вклада":
                print(f"{mask_account_card(result['to'])}")
            else:
                print(f"{mask_account_card(result['from'])} -> {mask_account_card(result['to'])}")
            if file_number == 1:
                print(
                    f"Сумма: {result['operationAmount']['amount']} {result['operationAmount']['currency']['name']}\n"
                )
            else:
                print(f"Сумма: {result['amount']} {result['currency_code']}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации.")
