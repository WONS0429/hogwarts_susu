# -*-coding: utf-8 -*-
# @Time    :2020-11-5 下午 12:46
# @Author  :susu
# @File    :python_oop5.py
"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西
（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""


# 定义一个宠物类（pet）
class Pet:

    # 定义构造函数
    def __init__(self, variety, color, weight):
        self.variety = variety
        self.color = color
        self.weight = weight

    # 定义吃eat函数，实现吃饭的方法
    def eat(self):
        print(f"{self.variety}喜欢吃鱼")

    # 定义sleep函数
    def sleep(self):
        print("宠物喜欢睡觉")


# 定义一个Cat类，继承宠物类
class Cat(Pet):

    # 定义play函数，实现玩耍的方法
    def play(self, toy):
        print(f"小猫喜欢玩{toy}")


# 实例化
mimi = Cat("加菲猫", "白色", 8)
mimi.eat()
mimi.play("球")


# 定义Computer类
class Computer:

    # 定义构造函数
    def __init__(self, color, size, brand):
        self.color = color
        self.size = size
        self.brand = brand

    # 定义函数internet，实现上网的功能
    def internet(self):
        print("电脑可以用来上网")

    # 定义函数playGame，实现玩游戏的功能
    def playGame(self):
        print("电脑可以玩游戏")


notebook = Computer("白色",14,"Dell")
notebook.playGame()


# 定义一个手机类（Phone）
class Phone:
    # 定义构造函数
    def __init__(self, brand, color, size, network, phoneOs):
        self.brand = brand
        self.color = color
        self.size = size
        self.network = network
        self.phoneOs = phoneOs

    def call(self):
        print(f"{self.brand}手机可以打电话")

    def sendMessage(self):
        print(f"{self.brand}手机可以发短信")


# 定义一个智能手机类，继承手机类
class SmartPhone(Phone):

    # 定义chat函数，实现聊天功能
    def chat(self):
        print("智能手机可以聊天")

    def playGame(self):
        print("智能手机可以打游戏")


# 实例化
myphone = SmartPhone("apple", "pink", 3.5, "4G", "ios")
myphone.sendMessage()


# 定义一个Human类
class Human:
    # 构造函数
    def __init__(self, name, age, gender, height, weight, color):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.color = color

    def work(self, job):
        print(f"我的职业是{job}")

    def hobby(self, hob):
        print(f"我的爱好是{hob}")


Zhangsan = Human("张三", 26, "male", "180", "75", "black")
Zhangsan.work("测试")
Zhangsan.hobby("打游戏？？？")





# 定义一个房间类(Room)
class Room:

    def __init__(self,size,color):
        self.size = size
        self.color = color

    def work(self):
        print("房间里可以工作")

    def sleep(self):
        print("房间里可以休息")

babyroom = Room(20,"pink")
babyroom.sleep()

