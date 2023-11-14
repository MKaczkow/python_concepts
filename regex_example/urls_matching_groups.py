import re


def main():
    urls = """
    https://www.google.com
    http://coreyms.com
    https://youtube.com
    https://www.nasa.gov
    """

    pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")

    subbed_urls = pattern.sub(r"\2\3", urls)
    print(subbed_urls)

    matches = pattern.finditer(urls)

    for match in matches:
        print(f"{match.group(2)}\t\t{match.group(3)}")
        # match_span = list(match.span())
        # print(urls[match_span[0]:match_span[1]])


if __name__ == "__main__":
    main()
