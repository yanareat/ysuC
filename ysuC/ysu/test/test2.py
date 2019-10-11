import bs4 as bs
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}
url = "https://book.douban.com"

res = requests.get(url="https://book.douban.com", headers=headers)
if res.status_code == 200:
    soup = bs.BeautifulSoup(res.content.decode("utf-8"), 'lxml')
    for el in soup.select(
            ".books-express .slide-list li,.popular-books li,.market-books .top,.market-books li,.ebook-area li"):
        # print(el)
        print("图书链接：%s" % el.select_one(".cover a").get("href"))
        img_src = ""
        img = el.select_one(".cover img")
        if img:
            img_src = img.get("src")
        else:
            style = el.select_one(".pic").get("style")
            img_src = re.search("url(.*?)", style)
        print("图书图片：%s" % img_src)

        title_name = ""
        title = el.select_one(".info .title a")
        if title:
            title_name = title.get_text().strip()
        else:
            title_name = el.select_one(".info .title").get_text().strip()
        print("书名：%s" % title_name)

        author = el.select_one(".author")
        print("作者：%s" % author.get_text().strip() if author else "")

        price = el.select_one(".price")
        print("价格：%s" % price.get_text().strip() if price else "")

        year = el.select_one(".year")
        print("出版时间：%s" % year.get_text().strip() if year else "")

        publisher = el.select_one(".publisher")
        print("出版商：%s" % publisher.get_text().strip() if publisher else "")

        abstract = el.select_one(".abstract")
        print("摘要：%s" % abstract.get_text().strip() if abstract else "")
        print("=" * 50)
