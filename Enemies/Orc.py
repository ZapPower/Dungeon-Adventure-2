from Monster import Monster
import json


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
        
    def attackChr(this, character):
        #TODO: Complete the attackChr function for Orc
        
        # choose skill to use (for now it wil be based on stamina)
        for skill in this.skills:
            pass



        if (character.hp <= 0):
            return False
        return True