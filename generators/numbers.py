def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i * i)
    return result


def generate_square_numbers(nums):
    for i in nums:
        yield (i * i)


def main():
    my_nums = square_numbers([1, 2, 3, 4, 5])
    print(f"Using function:\n{my_nums}")

    gen_nums = generate_square_numbers([1, 2, 3, 4, 5])
    print(f"Using generator one-by-one:")
    # print next(gen_nums)
    # print next(gen_nums)
    # print next(gen_nums)
    # print next(gen_nums)
    # print next(gen_nums)

    gen_nums_lc = (x**2 for x in [1, 2, 3, 4, 5])
    print(f"Using generator and list comprehension:")
    print(gen_nums_lc)
    for num in gen_nums_lc:
        print(num)


if __name__ == "__main__":
    main()
