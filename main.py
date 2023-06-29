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
dc.disp("World Level -- 1", .15)

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
# TODO: create floor/room system (could be replacement for world level?)
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


# TODO: Add numbering functionality for choosing menu & skill options
fightActions = ["attack", "item", "run"]
# small function to handle actions


def checkAction(action):
    if (action not in fightActions):
        dc.disp("That was not a valid action.")
        return checkAction(dc.dispFightMenu().lower())

    match action:
        case "attack":
            chosen = dc.dispSkills(currSkills)
            if (attack(chosen)):
                return True

# handles the "attack" action, executing the given attack skill


def attack(action):
    if (action == "back"):
        return checkAction(dc.dispFightMenu().lower())

    skillChoices = [skill.lower() for skill in list(currSkills.keys)]
    if (action not in skillChoices):
        dc.disp("That was not a valid skill.")
        dc.disp("Choose a Skill or enter \"Back\" to return: ", end=False)
        return attack(input().lower())

    global p
    global enemy

    output = p.attackChr(enemy, currSkills[action])
    dc.disp(f"{enemy.name} has taken {output[1]} damage!")
    return output[0]


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
    # TODO: create monster encounter loop
    checkAction(action)  # IF THIS RETURNS TRUE THEN MONSTER IS DEAD***

    # this should occur AFTER every fight, thus outside of fight loop
    newSkills = updateCurrSkills(p)
    for skill in newSkills:
        dc.disp(f"You have unlocked a new Skill!: {skill}")
