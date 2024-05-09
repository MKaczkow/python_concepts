import itertools

# counter
print("\ncounter: ")
counter = itertools.count(start=19, step=-3)
print(next(counter))
print(next(counter))


# zip_longest
print("\nzip_longest: ")
data = [100, 200, 300, 400]
daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

# cycle
print("\ncycle: ")
cycle = itertools.cycle([1, 2, 3])
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print()

cycle_switch = itertools.cycle(("ON", "OFF"))
print(next(cycle_switch))
print(next(cycle_switch))
print(next(cycle_switch))
print(next(cycle_switch))


# repeat
print("\nrepeat: ")
repeater = itertools.repeat(19, times=3)
print(next(repeater))
print(next(repeater))
print(next(repeater))
print()
# print(next(repeater))

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))


# starmap
squares_smap = itertools.starmap(pow, [(0, 2), (1, 2), (2, 2)])


# combinations and permutations
letters = ["a", "b", "c", "d"]
numbers = [0, 1, 2, 3]
names = ["Corey", "Nicole"]

print("\ncombinations: ")
result = itertools.combinations(letters, 2)
for item in result:
    print(item)

print("\npermutations: ")
result = itertools.permutations(letters, 2)
for item in result:
    print(item)


# product
print("\nproduct: ")
result = itertools.product(numbers, repeat=4)
for item in result:
    print(item)


# chain
print("\nchain: ")
combined = itertools.chain(letters, numbers, names)
for item in combined:
    print(item)


# islice
print("\nislice: ")
result = itertools.islice(range(100), 1, 5, 2)
for item in result:
    print(item)

# compress
print("\ncompress: ")
selectors = [True, True, False, True]
result = itertools.compress(letters, selectors)
for item in result:
    print(item)
