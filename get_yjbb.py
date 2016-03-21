# -*- coding: utf-8 -*-

import csv
import re
import sys
import urllib.request as ur
from bs4 import BeautifulSoup

"""
从东方财富获得单只股票的历年业绩报表详细
defjson里有所需要的全部数据
采用BeautifulSoup
code:6位数字

关于其他解题思路：
正则表达式略显麻烦
不能使用xml的解析包，因为html有时候并不是一个严格意义上的xml，例如script
HTMLParser应该也可以,不过一开始以为直接删掉不需要的div就可以了
"""
def get_yjbb_bs(code):
    # url -> str
    url = 'http://data.eastmoney.com/bbsj/stock{0}/yjbb.html'.format(code)
    html_source = ur.urlopen(url).read()
    html_str = html_source.decode('gbk')
    soup = BeautifulSoup(html_str, "html.parser")

    header = """
    股票代码,股票名称,每股收益,每股收益（扣除）,营业收入,营业收入同比增长,营业收入季度环比增长,
    净利润,净利润同比增长,净利润环比增长,每股净资产,净资产收益率,每股经营现金流,销售毛利率,
    利润分配,股息率,公告日期,截止日期""".split(',')
    json_str = soup.find(text= re.compile('defjson'))
    m = re.search(r"defjson: (\{.*\})", json_str)
    #print(m.group(1))
    f = open("c:/1.csv", newline='', mode='w')
    writer = csv.writer(f, dialect='excel')
    writer.writerow(header)
    for iter in re.finditer(r'"([^"]*)"', m.group(1)):
        if iter:
            one_year_str = iter.group(1)
            detail_list = one_year_str.split(',')
            writer.writerow(detail_list)
    f.close()

if __name__ == '__main__':
    if (len(sys) < 2):
        print('Please input stock code!')
    else:
        get_yjbb_bs('300072')
