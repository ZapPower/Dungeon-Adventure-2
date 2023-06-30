from Monster import Monster
import json
import random
import displayCommands as dc


class Orc(Monster):
    def __init__(this, attack, speed, defense, wl):
        max = 10 * wl + 2 * defense
        super().__init__(attack, speed, defense, wl, max)
        this.name = "Orc"
        this.luck = 5
        this.stm = wl * 3 + 2
        s = open("OrcSkills.json")
        this.skills = json.load(s)
        s.close()

        # TODO: figure out stat configuation so its better

    # attacks character using a chosen skill based on available stamina
    # procs a random effect and gives it to the chosen character
    # returns True if the chosen character is alive
    # returns False if the chosen character is dead
    # also returns damage dealt
    def attackChr(this, character):
        # choose skill to use (for now it wil be based on stamina)
        for skill in reversed(sorted(this.skills.keys())):
            if this.stm >= this.skills[skill]["stm"]:
                chosenSkill = this.skills[skill]

        # choose effect based on proc chance
        for effect in chosenSkill["effect"]:
            rng = float(random.randint(1, 100))
            if chosenSkill["effect"][effect]["proc"] < rng / 100:
                character.setCurrEffect(skill["effect"][effect])
                character.setCurrEffectname(effect)
                dc.effectProcMessage(effect, character.name)

        # calculate and apply damage
        dmg = this.attack * chosenSkill["dmgMult"]
        character.setHealth(character.hp - dmg)

        if character.hp <= 0:
            return False, dmg
        return True, dmg
