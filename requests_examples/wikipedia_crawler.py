from requests_html import HTML, HTMLSession

# does wikipedia has public API??


def main():
    session = HTMLSession()
    r = session.get("https://pl.wikipedia.org/")

    for link in r.html.absolute_links:
        print(link)


if __name__ == "__main__":
    main()
