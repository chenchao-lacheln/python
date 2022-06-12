class Airplan:
    name = ""
    color = ""

    def set_color(self,color):
        self.color = color
        print(f"飞机的颜色是：{self.color}")

    def set_name(self,name):
        self.name = name
        print(f"飞机的名字是：{self.name}")

class CivilAirplan(Airplan):
    def load_persion(self,num):
        print(f"民用飞机的载人数量为：{num}")

    def set_name(self,name): #子类的方法会覆盖父类的方法
        print(f"民用机的名字为")

civil1 = CivilAirplan()
civil1.set_name("超哥")
civil1.load_persion("89")
# air1 = Airplan()
# air1.set_name("第一架飞机")
# air1.set_color("蓝色")