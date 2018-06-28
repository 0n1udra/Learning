import os

from COLORS import *

Bright()
# brightens text


promptName = str(input("User > "))

def prompt():
    print(Fore.YELLOW + promptName, end='')
    print(Fore.GREEN + " > ", end='')
commandInput = str(input())
prompt()

Stay = True


while Stay:
    if commandInput == 'EXIT': Stay = False
    print(Fore.WHITE, end='')
    os.system(commandInput)
    prompt()
    commandInput = str(input())


