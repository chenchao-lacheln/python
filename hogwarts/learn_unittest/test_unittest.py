import unittest

class TestStringMethods(unittest.TestCase): #继承unittest.TestCase

    #setUp && tearDown 是在每条测试用例前后调用
    def setUp(self) -> None:
        print("setUp")

    def tearDown(self) -> None:
        print("tearDown")

    # setUpClass && tearDownClass 是在整个类的前后调用
    @classmethod
    def setUpClass(cls) -> None:
        print("set Up Class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tear Down Class")

    def test_add(self):
        print("hhhhh  111")

    def test_upper(self):
        print("test_upper 222")
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        print("test_isupper 333")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split 444")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()