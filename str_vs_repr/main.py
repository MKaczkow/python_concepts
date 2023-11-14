import datetime
import pytz


a = [1, 2, 3, 4]
b = "test_string"
c = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
d = str(c)

# the goal of __repr__ is to be unambigous
print(repr(a))
print(repr(b))
print(f"repr(c) {c}")
print(f"repr(c) {d}")

# the goal of __str__ is to be readable
print(str(a))
print(str(b))
print(f"str(c) {c}")
print(f"str(c) {d}")

# altough, right now, they are pretty much the same...
