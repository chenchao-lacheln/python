import os
# # 拓展题
# # 给定一个路径，请打印出所有的路径，（直至这个路径下没有目录为止）
# # 思路：递归函数
#
# # 给定一个路径，请打印所有的路径（直至这个路径下没有目录为止）
# # 思路：递归函数
# def get_full_path(current_working_directory):
#     for path in os.listdir(current_working_directory):
#         if os.path.isdir(os.path.join(current_working_directory, path)):
#             new_current_working_directory = os.path.join(current_working_directory, path)
#             print("{}还需要做进一步处理".format(path))
#             get_full_path(new_current_working_directory)
#         else:
#             print("这个是已经穷尽的路径：", os.path.join(current_working_directory, path))
#
#
# get_full_path(os.getcwd())

# 第一种语法：try except
# 第一种语法：try except finally   # finally 就是无论之前有什么错误，都会执行finally后面的代码
# 第一种语法：try except else   # 只要有错误，else里面的代码都不运行
try: #警察
    os.mkdir("超哥") # FileExistsError 嫌疑人

# 三种抓去错误的方法
# 1.处理某个错误
except FileExistsError as error: # expect 警力出动
# 2.处理某种错误
# except os:
# 3.有错就抓
# except Exception:
    print(error)
    file = open("error.txt","a+")
    file.write(str(error))
    file.close()
else:
    print("我最牛逼！")