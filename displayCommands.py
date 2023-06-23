import time

#displays a string one letter at a time
#can pass a speed and whether or not the string will end with a newline
def disp(string, speed = 0.05, end=True):
  for letter in string:
    print(letter, end="", flush=True)
    time.sleep(speed)
  else:
    if (not end):
      return
    print("")

#displays the health and name for a character
def dispFightStats(character):
  name = character.name
  hp = character.hp
  maxHp = character.maxHp
  numBoxes = 20

  pctHp = float(hp) / maxHp
  healthBar = "▮" * round(pctHp * numBoxes)
  healthBar += "▯" * (numBoxes - len(healthBar))
  
  disp(name)
  disp(f"{healthBar} {round(pctHp * 100)}% ({hp}/{maxHp})")

def dispFightMenu():
  disp("Choose what to do (attack, item, run):")
  return input("")

def dispMainMenu():
  print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
  disp("Choose what to do (item, resume, exit)")
  print("/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/-/")
  
  
def getAction(action):
  match action:
    case "attack":
      
    case "item":
      
    case "run":
      
    case _:
      disp("That was not a valid action.")
      getAction(dispFightMenu().lower())
      
def getAttack(skillsAvailable):
  for skill in skillsAvailable:
    