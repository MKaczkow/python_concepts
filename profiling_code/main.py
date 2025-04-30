import cProfile
import pstats
import sys
import time


def add(x, y):
    """Add two numbers, but weirdly."""
    result = 0
    result += x
    result += y
    return result


def factorial(n):
    """Calculate the factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def do_stuff():
    """Tak zwane 'robienie rzeczy'."""
    result = []
    for x in range(1_000_000):
        result.append(x * 2)
    return result


# profile specific function using scalene
# don't import profile
# @profile
def waste_time():
    """Wasting time."""
    time.sleep(10)
    print("Wasted 10 seconds!")
    return None


if __name__ == "__main__":

    sys.set_int_max_str_digits(
        1_000_000_000
    )  # Increase the limit for integer string conversion
    with cProfile.Profile() as profile:
        print(add(1, 1_000_000))
        print(factorial(4242))
        print(do_stuff())
        waste_time()
        print(do_stuff())
        print(waste_time())
        print(do_stuff())
        print(waste_time())

    results = pstats.Stats(profile)
    results.sort_stats(pstats.SortKey.TIME)
    results.print_stats(10)
    results.dump_stats("results.prof")
