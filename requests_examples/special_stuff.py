from requests_html import HTML, HTMLSession


def main():

    session = HTMLSession()
    r = session.get('https://coreyms.com/')

    for link in r.html.absolute_links:
        print(link)


if __name__ == "__main__":
    main()
