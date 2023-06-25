import random
import displayCommands as dc


class Player:
    def __init__(this, name):
        this.attack = 5
        this.defense = 5
        this.speed = 5
        this.luck = 1
        this.name = name
        this.lvl = 1
        this.maxHp = 20
        this.hp = this.maxHp
        this.stm = 10
        this.currEffect = None
        this.currEffectName = None
        this.exp = 0
        this.nextLvl = 10

    def setHealth(this, newHp, isPct=False):
        this.hp = newHp
        if (isPct):
            this.hp = round(this.maxHp * newHp * .01)

    def setMaxHp(this, newMax):
        this.maxHp = newMax

    def setAtk(this, newAtk):
        this.attack = newAtk

    def setDef(this, newDef):
        this.defense = newDef

    def setSpd(this, newSpd):
        this.speed = newSpd

    def setLuck(this, newLuck):
        this.luck = newLuck

    def setName(this, newName):
        this.name = newName

    # attacks given character with a passed skill from skills.json
    # procs a random effect and gives it to the chosen character
    # returns True if the chosen character is alive
    # returns False if the chosen character is dead
    # also returns damage dealt
    def attackChr(this, character, skill):
        for effect in skill["effect"]:
            rng = random.randint(1, 100)
            if (skill["effect"][effect]["proc"] < rng):
                character.setCurrEffect(skill["effect"][effect])
                character.setCurrEffectName(effect)
                dc.effectProcMessage(effect, character.name)

        dmg = this.attack * skill["dmgMult"]
        character.setHealth(character.hp - dmg)
        if (character.hp <= 0):
            return False, dmg
        return True, dmg

    def setCurrEffect(this, effect):
        this.currEffect = effect

    def setCurrEffectName(this, name):
        this.currEffectName = name

    # applies the damage from the effect given to the character
    # returns damage amount
    def applyCurrEffect(this):
        if (this.currEffect == None):
            return
        if (this.currEffect["duration"] == 0):
            dc.effectRunOutMessage(this.currEffectName, this.name)
            this.currEffect = None

        this.currEffect["duration"] -= 1
        dmgTaken = round(this.hp * (this.currEffect["dmgPct"] / 100.0), 1)
        this.hp -= dmgTaken
        dc.effectAppliedMessage(this.currEffectName, this.name, dmgTaken)
        return dmgTaken
