import logging
import os
from functools import wraps
from time import time


def checkdir(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        print(f"Function {func.__name__!r} works in {os.getcwd()}")
        print(f"Other things in this dir: {os.listdir()}")
        result = func(*args, **kwargs)
        return result

    return wrapper_function


def timeit(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result

    return wrapper_function


def verbose(func):
    @wraps(func)
    def wrapper_function(*args, **kwargs):
        print(f"\nRunning function {func.__name__!r} ...")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__!r} executed")
        return result

    return wrapper_function


def logit(func):
    print("Log started...")

    @wraps(func)
    def wrapper_function(*args, **kwargs):
        logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)
        logging.info(
            f'Running "{func.__name__}" with arguments {args} and keyword arguments {kwargs}'
        )
        result = func(*args, **kwargs)
        return result

    return wrapper_function


def decorator_with_argument(prefix):
    def decorator(func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            print(f"\n{prefix} - running function {func.__name__!r} ...")
            result = func(*args, **kwargs)
            print(f"{prefix} - function {func.__name__!r} executed")
            return result

        return wrapper_function

    return decorator


class DecoratorClass(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"Call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_with_argument("sample prefix")
# @logit
# @timeit
# @checkdir
# @verbose
# @DecoratorClass
def calculate_fibonacci(n):
    a, b = 0, 1

    for i in range(0, n):
        a, b = b, a + b

    return a


# @logit
def main():
    result = calculate_fibonacci(10)
    print(result)


if __name__ == "__main__":
    main()
