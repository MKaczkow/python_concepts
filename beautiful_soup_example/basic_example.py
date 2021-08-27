from bs4 import BeautifulSoup


def main():

    with open('sample.html') as f:
        soup = BeautifulSoup(f, 'lxml')

    # print(soup.prettify())

    for article in soup.find_all('div', class_='article'):

        headline = article.h2.a.text
        print(headline)

        summary = article.p.text
        print(summary)


if __name__ == "__main__":
    main()
