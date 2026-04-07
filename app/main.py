from typing import Callable


def cache(func: Callable) -> Callable:
    storage = {}

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Формуємо стабільний ключ із позиційних та іменованих аргументів
        # Сортування kwargs.items() гарантує, що порядок аргументів не змінить ключ
        key = (args, tuple(sorted(kwargs.items())))

        if key in storage:
            print("Getting from cache")
            return storage[key]
        else:
            print("Calculating new result")
            # Викликаємо функцію з усіма типами аргументів
            result = func(*args, **kwargs)
            storage[key] = result
            return result

    return wrapper








