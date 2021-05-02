from os import read
from english import *



def printStoredMessage(path):
    fl = open(path)
    entire = fl.read()
    fl.close()
    print(entire)
    

def handleCommand(usrInput):
    usrInput = str(usrInput)
    parts = usrInput[1:].split(" ")
    if parts[0] == "commands":
        printStoredMessage("commands.txt")
    elif parts[0] == "about":
        printStoredMessage("description.txt")
    elif parts[0] == "reset":
        print("Sentance cache has been reset.")
    elif parts[0] == "exit":
        return False
    else:
        print("Command not recognized. See $commands for list of valid commands.")

    # If no other things happened return true
    return True

def handleUserSentance(usrInput):
    pass


if __name__ == "__main__":
    wordDict = loadWordDictionary("smalldict.txt")

    shouldExit = False
    userInput = ""
    printStoredMessage("welcomemsg.txt")
    while (not shouldExit):
        print("> ",end='')
        userInput = input()
        if userInput.startswith("$"):
            # THis is a user command! We must dissect it
            shouldExit = not handleCommand(userInput)
        else:
            handleUserSentance(userInput)
    