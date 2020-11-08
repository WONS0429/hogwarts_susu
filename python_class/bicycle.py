# -*-coding: utf-8 -*-
# @Time    :2020-11-5 上午 10:49
# @Author  :susu
# @File    :bicycle.py

# 自行车类
class Bicycle:

    # 骑行方法
    def run(self, km):
        print(f"一共用脚骑了{km}公里，累死了")

# 电动自行车类
# 继承：把父类名称放在类名后的小括号中
class EBicycle(Bicycle):
    # 属性需要传参定义，可以直接放到构造函数中
    def __init__(self, valume):
        self.valume = valume  # valume电量

    # 充电方法
    def fill_charge(self, vol):
        # 充电后的电量 = 本身的电量 + 充电电量
        self.valume = self.valume + vol
        print(f"充了{vol}度电，现在的电量是{self.valume}度")

    def run(self, km):

        # 1.获取目前电量所能电动骑行的最大里程数
        power_km = self.valume * 10
        if power_km >= km:
            print(f"我用电瓶电量骑行了{km}公里")
        else:
            # 电量不够骑行全部的里程，电量用完后，还得用脚骑行
            print(f"我用电瓶电量骑行了{power_km}公里")
            # 当电量耗尽的时候，需要调用Bicycle的run方法骑行
            # 非继承调用
            # bike = Bicycle()
            # bike.run(km - power_km)

            # 继承调用
            super().run(km - power_km)

ebike = EBicycle(10)
ebike.run(120)

# bike = Bicycle()
# bike.run(10)
