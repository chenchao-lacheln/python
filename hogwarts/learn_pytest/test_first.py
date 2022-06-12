# 文件名  test_开头
def inc(x):
	return x + 1

def test_answer():
	assert inc(4) == 5

class TestDemo:  #类名 驼峰
	def test_demo1(self): # 方法名 test_开头
		pass

	def test_demo2(self): # 方法名 test_开头
		pass

	def test_demo3(self):
		pass

	def test_demo4(self):
		pass