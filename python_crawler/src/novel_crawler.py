import requests
from bs4 import BeautifulSoup


def get_html(url,headers):
    response = requests.get(url,headers=headers)
    return response.text


def get_novel(html):
    soup = BeautifulSoup(html, 'lxml')
    passages = soup.find_all(id = 'content')
    for passage in passages:
        with open("../data/仙逆.txt", "a", encoding="utf-8") as file:
            file.write('\n'.join([child.string for child in passage.children if child.string]) + "\n")
            file.write("\n---------------------------------------------------\n\n")
    print("爬取成功!")

if __name__ == '__main__':
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"
    }
    for number in range(21200, 23238):
        url = f"https://www.hetushu.com/book/36/{number}.html"
        html = get_html(url, headers)
        get_novel(html)