import os
# # os.mkdir("testdir")  #创建文件夹
# print(os.listdir("./")) #遍历当前目录
# # os.removedirs("testdir") # 删除文件家
# print(os.getcwd()) #获取当前的路径的绝对路径

# b/test.txt 创建文件夹b，并在该文件夹下面创建文件test.txt这个文件
# 判断当前目录下有没有这个文件
print(os.path.exists("b"))
if not os.path.exists("b"):
    os.mkdir("b")
if not os.path.exists("b/test.txt"):
    f = open("b/text.txt","w")
    f.write("hello , os usering !")
    f.close()