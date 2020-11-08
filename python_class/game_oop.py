# -*-coding: utf-8 -*-
# @Time    :2020-11-5 上午 11:53
# @Author  :susu
# @File    :game_oop.py

class Game:

    # 定义构造函数
    def __init__(self,my_hp,enemy_hp):
        # 定义4个变量存放数据
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

    # 定义fight函数，实现游戏逻辑
    def fight(self):
        # 打印敌人的血量和攻击力
        print(f"敌人的血量{self.enemy_hp}，敌人的攻击力{self.enemy_power}")
        # 加入循环，让游戏可以进行多轮
        while True:
            self.my_hp = self.my_hp - self.enemy_power
            self.enemy_hp = self.enemy_hp - self.my_power

            print(self.my_hp)

            # 判断谁的血量先小于等于0
            if self.my_hp <= 0:
                # 打印我和敌人的剩余血量
                # print(f"我的剩余血量为{self.my_hp}")
                # print(f"敌人的剩余血量为{self.enemy_hp}")
                print("我输了")
                # 满足条件跳出循环
                break
            elif self.enemy_hp <= 0:
                # 打印我和敌人的剩余血量
                # print(f"我的剩余血量为{self.my_hp}")
                # print(f"敌人的剩余血量为{self.enemy_hp}")
                print("我赢了")
                # 满足条件跳出循环
                break

    # 定义休息的方法
    def rest(self,rest_time):
        print(f"太累了，休息{rest_time}分钟")



# game = Game()
# game.fight()
