import bs4
import requests

base_url = "https://www.goodreads.com"
quotes_url = base_url + "/quotes?page={}"
author_url = "https://www.goodreads.com{}"
tag_url = "https://www.goodreads.com{}"


class Quote:

    def __init__(self, author=None, text="", tags=None):
        if tags is None:
            tags = []
        self.author = author
        self.text = text
        self.tags = tags

    def __str__(self) -> str:
        return f"{self.text} \t by \n\t{self.author}.\n\t{self.tags}"


class Tag:

    def __init__(self, text: str, link=""):
        self.text = text.replace("\n", "")
        self.link = link

    def __str__(self) -> str:
        return f"{self.text}"

    def __repr__(self):
        return self.__str__()


class Author:

    def __init__(self, name: str, link=""):
        self.name = name.replace("\n", "")
        self.link = link

    def __str__(self) -> str:
        return f"{self.name}"


def get_html_object(site_url, parser="html.parser"):
    print(f"Getting html from site : {site_url}.")
    response = requests.get(site_url)
    print(f"Getting html object from site : {site_url}.")
    cur_soup = bs4.BeautifulSoup(response.text, parser)
    page_title = cur_soup.select("title")[0].getText()
    print(f"Converting the html page : {page_title}, to object.")
    return cur_soup


def get_quote(quote_html):
    try:
        author_html = quote_html.select(".leftAlignedImage")
        author = None
        # Some quotes not have any author. They will only have the text and tags.
        if len(author_html) > 0:
            author_name = author_html[0].select("img")[0]["alt"]
            author_link = author_url.format(quote_html.find('a')["href"])
            author = Author(author_name, author_url.format(author_link))

        array = quote_html.select('.quoteText')[0].getText().split("―")

        # Grab the author name from the quote
        if len(array) > 1:
            author = Author(array[1])

        htmltags = quote_html.select(".quoteFooter .greyText.smallText.left a")
        tags = [Tag(tag.getText(), tag_url.format(tag['href'])) for tag in htmltags]
        return Quote(author, array[0], tags)
    except Exception as ex:
        print(f"Error while converting the quote.")
        print(f"Error Details : {ex}")
        print(f"Quote Details : \n {quote_html}")


def get_quotes(page_url):
    html_object = get_html_object(page_url)
    quotes_html = html_object.select(".quote")
    quotes = []
    for quote_html in quotes_html:
        quotes.append(get_quote(quote_html))
    return quotes


if __name__ == "__main__":
    print(f"Scraping {base_url} for Quotes.")
    quotes = get_quotes(quotes_url.format("1"))
    for quote in quotes:
        print(quote)
