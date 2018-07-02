from colorama import *



# Resets Text and Background color
def ResetA(): print(Style.RESET_ALL, end='')

# Resets text color
def ResetT(): print(Fore.RESET, end='')

# Resets Background color
def ResetB(): print(Back.Reset, end='')

# Brightens the text color
def Bright(): print(Style.BRIGHT, end='')

# Dim text
def Dim(): print(Style.DIM, end='')

def Norm(): print(Style.NORMAL, end='')

# Prints out example text
def Example():

    print("Normal Text")


    Bright()
    print("bright Text")

    Dim()
    print("dim text")

    print(Fore.RED + "RED")

    ResetA()
    print("A back to normal")


if __name__ == '__main__':
    Example()
