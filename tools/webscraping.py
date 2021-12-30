from typing import List

import bs4 as bs4
import requests


def get_html(site_url):
    print(f"Getting html from site : {site_url}.")
    r = requests.get(site_url)
    return r.text


def get_object(input_html, parser="html.parser"):
    print(f"Getting object from html with parser : {parser}")
    cur_soup = bs4.BeautifulSoup(input_html, parser)
    page_title = get_element_by_tag(cur_soup, "title")[0].getText()
    print(f"Converting the html page : {page_title}, to object.")
    return cur_soup


def get_html_object(site_url, parser="html.parser"):
    print(f"Getting html object from site : {site_url}.")
    html_page = get_html(site_url)
    cur_soup = get_object(html_page, parser)
    return cur_soup


'''
Syntax to pass to .select() Match Results
--------------------------  -------------
soup.select('div')          All elements with the <div> tag
soup.select('#some_id')     The HTML element containing the id attribute of some_id
soup.select('.notice')      All the HTML elements with the CSS class named notice
soup.select('div span')     Any elements named <span> that are within an element named <div>
soup.select('div > span')   Any elements named <span> that are directly within an element named <div>, with no other element in between

'''


def get_select_string(tag="", class_name="", id="", tags=[], classes=[], ids=[]):
    select_string = "" if tag == "" else f"{tag}"
    select_string += "" if class_name == "" else f".{class_name}"
    select_string += "" if id == "" else f"#{id}"

    for tag in tags:
        select_string += f"{tag} "
    for cn in classes:
        select_string += f".{cn}"
    for idn in ids:
        select_string += f"#{idn}"

    return select_string


def get_element_by_tag(my_page, tag):
    print(f"Getting the tag : {tag} from page.")
    select_string = get_select_string(tag=tag)
    return my_page.select(select_string)


def get_element_by_id(my_page, id):
    print(f"Getting the id : {id} from page.")
    select_string = get_select_string(id=id)
    return my_page.select(select_string)


def get_element_by_class(my_page, class_name):
    print(f"Getting the class : {class_name} from page.")
    select_string = get_select_string(class_name=class_name)
    return my_page.select(select_string)


def get_element_by_tag_and_class(my_page, tag, class_name):
    print(f"Getting the tag : {tag} and class : {class_name} from page.")
    select_string = get_select_string(tag=tag, class_name=class_name)
    return my_page.select(select_string)


def get_element_by_tag_and_id(my_page, tag, id):
    print(f"Getting the tag : {tag} and id : {id} from page.")
    select_string = get_select_string(tag=tag, id=id)
    return my_page.select(select_string)


def get_element_by_tag_and_class_and_id(my_page, tag, class_name, id):
    print(
        f"Getting the tag : {tag}, class : {class_name} and id : {id} from page.")
    select_string = get_select_string(tag, class_name, id)
    return my_page.select(select_string)


def get_element_by_tags_classes_and_ids(my_page, tags=[], classes=[], ids=[]):
    print(
        f"Getting the tags : {tags} and classes : {classes} and ids : {ids} from page.")
    # Convert tags list to string
    select_string = get_select_string(tags=tags, classes=classes, ids=ids)
    return my_page.select(select_string)


def get_element_by_multiple_tags(my_page, tags: List):
    print(f"Getting the tags : {tags} from page.")
    # Convert tags list to string
    select_string = get_select_string(tags=tags)
    return my_page.select(select_string)


def get_all_image_links(my_page):
    print("Getting all image links from page.")
    img_elements = my_page.select("img")
    return get_links(img_elements)


def get_links(src_elements):
    links = {}
    for img in src_elements:
        url = img.get("src")
        name = url.split("/")[-1]
        if url.startswith("http"):
            links[name] = url
        elif url.startswith("//"):
            links[name] = "https:" + url
        else:
            links[name] = "https://" + url
    return links


def get_text_from_html(my_page):
    print("Getting text from html.")
    return my_page.get_text()


def running():
    url = "https://en.wikipedia.org/wiki/Guido_van_Rossum"
    html = get_html(url)
    print("\n***********************\n")
    print("Printing the html page.")
    print(html)

    print("\n***********************\n")
    soup = get_html_object(html)
    print("Printing the pretty version of html.")
    print(soup.prettify())

    print("\n***********************\n")
    print("Printing all the elements with the <title> tag.")
    title_elements = get_element_by_tag(soup, "title")
    for element in title_elements:
        print(element.getText())

    print("\n***********************\n")
    print("Printing all the elements with the <img> tag.")
    img_elements = get_element_by_tag(soup, "img")
    for element in img_elements:
        print(element.get("src"))

    print("\n***********************\n")
    print("Printing all the images name and the respective links.")
    links_dic = get_all_image_links(soup)
    for key, value in links_dic.items():
        print(f"{key.ljust(60)} \t: {value}")

    print("\n***********************\n")
    print("Printing images with thumbimage class and the respective links.")
    image_elements = get_element_by_tag_and_class(soup, "img", "thumbimage")
    links_dic = get_links(image_elements)
    for key, value in links_dic.items():
        print(f"{key.ljust(60)} \t: {value}")

    print("\n***********************\n")
    print("Printing the text of the page.")
    print(get_text_from_html(soup))
