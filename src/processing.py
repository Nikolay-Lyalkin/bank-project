def filter_by_state(info_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """фильтрация операций по ключу state = EXECUTED"""

    result_operations = []
    [result_operations.append(info) for info in info_operations if info["state"] == state]
    return result_operations
