from bs4 import BeautifulSoup
import requests
from os import path

# if the file wasn't created before (probably at the first start of the game) this function will connect to given site
# and scrape words to create words database, it will make it usable by taking off all unnecessary html syntax

if not path.exists('words.txt'):
    page_link = 'https://www.ef.com/ca/english-resources/english-vocabulary/top-1000-words/'

    page_response = requests.get(page_link, timeout=10)
    page_content = BeautifulSoup(page_response.text, "html.parser")

    words = page_content.find("div", class_="field-item even")

    first_words = words.contents[2]

    words_file = open("words.txt", "w")
    words_file.write(str(first_words))

    with open("words.txt", "r+") as f:
        f.readline()
        lines = f.readlines()
    with open("words.txt", "w") as f:
        for line in lines:
            if line != "\n":
                f.write(line.replace("<br/>\n", "\n").replace("</p>", ""))
    words_file.close()
