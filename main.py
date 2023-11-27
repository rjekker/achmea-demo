"""main.py
---
Bla di bla
"""


def bla():
    pass


def print_hi(name: str) -> None:
    """Deze functie print hallo"""
    print("hallo")
    lst = [
        1,
        2,
        3,
        4,
    ]
    return lst.append(10)


def my_decorator(func, x):
    "..."

    def wrapped_func(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapped_func
