import requests
from bs4 import BeautifulSoup
import lxml

url = "https://www.bestchange.ru/ethereum-to-tinkoff.html"

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}

request = requests.get(url, headers = headers)
src = request.text

with open("index.html", "w") as file:
    file.write(src)

soup = BeautifulSoup(src, "lxml")

all_exchanges = soup.find_all("div", class_ = "pa labpad2")
for item in all_exchanges:
    name = item.find(class_ = "ca")
    info = name.find(class_ = "fm1")
    print(name.text)
    print(info.text)
    #print(item.find(class_ = "fm1").text)
