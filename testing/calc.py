def add(x: float, y: float):
    return x+y


def subtract(x: float, y: float):
    return x-y


def multiply(x: float, y: float):
    return x*y


def divide(x: float, y: float):
    if y == 0:
        raise ZeroDivisionError
    return x/y
