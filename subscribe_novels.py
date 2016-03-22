# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib.request as ur

def get_url_contents():
    zqwk_url = 'http://m.fenghuaju.com/1_1635/'
    #zqwk_url = 'http://www.sodu.cc/newmulu_394_2.html'
    #zqwk_url = 'http://read.qidian.com/BookReader/t8z_AX1MSu41.aspx'
    html_source = ur.urlopen(zqwk_url).read()
    soup = BeautifulSoup(html_source, "html.parser")
    print(soup)

if __name__ == "__main__":
    get_url_contents()