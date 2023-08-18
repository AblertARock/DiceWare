import random

def roll():
    #Define "dice".
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    die3 = random.randint(1,6)
    die4 = random.randint(1,6)
    die5 = random.randint(1,6)
    #Convert to string.
    die1 = str(die1)
    die2 = str(die2)
    die3 = str(die3)
    die4 = str(die4)
    die5 = str(die5)
    #Converts to searchable chunk.
    chunk = die1 + die2 + die3 + die4 + die5
    #Puts end result in variable.
    return chunk

diceRoll = roll()

print(diceRoll)

with open("/workspaces/DiceWare/EFFWordlist", "r") as EFFWordlist:
    lines = EFFWordlist.readlines()
    for line in lines:
        if line.find(diceRoll) != -1:
            word = line.replace(diceRoll + "    ","")