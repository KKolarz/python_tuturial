import random


class Enemy:
    hp = 200

    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

    def getAtk(self):
        print("atkl is ", self.atkl)

    def getHp(self):
        print("Hp is ", self.hp)


enemy1 = Enemy(20, 40)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(49, 75)
enemy2.getAtk()
enemy2.getHp()

'''
playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh, 1)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for ", dmg, " points of damage. Current HP is ", playerhp)

    if playerhp > 30:
        continue  # ignoruje to co nastepuje w petli po czym zabiera się za jej wykonywanie od poczatku

    print("You have low health. You have been teleported to the nearest inn.")
    break
'''