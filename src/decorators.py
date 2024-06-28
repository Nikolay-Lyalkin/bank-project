from functools import wraps
from typing import Any


def log(filename: Any = None) -> Any:
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            if filename:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    with open(filename, "a") as f_obj:
                        f_obj.write(f"\n{func.__name__} error: {type(e)} {e}. Inputs: {args}, {kwargs}.")
                else:
                    print(result)
                    with open(filename, "a") as f_obj:
                        f_obj.write(f"\n{func.__name__} ok")
            else:
                try:
                    result = func(*args, **kwargs)
                except Exception as e:
                    print(f"{type(e)}: {e}")
                else:
                    print(result)

        return inner

    return wrapper
