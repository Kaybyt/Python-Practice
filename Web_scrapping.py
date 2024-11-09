import requests
from bs4 import BeautifulSoup


#url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
#webpage = requests.get(url)

#parsed_webpage = BeautifulSoup(webpage.content, "html.parser")

#tittle = parsed_webpage.find("span", class_ = "mw-page-title-main").get_text()
#print(tittle)

#paragraphs = parsed_webpage.find_all("p",)
#with open("wiki-python.txt", "a", encoding = "utf-8") as f:
    #for paragraph in paragraphs:
        #print("............................................................")
        #f.write(paragraph.txt)
        #print("Done writing to file")

#url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
#webpage = requests.get(url)

#parsed_webpage = BeautifulSoup(webpage.content, "html.parser")

#paragraphs = parsed_webpage.find_all("p")
#for paragraph in paragraphs:
#    print(paragraph.txt)
#    print('.....................................................')


url = "https://books.toscrape.com/"
webpage = requests.get(url)

print(webpage.content)

parsed_webpage = BeautifulSoup(webpage.content, "html.parser")

all_products = parsed_webpage.find_all("li", class_ = "col-xs-6 col-sm-4 col-md-3 col-lg-3")


for product in all_products:
    tittle = product.find("h3").find("a")["title"]
    link = product.find("h3").find("a")["href"]
    stock = product.find("p")
    print(tittle)