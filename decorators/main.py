import os
from time import time


def checkdir(func):
	def checked_function(*args, **kwargs):
		print(f'Function {func.__name__!r} works in {os.getcwd()}')
		print(f'Other things in this dir: {os.listdir()}')
		result = func(*args, **kwargs)
		return result
	return checked_function


def timeit(func):
	def timed_function(*args, **kwargs):
		t1 = time()
		result = func(*args, **kwargs)
		t2 = time()
		print(f'Function {func.__name__!r} executed in {(t2 - t1):.4f}s')
		return result
	return timed_function


def verbose(func):
	def explained_function(*args, **kwargs):
		print(f'\nRunning function {func.__name__!r} ...')
		result = func(*args, **kwargs)
		print(f'Function {func.__name__!r} executed')
		return result
	return explained_function


@verbose
# @timeit
# @checkdir
def calculate_fibonacci(n):
	a, b = 0, 1

	for i in range(0, n):
		print(a)
		a, b = b, a + b


def main():
	calculate_fibonacci(10)


if __name__ == "__main__":
	main()
