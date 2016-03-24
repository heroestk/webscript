from subscribe_novels import *
import unittest

test_content = """
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<base href="http://m.fenghuaju.com"/>
</head>
<body>
<!--noads-->
<div class="qd_bookinfo">
<div class="book_title">
<a class="return" href="http://m.fenghuaju.com/"><span>返回</span></a>
<h1>
                都市之最强纨绔</h1>
 </div>
<div class="book_info_box">
<div class="chapter_list">
<ul id="chapterList">
<li onclick="location.href=&#39;1_1635/2500.html&#39;;">
<a href="1_1635/2500.html">
                            第两千四百九十六章 混乱的局势</a></li>
<li onclick="location.href=&#39;1_1635/2499.html&#39;;">
<a href="1_1635/2499.html">
                            第两千四百九十五章 杀心！被困！</a></li>
<li onclick="location.href=&#39;1_1635/2498.html&#39;;">
<a href="1_1635/2498.html">
                            第两千四百九十四章 风云动！风波起！</a></li>
<li onclick="location.href=&#39;1_1635/2497.html&#39;;">
<a href="1_1635/2497.html">
                            第两千四百九十三章 四大老祖</a></li>
<li onclick="location.href=&#39;1_1635/2496.html&#39;;">
<a href="1_1635/2496.html">
                            第两千四百九十二章 幻境相遇</a></li>
<li onclick="location.href=&#39;1_1635/2495.html&#39;;">
<a href="1_1635/2495.html">
                            第两千四百九十一章 异动的天道</a></li>
<li onclick="location.href=&#39;1_1635/2494.html&#39;;">
<a href="1_1635/2494.html">
                            第两千四百九十章 为凝聚肉身做准备</a></li>
<li onclick="location.href=&#39;1_1635/2493.html&#39;;">
<a href="1_1635/2493.html">
                            第两千四百八十九章 认输！获得名额！</a></li>
<li onclick="location.href=&#39;1_1635/2492.html&#39;;">
<a href="1_1635/2492.html">
                            第两千四百八十八章 完胜！爆裂而死！</a></li>
<li onclick="location.href=&#39;1_1635/2491.html&#39;;">
<a href="1_1635/2491.html">
                            第两千四百八十七章 支脉比斗开始</a></li>
<li onclick="location.href=&#39;1_1635/1/&#39;;" style="text-align: center;">
<a href="1_1635/1/">更多目录&gt;&gt;</a></li>
</ul>
</div>
</div>
</div>
</body></html>
"""


class TestSubscribeNovels(unittest.TestCase):
    def test_parse_chapter_string(self):
        test_list = {'第两千四百九十八章 有本事，自己来拿' : [2498, '有本事，自己来拿']}
        for k, v in test_list.items():
            self.assertEqual(parse_subscribe_string(k), test_list[k])

    def test_get_deliver_list(self):
        deliver_list = get_deliver_list(test_content, 2494)
        self.assertEqual(len(deliver_list), 2)
        first = deliver_list[0]
        self.assertEqual(first[0], 2496)
        self.assertEqual(first[1], '混乱的局势')
        self.assertEqual(first[2], 'http://m.fenghuaju.com/1_1635/2500.html')

if __name__ == "__main__":
    unittest.main()