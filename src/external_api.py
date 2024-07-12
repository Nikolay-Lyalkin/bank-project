import os
from typing import Any

import requests
from dotenv import load_dotenv


def convertation(from_currency: str, to_currency: str, amount: str) -> Any:
    """Принимает валюты из какой в какую необходимо конвертировать и сумму. возвращает результат конвертации"""

    load_dotenv()
    apikey = os.getenv("API_KEY")
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": f"{apikey}"}
    response = requests.get(url, headers=headers)
    result_convert = response.json()
    return result_convert["result"]
