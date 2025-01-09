from functools import wraps
from typing import Any, Callable, Optional


def log(filename: Optional[str]) -> Callable:
    """
    Декоратор для логирования результатов работы функции.
    :param filename: путь к txt файлу для записи. При отсутствии - результат выводится в терминал.
    :return: декорированная функция.
    """
    def wrapper(func: Any) -> Any:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            """
            Внутренняя функция "обертка", выполняет функцию логирования.
            :param args: позиционные аргументы.
            :param kwargs:именованные аргументы.
            :return:результат выполнения.
            """
            result = func(*args, **kwargs)
            if filename:
                with open(filename, "w") as file:
                    file.write(str(result))
            else:
                print(result)
            return result

        return inner

    return wrapper
