import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
page = requests.get(url)
#print(page)
soup = BeautifulSoup(page.content,"html.parser")
#print(soup)

items = soup.find_all("div",class_ = "thumbnail")
# print(items[0])
# print(items[0].find(class_="title").get_text())
# print(items[0].find(class_="description").get_text())
# print(items[0].find(class_="price").get_text())

title = [item.find(class_="title").get_text() for item in items]
description = [item.find(class_="description").get_text() for item in items]
price = [item.find(class_="price").get_text() for item in items]
# print(title)
# print(description)
# print(price)

data = pd.DataFrame(
    {
        "title" : title,
        "description" : description,
        "price" : price
    }
)
print(data)
data.to_csv("data.csv")



