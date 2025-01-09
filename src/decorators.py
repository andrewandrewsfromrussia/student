import traceback
from datetime import datetime
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
            now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            log_message = f"[{now}] Function {func.__name__} called with args: {args}, kwargs: {kwargs}"

            try:
                if filename:
                    with open(filename, "a") as file:
                        file.write(log_message + "\n")
                        file.write(str(result) + "\n")

                else:
                    print(log_message)
                    print(result)

                return result

            except Exception as e:
                error_message = f"[{now}] Error in function {func.__name__}: {e}\n{traceback.format_exc()}"

                if filename:
                    with open(filename, "a") as file:
                        file.write(error_message)

                else:
                    print(error_message)

                raise

        return inner

    return wrapper
