import socket
import random as rd


import itertools as it
def findIP():
    opt1 = '127'
    opt2 = '192.168'

    for i in range(255):
        addr = opt2 + '1' + str(rd.randint(0, 255))

        try:
            socket.inet_aton(addr)
            print("Valid IP")
        except socket.error:
            print("Invalid IP")

key = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(n, plaintext): # asks for rotation(key) and the message
    result = '' # end result well be in here
    for l in plaintext.lower(): # loops through every letter from message
        try: result += key[(key.index(l) + n ) % 26]
        # finds the index of current letter from key then finds the next letter up and puts it in result. the % makes sure it doesn't crash if you go over like 100 or something
        except ValueError: result += l # if it fails like from a symbol or etc, it'll just add it to result

    print(result.lower())

def decrypt(n, ciphertext):
    result = ''
    for l in ciphertext:
        try: result += key[(key.index(l) - n) % 26]
        except ValueError: result += l

    print(result)



def get_Command():
    print("e for encrypt. d for decrypt")
    command = input("Command > ")
    msg = input("Input a message > ")
    rotation = int(input("Rotation number > "))

    if command == 'e': encrypt(rotation, msg)
    elif command == 'd': decrypt(rotation, msg)



get_Command()

