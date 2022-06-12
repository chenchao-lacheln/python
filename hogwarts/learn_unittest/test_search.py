
# 32min
# 被测方法
import unittest


class Search:
    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()

if __name__ == '__main__':
    unittest.main()

