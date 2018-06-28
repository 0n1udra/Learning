
def mario(height=5):
    #height = input("Enter a non-negative int < 24: >  ")
    for i in range(height+1):
        print(" " * (height - i), "#" *i + "  " + "#"*i)

    #mario(5)

def caesar(key=1):
    usrInp = input("plaintext > ")

    result = ""

    # Loops through string, editing one character at a time
    for i in usrInp:
        if i.islower():
            result += chr((((ord(i) + key) - 97) % 26) + 97)
        elif i.isupper():
            result += chr((((ord(i) + key) - 65) % 26) + 65)
        else:
            result += i

    print("ciphertext: ", result)

    #caesar(1)

def vigenere(Keyword='b'):
    Keyword.lower()

    usrInp = input("plaintext > ")

    result = ""

    j = 0 # Counter for keyword

    #Loops through string, editing one character at a time
    for i in usrInp:
        # So key gets looped through continuously
        j = j % len(Keyword)

        # Checks whether needs to edit current character
        if not i.isalpha():
            result += i
            continue

        # Gets the key for current char using typecasting
        cKey = (ord(Keyword[j]) - 97) % 26
        # Edits current character with corresponding key
        if i.islower():
            result += chr((((ord(i) + cKey) - 97) % 26) + 97)
        elif i.isupper():
            result += chr((((ord(i) + cKey) - 65) % 26) + 65)

        j+= 1

    print("ciphertext: ", result)

    #vigenere("b")

def credit(cardNumber):

    def digit(x): return list(map(int, str(x)))

    strCardNum = str(cardNumber)

    # Puts digits from cardNumber into a integer array
    cardNumArr = list(map(int, str(cardNumber)))

    # Checks if cardNumber is valid length
    cardNumRev = list(reversed(cardNumArr)) # Reverses array

    #cardNumRev[1::2] = [list(map(int, str(i * 2))) for i in cardNumRev[1::2]]
    for i in cardNumRev[1::2]:
        cardNumRev.remove(i)
        cardNumRev.extend(digit(i*2))

    numSum = digit(sum(cardNumRev))

    if (not len(str(cardNumber)) in (13, 15, 16)) and (numSum[1] == 0):
        exit("INVALID")

    # Checks what card it is
    if strCardNum[:2] in ('37', '34'):
        print("American Express")
    elif strCardNum[:2] in ('51', '51', '52', '54', '55'):
        print("Master Card")
    elif strCardNum[:1] == '4':
        print("Visa")
    else: print("INVALID")


credit(371449635398431)
credit(378282246310005)

