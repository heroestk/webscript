import subscribe_novels
import unittest


class TestSubscribeNovels(unittest.TestCase):
    def test_parse_chapter_string(self):
        test_list = {'第两千四百九十八章 有本事，自己来拿' : [2498, '有本事，自己来拿']}
        for k, v in test_list.items():
            self.assertEqual(subscribe_novels.parse_subscribe_string(k), test_list[k])

if __name__ == "__main__":
    unittest.main()