from multiprocessing import Value

DEBUG = Value("b", False)


def get_debug() -> bool:
    return DEBUG.value


def set_debug(debug: bool) -> None:
    with DEBUG.get_lock():
        DEBUG.value = debug
