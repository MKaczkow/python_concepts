def greeting(name):
    return "Helo " + name


def static_greeting(name: str) -> str:
    return "Helo " + name


# def main():
# should fail but not get caught by mypy
# because it doesn't check dynamicly typed functions
# greeting(123)
# greeting(b"world")
static_greeting("123")  # OK
# static_greeting(123)   # NOK
# static_greeting(b"world")   # NOK

# if __name__ == "__main__":
#     main()
