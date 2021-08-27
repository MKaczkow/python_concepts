import requests as req


def main():

    # basic GET request and response
    r = req.get('https://xkcd.com/353/')

    # print(r.text)
    print(r.url)
    # print(r.encoding)
    # print(r.content)
    # print(r.json())

    print(r.raw)
    print(r.raw.read(10))

    # basic GET request and response
    r = req.get('https://xkcd.com/327/')

    # print(r.text)
    print(r.url)
    # print(r.encoding)
    # print(r.content)
    # print(r.json())

    print(r.raw)
    print(r.raw.read(10))


if "__name__" == "__main__":
    main()
