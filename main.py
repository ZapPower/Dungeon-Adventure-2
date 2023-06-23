from Player import Player
from Enemies.Orc import Orc
import displayCommands as dc
import os
import random
import time
import json

dc.disp("Welcome to Dungeon Adventure 2")
dc.disp("What is your name?: ", .025, False)
pName = input()
print("")

p = Player(pName)

enemy = None
armor = {
  "Head": ["", None],
  "Chest": ["", None],
  "Leg": ["", None],
  "Boot": ["", None]
}

i = open("items.json")
items = json.load(i)
i.close()

worldLevel = 1


def chooseMonster(atk, spd, df, wl):
  enemies = os.listdir('Enemies')
  enemyInd = random.randint(0, len(enemies) - 2)
  if (enemies[enemyInd] == "Orc.py"):
    return Orc(atk, spd, df, wl)


#main game loop
while True:
  #choose enemy type
  enemyAtk = worldLevel * 2
  enemySpd = worldLevel
  enemyDf = (worldLevel+1) * 2
  enemy = chooseMonster(enemyAtk, enemySpd, enemyDf, worldLevel)
  dc.dispFightStats(p)
  dc.dispFightStats(enemy)
  action = dc.dispFightMenu().lower()
  dc.getAction(action)