# 输出直角三角形
# *
# **
# ***
# ****
# *****
# for i in range(1,6):
#     print("*"*i)
# for i in range(1,6): # 控制行数
#     for j in range(1,i+1):
#         print("*",end="") #end=""不换行输出
#     print("") #print语句会换行

#     *
#    **
#   ***
#  ****
# *****

# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print("*",end="")
#     print("")

# 输出等边三角形（三个边均为5个*）
# for i in range(1,6):
#     for j in range(1,6-i):
#         print(" ",end="")
#     for k in range(1,i+1):
#         print(" *",end="")
#     print("")

#输出99乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("{}*{}={} ".format(i,j,i*j),end="")
#     print("")

# 冒泡排序 相邻数依次比较
# list = [1,3,5,7,9,0,3]
#
# for i in range(0,len(list)-1): #比较几次
#     for j in range(0,len(list)-1):
#         if list[j] > list[j+1]:
#             list[j],list[j+1]=list[j+1],list[j]
#     # print(list) # 打印过程
# print(list)

# 分别求出0-100之间的所有偶数和和所有奇数和
# for i in range(0,101,2):
#     print(i)

# 自动贩卖机,只接受1元，5元，10元的纸币或者硬币
# 可以1元，5元，10元，最多不超过10元
# 饮料只有橙汁，椰汁，矿泉水，早餐奶
# 售价分别是3.5，4，2，4.5
# 写一个函数用来表示贩卖机的功能，
# 用户投钱或者选择饮料，通过判断之后，给用户吐出饮料和找钱

#选择饮料：字典
# 投钱：1 5 10 判断金额的面值
# 判断：钱不够  钱多了 钱刚好的情况

# 用户选择饮料

def auto_buy():
    drinks = {"1":3.5,"2":4,"3":2,"4":4.5}
    total = 0 #存储购买饮料的总金额
    while True:
        choose = input("请选择你要购买的饮料，1：橙汁 2：椰汁 3：矿泉水 4：早餐奶 q：退出")
        if choose in drinks.keys():
            total +=drinks[choose]
        elif choose == "q":
            print("退出选择饮料")
            break
        else:
            print("你输入的选项不存在")

    # 用户投币
    toubi = 0
    while True:
        money = int(input("请投币：只能投1 5 10元的币，按q退出投币"))
        if money ==1 or money ==5 or money ==10:
            toubi += int(money)
            if toubi > total:
                print("您刚刚购买了{0}元饮料，已经支付了{1}元,还需要找你{2}元".format(total,toubi,toubi - total))
                break
            elif toubi < total:
                print("您刚刚购买了{0}元饮料，已经支付了{1}元,还需要投币{2}元,请继续投币！".format(total,toubi, total - toubi))
            else:
                print("您刚刚购买了{0}元饮料，已经支付了{1}元,您已支付完毕！".format(total, toubi))
                break
        elif money == "q":
            print("退出投币")
            break
        else:
            print("你输入的选项不存在")

auto_buy()