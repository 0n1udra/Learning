RESET = "\u001B[0m"
# resets fg and bg
BLACK = "\u001B[30m"
LIGHT_RED = "\u001B[31m"
LIGHT_GREEN = "\u001B[32m"
BROWN = "\u001B[33m"
LIGHT_BLUE = "\u001B[34m"
CYAN = "\u001B[36m"
GREY = "\u001B[37m"

# background colors
BLACK_BG = "\u001B[40m"
RED_BG = "\u001B[41m"
GREEN_BG = "\u001B[42m"
YELLOW_BG = "\u001B[43m"
BLUE_BG = "\u001B[44m"
PURPLE_BG = "\u001B[45m"
CYAN_BG = "\u001B[46m"
WHITE_BG = "\u001B[47m"

# other colors
BRIGHT_PINK = '\033[95m'
BRIGHT_BLUE = '\033[94m'
BRIGHT_GREEN = '\033[92m'
BRIGHT_YELLOW = '\033[93m'
BRIGHT_RED = '\033[91m'
BRIGHT_WHITE = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def println(text, fg="", bg=""): print(fg+ bg + text, RESET)

def printlnErr(text, location=''): print(BRIGHT_RED+"ERROR: {} | {}".format(location, text), RESET)
def printlnWarn(text, location=''): print(BRIGHT_PINK + "WARNING: {} | {}".format(location, text), RESET)
def printlnInfo(text, location=''): print(BRIGHT_YELLOW + "INFO: {} | {}".format(location, text), RESET)
def printlnNote(text, location=''): print(BRIGHT_BLUE + "NOTE: {} | {}".format(location, text), RESET)
def printlnUsrinp(text): print(BRIGHT_GREEN + text, ">", RESET)
def printlnOutp(text): print(CYAN + text, RESET)

def printlnBold(text): print(BOLD + text, RESET)
def printlnUnderL(text): print(UNDERLINE + text, RESET)


def printReg(text, fg=None, bg=None): print(fg+ bg + text, RESET, end='')
def printErr(text, location=''): print(BRIGHT_RED + "ERROR: {} | {}".format(location, text), RESET, end='')
def printInfo(text, location=''): print(BRIGHT_YELLOW + "INFO: {} | {}".format(location, text), RESET, end='')
def printWarn(text, location=''): print(BRIGHT_PINK + "WARNING: {} | {}".format(location, text), RESET, end='')
def printNote(text, location=''): print(BRIGHT_BLUE + "NOTE: {} | {}".format(location, text), RESET, end='')
def printUsrinp(text): print(BRIGHT_GREEN + text+" >", RESET, end='')
def printOutp(text): print(CYAN + text, RESET, end='')
def printBold(text): print(BOLD + text, RESET, end='')
def printUnderL(text): print(UNDERLINE + text, RESET, end='')

def printlnRed(text): print(BRIGHT_RED + text, RESET)
def printlnYell(text): print(BRIGHT_YELLOW + text, RESET)
def printlnPink(text): print(BRIGHT_PINK + text, RESET)
def printlnBlue(text): print(BRIGHT_BLUE + text, RESET)
def printlnCyan(text): print(CYAN + text, RESET)
def printWhite(text): print(BRIGHT_WHITE + text, RESET)


"""
Red - Error
Yellow - Info
Purple - Warning
Blue - Note
Green - User input > 
Cyan - User output
Bold ~ Other Info
UnderL ~ Special info
"""


# Other stuff
_yesStrings = ['Y', 'y', 'yes', 'Yes', 'YES']
_noStrings = ['N', 'n', 'no', 'No', 'NO']
def askYesNo():
    printUsrinp("Yes/No")
    _yesNoAnswer = input()
    if(_yesNoAnswer in _yesStrings):
        return True
    elif(_yesNoAnswer in _noStrings):
        return False
    else:
        return False
    # asks Yes/No, returns boolean




# with these you can't use , like in print to print multiple items, have to use +, and convert if need be
# most of the time you'll want to use printUsrinp not printlnUsrinp, if you want them to type on the same line
if __name__ == '__main__':
    println("Regular Text")
    print("Status: location | info")
    printlnErr("Eif.__main__", "Error info in RED")
    printlnInfo("if.__main__", "Information in Yellow ")
    printlnWarn("WARif.__main__", "Warning in Purple or Pink ")
    printlnNote("if.__main__", "Note text in Blue")
    printUsrinp("User Input text")
    usrInp = input()
    printlnOutp("OUPUT: if __main__.usrInp | Output of usrInp : " + usrInp)

    printlnBold("Bold Text")
    printlnUnderL("Underlined Text")
    # you can combine BOLD and UNDERLINE with other colors


    print(askYesNo())