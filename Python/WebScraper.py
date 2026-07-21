import requests
from bs4 import BeautifulSoup
import csv

url = "http://books.toscrape.com"
odziv = requests.get(url)

print(odziv.status_code)

juha = BeautifulSoup(odziv.text, "html.parser")
knjige = juha.find_all("article", class_="product_pod")


print(len(knjige))


for knjiga in knjige:
    naslov = knjiga.h3.a["title"]
    print(naslov)

open("knjige.csv", "w", )