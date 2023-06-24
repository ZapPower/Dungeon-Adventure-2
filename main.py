from Player import Player
from Enemies.Orc import Orc
import displayCommands as dc
import os
import random
import time
import json

dc.disp("Welcome to Dungeon Adventure 2")
dc.disp("What is your name?: ", .04, False)
pName = input()
print("")
dc.disp("World Level -- 1", .1)

p = Player(pName)

# TODO: create armor system WOW :O
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

currSkills = {}

worldLevel = 1

# returns a new instance of a monster from the enemies folder


def chooseMonster(atk, spd, df, wl):
    enemies = os.listdir('Enemies')
    enemyInd = random.randint(0, len(enemies) - 2)
    if (enemies[enemyInd] == "Orc.py"):
        return Orc(atk, spd, df, wl)

# updates the player's skills based on skills.json


def updateCurrSkills(player):
    skillsJSON = open("skills.json")
    allSkills = json.load(skillsJSON)
    skillsJSON.close()

    global currSkills
    newSkills = []
    for skill in allSkills:
        if (currSkills.has_key(skill)):
            continue

        if (allSkills[skill]["lvl"] <= player.lvl):
            newSkills.append(skill)
            currSkills[skill] = allSkills[skill]

    return newSkills


fightActions = ["attack", "item", "run"]
# small function to handle actions


def checkAction(action):
    if (action not in fightActions):
        dc.disp("That was not a valid action.")
        return checkAction(dc.dispFightMenu().lower())

    match action:
        case "attack":
            chosen = dc.dispSkills(currSkills)
            attack(chosen)


def attack(action):
    # TODO: handle string funny action with dict keys (aka how to choose skill)
    if (action == "back"):
        return checkAction(dc.dispFightMenu().lower())

    if (action not in list(currSkills.keys)):
        dc.disp("That was not a valid skill.")
        dc.disp("Choose a Skill or enter \"Back\" to return: ", end=False)
        return attack(input())

    global p
    global enemy

    output = p.attackChr(enemy, currSkills[action])
    # TODO: continue this ^^^


# main game loop
while True:
    # generate enemy stats (this might be better handled within each enemy file for enemy variety)
    # TODO: move stat calculations into class file
    enemyAtk = worldLevel * 2
    enemySpd = worldLevel
    enemyDf = (worldLevel+1) * 2

    # choose enemy
    enemy = chooseMonster(enemyAtk, enemySpd, enemyDf, worldLevel)

    # begin fight -- needs to be within its own game loop
    # TODO: create better way to handle menu system
    dc.dispFightStats(p)
    dc.dispFightStats(enemy)
    action = dc.dispFightMenu().lower()
    checkAction(action)

    # this should occur AFTER every fight, thus outside of fight loop
    newSkills = updateCurrSkills(p)
    for skill in newSkills:
        dc.disp(f"You have unlocked a new Skill!: {skill}")
