# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import chinese_to_number
import re
import urllib.request as ur


def parse_subscribe_string(str):
    """return [number, name] if str is valid"""
    result = str.split(' ')
    chi = result[0][1: -1]
    result[0] = chinese_to_number.cn2dig(chi)
    return result


def get_url_contents():
    zqwk_url = 'http://m.fenghuaju.com/1_1635/'
    # zqwk_url = 'http://www.sodu.cc/newmulu_394_2.html'
    # zqwk_url = 'http://read.qidian.com/BookReader/t8z_AX1MSu41.aspx'
    return ur.urlopen(zqwk_url).read()


def get_deliver_list(content, last_delivered):
    """Return chapter list we want to deliver : [number, title, href]
    """
    deliver_list = []
    soup = BeautifulSoup(content, "html.parser")
    site_url = soup.head.base['href']
    print(site_url)
    ul = soup.find(name="div", class_="chapter_list")

    for ele in ul.find_all('li'):
        if '更' == ele.text.strip()[0]:
            continue
        num_and_text = parse_subscribe_string(ele.text.strip())
        if int(num_and_text[0]) > last_delivered:
            if ele.a['href'][0] == '/':
                href = site_url + ele.a['href']
            else:
                href = site_url + '/' + ele.a['href']
            one_chapter = [num_and_text[0], num_and_text[1], href]
            deliver_list.append(one_chapter)

    return  deliver_list

if __name__ == "__main__":
    print(get_deliver_list(get_url_contents(), 2496))