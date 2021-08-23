from MyRange import MyRange, my_range_generator
from Sentence import Sentence, sentence_generator


def main():
    nums = [1, 2, 3]

    # not nice way
    # i_nums = nums.__iter__()

    # nice way
    i_nums = iter(nums)

    # what is iterator doing?
    # sth like this:

    while True:
        try:
            item = next(i_nums)
            print(item)
        except StopIteration:
            break

    # print(next(i_nums))
    # print(next(i_nums))
    # print(next(i_nums))
    # print(i_nums)
    # print(dir(i_nums))
    # print(dir(nums))

    # proof that MyRange is iterable == has __iter__() method
    custom_nums = MyRange(1, 19)
    print('\nCustom nums: ')
    for num in custom_nums:
        print(num)

    # proof that MyRange is iterator == has __next__() method
    custom_nums_bis = MyRange(1, 19)
    print('\nCustom nums bis: ')
    print(next(custom_nums_bis))
    print(next(custom_nums_bis))
    print(next(custom_nums_bis))
    print(next(custom_nums_bis))
    print(next(custom_nums_bis))

    # Sentence tests
    sentence = Sentence('This is test sentence')
    print('\nSentence: ')
    for word in sentence:
        print(word)

    # Sentence tests
    sentence = Sentence('Test with two identical words Test')
    print('\nSentence: ')
    for word in sentence:
        print(word)

    # sentence_generator tests
    gen_sentence = sentence_generator('This is test sentence')
    print('\nsentence_generator: ')
    print(next(gen_sentence))
    print(next(gen_sentence))
    print(next(gen_sentence))
    print(next(gen_sentence))

    # sentence_generator tests
    gen_sentence_bis = sentence_generator('Test with two identical words Test')
    print('\nsentence_generator: ')
    print(next(gen_sentence_bis))
    print(next(gen_sentence_bis))
    print(next(gen_sentence_bis))
    print(next(gen_sentence_bis))
    print(next(gen_sentence_bis))
    print(next(gen_sentence_bis))


if __name__ == "__main__":
    main()
