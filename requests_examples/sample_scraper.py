from requests_html import HTML


def main():
    with open("sample.html") as f:
        source = f.read()
        html = HTML(html=source)

    match = html.find("title", first=True)
    # print(match.text)

    match = html.find("#footer", first=True)
    # print(match.text)

    articles = html.find("div.article")
    for article in articles:
        headline = article.find("h2", first=True).text
        summary = article.find("p", first=True).text
        print(article.text)
        print(headline)
        print(summary)
        print()


if __name__ == "__main__":
    main()
