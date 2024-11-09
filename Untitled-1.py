import requests
from bs4 import BeautifulSoup

url = "https://careerfoundry.com/en/blog/data-analytics/web-scraping-guide/"
webpage = requests.get(url)
parsed_webpage = BeautifulSoup(webpage.content, "html.parser")
all_outlines = parsed_webpage.find_all("header", class_ = "entry-title ds-typography__h1 ds-color__static-content-primary")
for outline in all_outlines:
    head = outline.find("h1")
    print(head)
