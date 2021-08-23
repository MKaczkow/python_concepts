
class Sentence:

    def __init__(self, sentence_string: str):
        self.sentence_string = sentence_string

    def __iter__(self):
        return self

    def __next__(self):
        if not self.sentence_string:
            raise StopIteration

        first_word, self.sentence_string = self.sentence_string.split(maxsplit=1)[0],\
                                           ' '.join(self.sentence_string.split(maxsplit=1)[1:])

        return first_word


def sentence_generator(sentence_string: str):
    # num_of_words = len(sentence_string.split())
    # for num in range(num_of_words):
    #     first_word, sentence_string = sentence_string.split(maxsplit=1)[0], \
    #                                   ' '.join(sentence_string.split(maxsplit=1)[1:])
    #
    #     yield first_word

    for word in sentence_string.split():
        yield word
