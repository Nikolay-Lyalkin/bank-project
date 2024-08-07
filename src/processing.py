def filter_by_state(info_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Фильтрация операций по ключу state = EXECUTED"""

    result_operations = [info for info in info_operations if info["state"] == state]
    return result_operations


def sort_by_date(info_operations: list[dict], reverse: bool = True) -> list[dict]:
    """Сортировка операций по дате, принимает на вход информацию о банковских операциях и сортирует их по дате"""

    result_sort = sorted(info_operations, key=lambda x: x["date"], reverse=reverse)
    return result_sort
