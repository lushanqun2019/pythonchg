# -*- coding: utf-8 -*-
import time,random

class Hero():
    def __init__(self,name,level=1,HP=100,Q_hurt=10,W_hurt=15,E_hurt=20):
        self.name=name
        self.level=level
        self.HP=HP
        self.Q_hurt=Q_hurt
        self.W_hurt=W_hurt
        self.E_hurt=E_hurt
    
    def Q_attack(self,enemy):
        if not enemy.isdead():
            print('{}对{}进行了Q技能攻击，{}减少了{}HP'\
                  .format(self.name,enemy.name,enemy.name,self.Q_hurt))
            enemy.HP-=self.Q_hurt
            print('{}目前的HP为：{}'.format(enemy.name,enemy.HP))
            
    def W_attack(self,enemy):
        if not enemy.isdead():
            print('{}对{}进行了W技能攻击，{}减少了{}HP'\
                  .format(self.name,enemy.name,enemy.name,self.W_hurt))
            enemy.HP-=self.W_hurt
            print('{}目前的HP为：{}'.format(enemy.name,enemy.HP))

    def E_attack(self,enemy):
        if not enemy.isdead():
            print('{}对{}进行了E技能攻击，{}减少了{}HP'\
                  .format(self.name,enemy.name,enemy.name,self.E_hurt))
            enemy.HP-=self.E_hurt
            print('{}目前的HP为：{}'.format(enemy.name,enemy.HP))

    def isdead(self):
        if self.HP<=0:
            print('{}已经死亡'.format(self.name))
            return True
        else:
            return False
    def choose_attack(self,enemy):
        attack=random.choice([self.Q_attack,self.W_attack,self.E_attack])
        attack(enemy)
    
hero1=Hero('小乔',1,100,30,20,10)
hero2=Hero('亚瑟',1,100,5,20,35)
heros=[hero1,hero2]

round=0
while (not hero1.isdead()) and (not hero2.isdead()):
    round+=1
    print('====================ROUND {}===================='.format(round))
    time.sleep(1)
    hero1.choose_attack(hero2)
    if hero2.isdead():
        break
    time.sleep(1)
    hero2.choose_attack(hero1)
    if hero1.isdead():
        break
