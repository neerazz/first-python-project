from decorater import include_seperator_3, print_stars
from tools.webscraping import get_element_by_class, get_element_by_tags_classes_and_ids
from tools.webscraping import get_html_object

url = "https://books.toscrape.com/"


class Book:

    def __init__(self, name, price, book_url, stars, description, upc, avail) -> None:
        self.name = name
        self.price = price
        self.book_url = book_url
        self.upc = upc
        self.stars = stars
        self.description = description
        self.avail = avail

    def __str__(self):
        return f"{self.name} - {self.price} - {self.stars}. \n {self.description} \n\n {self.upc} \n {self.avail}"


@include_seperator_3
def get_number_of_pages(book_home_page):
    print("Get number of pages.")
    # Get number of pages
    page_element = get_element_by_tags_classes_and_ids(book_home_page, classes=["current"])
    cur_page, total_pages = 0, 0
    if page_element and len(page_element) > 0:
        for ele in page_element:
            ele_txt = ele.getText()
            print(f"Element Text : {ele_txt}")
            txt_split = ele_txt.split()
            cur_page, total_pages = int(txt_split[1]), int(txt_split[3])
    return cur_page, total_pages


@include_seperator_3
def get_books(product_ele) -> Book:
    book_suffix = "/catalogue/{}"
    book_url = url + book_suffix.format(product_ele.find('a')["href"])
    book_soup = get_html_object(book_url)
    title = book_soup.find("title").getText().strip().split("|")[0]
    price = book_soup.select(".price_color")[0].getText().replace("Â", "")
    stars = book_soup.select(".star-rating")[0]["class"][1]
    description = book_soup.select(".product_page p")[3].getText()
    table = book_soup.select(".table.table-striped")[0]
    upc = ""
    avail = ""
    for row in table.findAll("tr"):
        headval = row.find("th").getText()
        if headval == "UPC":
            upc = row.find("td").getText()
        elif headval == "Availability":
            avail = row.find("td").getText()
    return Book(title, price, book_url, stars, description, upc, avail)


# Goal 1: Get title all the books in the site.

@include_seperator_3
def get_all_books():
    print("Goal 1: Get title all the books with a 2 star rating.")
    # Get book home page
    book_home_page = get_html_object(url)
    # Get number of pages
    cur_page, total_pages = get_number_of_pages(book_home_page)
    print(f"Current Page: {cur_page}, Total pages : {total_pages}")
    page_suffix = "/catalogue/page-{}.html"
    books = []
    for page in range(1, total_pages + 1):
        page_url = url + page_suffix.format(page)
        page = get_html_object(page_url)
        products_ele = get_element_by_class(page, "product_pod")
        for product_ele in products_ele:
            book = get_books(product_ele)
            print(f"Extracted book : {book}")
            books.append(book)
    return books


@include_seperator_3
def get_title_of_books_with_2_star_rating():
    None


books = get_all_books()
print(f"Total number of books : {len(books)}")
print("Printing individual Books : \n")
for book in books:
    print_stars()
    print(book)
# print(get_title_of_books_with_2_star_rating())
