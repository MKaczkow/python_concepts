import re


def main():
    emails = '''
    CoreyMSchafer@gmail.com
    corey.schafer@university.edu
    corey-321-schafer@my-work.net
    '''

    pattern = re.compile(r'\w+[-.]*\w+[-.]*\w+@\w+[-.]*\w+[-.]*\w+')

    matches = pattern.finditer(emails)

    for match in matches:
        # print(match)
        match_span = list(match.span())
        print(emails[match_span[0]:match_span[1]])


if __name__ == "__main__":
    main()
