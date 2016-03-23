# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import chinese_to_number
import re
import urllib.request as ur


# return [number, name] if good.
def parse_subscribe_string(str):
    result = str.split(' ')
    chi = result[0][1: -1]
    result[0] = chinese_to_number.cn2dig(chi)
    return result


def get_url_contents():
    zqwk_url = 'http://m.fenghuaju.com/1_1635/'
    # zqwk_url = 'http://www.sodu.cc/newmulu_394_2.html'
    # zqwk_url = 'http://read.qidian.com/BookReader/t8z_AX1MSu41.aspx'
    html_source = ur.urlopen(zqwk_url).read()
    soup = BeautifulSoup(html_source, "html.parser")
    ul = soup.find(name="div", class_="chapter_list")
    for ele in ul.find_all('li'):
        print("One line:", ele.text.strip())

if __name__ == "__main__":
    get_url_contents()