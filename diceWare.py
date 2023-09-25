import random
import os
import platform
import time

system = platform.system()

try:
    import pyperclip
    havePyperclip = True
except:
    havePyperclip = False

    print("""You need to install pyperclip for the copying mechanism to work.
    If you don't want to instal pyperclip, this program will work just fine.
    If you do want to use the copy mechanism, run "pip install pyperclip".""")

    installPyperclip = input("Do you want to install pyperclip?: ")

    if installPyperclip == "y":
        os.system("pip install pyperclip")
        time.sleep(10)
        havePyperclip = True



if system == "Windows":
    os.system("cls")
if system == "Darwin" or "Linux":
    os.system("clear")

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

def strCut(string):
    lineList = string.split("\t")
    baseWord = lineList[1]
    finalWord = baseWord.capitalize()
    return finalWord

word = ""

wordNum = input("Amount of words in password: ")
try:
    wordNum = int(wordNum)

except:
    while True:
        wordNum = input("Please enter a VALID number: ")
        try:
            wordNum = int(wordNum)
            break
        except:
            placeholder = ""


for i in range(wordNum):
    diceRoll = roll()
    with open("/workspaces/DiceWare/EFFWordlist", "r") as EFFWordlist:
        lines = EFFWordlist.readlines()
        for line in lines:
            if line.find(diceRoll) != -1:
                tempWord = strCut(line)
                word = word + tempWord

word = word + "5%"            
word = word.replace("\n", "")
print("Your password is: " + word)

if havePyperclip == True:
    try:
        pyperclip.copy(word)
        print("Your password has also been copied to the clipboard.")

    except:
        print("""\n Sorry, the program was unable to copy your password to the clipboard.
        If you're running on Linux, try one of these methods:
            a) "sudo apt-get install xsel" to install the xsel utility.
            b) "sudo apt-get install xclip" to install the xclip utility.
            c) "pip install gtk" to install the gtk Python module.
            d) "pip install PyQt4" to install the PyQt4 Python module.
        If you're running on chromeOS, you're screwed. (Like me!)""")

blank = input("Hit enter to close the program.")