# 模块级别,只被调用1次
def setup_module():
    print("资源准备：setup module")

def teardown_module():
    print("资源准备：teardown module")

def test_case1():
    print("case1")

def test_case2():
    print("case2")

def test_case3():
    print("case3")

def test_case4():
    print("case4")

def setup_function():
    print("资源准备: setup function")

def teardown_function():
    print("资源销毁:teardown function")


class TestDemo:

# 执行类 前后分别执行setup_calss teardown_calss
    def setup_class(self):
        print("Testchmod u+x *.shDemo setup class")

    def teardown_class(self):
        print("TestDemo teardowm class")

    #每个类里面的方法分别执行 setup,teardown
    def setup(self):
        print("test setup")

    def teardown(self):
        print("test teardown")

    def test_demo1(self):
        print("test demo1")

    def test_demo2(self):
        print("test demo2")

    def test_demo3(self):
        print("test demo3")
