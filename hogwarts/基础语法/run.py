import unittest

if __name__ == '__main__':
    test_dir = './learn_unittest'
    discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
    unittest.TextTestRunner(verbosity=2).run(discover)


