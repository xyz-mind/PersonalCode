from bs4 import BeautifulSoup
import re

with open("../data/baidu.html","r",encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html,"lxml")

sentences = soup.find_all(re.compile("a"))
for sentence in sentences:
    print(sentence.string)
