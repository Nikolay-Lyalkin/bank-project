# Bank project

## Описание:
Bank project - это виджет, который показывает несколько последних успешных банковских операций клиента.

## Установка:
1. Клонируйте репозиторий:
- git clone git@github.com:Nikolay-Lyalkin/bank-project.git
- [скопируйте ключ самостоятельно](https://github.com/Nikolay-Lyalkin/bank-project)
2. Установите зависимости

## Иструкция по использованию:
1. Модуль widget.py принимает счёт или банковскую карту формата:
  - Maestro 1596837868705199
  - Счет 64686473678894779589

  И возвращает маску:
  - Visa Platinum 7000 79** **** 6361
  - Счет **4305
2. Модуль generators.py принимает на вход списки словарей со сведениями об операциях.
  - filter_by_currency() - фильтрует операции по заданной валюте
  - transaction_descriptions() - возвращает описание операций
  - card_number_generator() - генерирует номер карты в заданном диапазоне
3. Модуль decorators.py - содержит декораторы.
- @log() - логирует вызов функции и ее результат в файл или в консоль.
4. Модуль utils.py реализует функции:
- get_data_by_operations() - принимает на вход путь до JSON, CSV, XLSX - файла и возвращающую список словарей с данными о финансовых транзакциях
- amount_transaction() - обрабатывает транзакцию и возвращающает сумму данной транзакции в рублях
5. Модуль external_api.py реализует функцию:
- convertation() - принмает на вход валюту из какой и какую необходимо конвертировать и возвращает результат
6. Модуль main.py реализует функционал проекта, возвращает информацию о транзакциях в виде:
01.01.2020 Перевод с карты на карту
American Express: 2957 86** **** 4974 -> American Express: 6990 78** **** 8331
Сумма: 12764.0 AZN
## Логирование:
В корне проекта в папке logs реализованы выводы логирования модулей utils.py и masks.py
## Тестирование:
В пакете tests проведено тестирование модулей masks, processing, widget, generators, decorators.
В модуле conftest содержатся фикстуры для тестирования.
