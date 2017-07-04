#!/usr/bin/env python3

"""
download books from https://h.sicp.org.uk/virtual~plaza/books/
"""

from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings()

URL_PREFIX = "https://h.sicp.org.uk"
BOOK_URL = URL_PREFIX + "/virtual~plaza/books/"

html = requests.get(BOOK_URL, verify=False).text
soup = BeautifulSoup(html, "html.parser")

for link in soup.find_all("a"):
    book_name = link.text

    print("found " + book_name)

    if ".pdf" not in book_name:
        print("not a book, skipping " + book_name)
        continue

    book_url = URL_PREFIX + link.get("href")

    print("downloading " + book_url)

    r = requests.get(book_url, stream=True, verify=False)
    with open(book_name, "wb") as f:
        f.write(r.content)
