class Monster:
  def __init__(this, attack, speed, defense, worldLvl, maxHp):
    this.attack = attack
    this.speed = speed
    this.defense = defense
    this.worldLvl = worldLvl
    this.maxHp = maxHp
    this.hp = maxHp
    this.currEffect = None
    this.currEffectName = None

  def setHealth(this, newHp, isPct = False):
    this.hp = newHp
    if (isPct):
      this.hp = round(this.maxHp * newHp * .01)

  def attackChr(this, character):
    character.setHealth(character.hp - this.attack)
    if (character.hp <= 0):
      return False
    return True

  def setCurrEffect(this, effect):
    this.currEffect = effect
    
  def setCurrEffectName(this, name):
    this.currEffectName = name
    
  #applies the damage from the effect given to the character
  #returns damage amount
  def applyCurrEffect(this):
    if (this.currEffect == None):
      return
    
    this.currEffect["duration"] -= 1
    dmgTaken = round(this.hp * (this.currEffect["dmgPct"] / 100.0), 1)
    this.hp -= dmgTaken
    return dmgTaken