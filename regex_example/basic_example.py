import re


def main():
    text_to_search = """
    abcdefghijklmnopqurtuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    Ha HaHa
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    coreyms.com
    321-555-4321
    123.555.1234
    123*555*2345
    800-555-4567
    900-555-6787
    901-555-6312
    400-555-0866
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    """

    # matching phone numbers
    # pattern = re.compile(r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d')

    # matching phone numbers
    # pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{3}')

    # matching 800 and 900 phone numbers
    pattern = re.compile(r"(?!(8|9)00)\d{3}[.-]\d{3}[.-]\d{4}")

    # matching phone numbers that aren't 800 or 900
    # pattern = re.compile(r'[^89][^0][^0][.-]\d\d\d[.-]\d\d\d\d')

    # matching Mr, Ms, Mrs, etc.
    # pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')

    matches = pattern.finditer(text_to_search)

    for match in matches:
        # print(match)
        match_span = list(match.span())
        print(text_to_search[match_span[0] : match_span[1]])


if __name__ == "__main__":
    main()
