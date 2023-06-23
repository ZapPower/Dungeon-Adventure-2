from Monster import Monster
class Orc(Monster):
  def __init__(this, attack, speed, defense, wl):
    max = 10 * wl + 2 * defense
    super().__init__(attack, speed, defense, wl, max)
    this.name = "Orc"
    this.luck = 5