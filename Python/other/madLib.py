
# Prints Letter with number next to them
def printNumsLetters():
    import string
    Letters = string.ascii_lowercase
    for i in range(len(Letters)):
        print(i, Letters[i])

# Creates a setence from lists
def sentenceGen():
    nouns = ['dog', 'computer', 'cat', 'phone', 'arrow', 'tablet', 'people', 'fire', 'stuff']
    verbs = ['digging', 'working', 'asking', 'sleeping' , 'swimming', 'watching', 'listening', 'stuffing']
    adj = ['red', 'pretty', 'weird', 'awkward', 'spooky' , 'lucky', 'shitty']
    prep = ['was', 'is']
    arti = ['a', 'an', 'the']
    from random import choice
    for i in range(3):
        print(choice(arti), choice(adj), choice(nouns), choice(prep), choice(verbs))



def run():
    sentenceGen()
    #printNumsLetters()











if __name__ == '__main__':
    run()