import os
import random

def roll()
    #Define "dice".
    die1 = random.randint()
    die2 = random.randint()
    die3 = random.randint()
    die4 = random.randint()
    die5 = random.randint()
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

text = roll()

print(text)