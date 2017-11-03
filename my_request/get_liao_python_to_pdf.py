# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import pdfkit


def get_url_list():
    """
    获取所有URL目录列表
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("div"):
        url = "http://www.liaoxuefeng.com" + li.a.get('href')
        urls.append(url)
    return urls

# print get_url_list()


def save_pdf(htmls):
    """
    把所有html文件转换成pdf文件
    """
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_url(htmls, 'liao.pdf', options=options)

save_pdf(get_url_list()[:10])
