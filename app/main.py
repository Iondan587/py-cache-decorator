from typing import Callable

from typing import Callable


def cache(func: Callable) -> Callable:
    num = {}

    def wrapper(*args):
        if args in num:
            print("Getting from cache")
            return num[args]
        else:
            print("Calculating new result")
            result = func(*args)
            num[args] = result
            return result

    return wrapper








