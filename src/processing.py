def filter_by_state(info_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрация операций по ключу state = EXECUTED"""

    result_operations = []
    [result_operations.append(info) for info in info_operations if info["state"] == state]
    return result_operations


def sort_by_date(info_operations: list[dict], reverse: bool = True) -> list[dict]:
    """сортировка операций по дате"""

    result_sort = sorted(info_operations, key=lambda x: x["date"], reverse=reverse)
    return result_sort
