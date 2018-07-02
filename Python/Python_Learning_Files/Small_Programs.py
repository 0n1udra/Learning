def age():
    names2, ages2 = [], [] # sets data variables
    name2 = input("input name or done > ") # ask for input of name, to start it off
    while name2 != 'done': # keeps looping until input is 'done'
        age2 = int(input("age of " + name2 + " > ")) # ask for age of person
        names2.append(name2), ages2.append(age2) # adds name and age to lists
        name2 = input("name or done >  ") # ask for name again
    max2 = max(ages2) # finds max age in 'ages2' list
    index2 = ages2.index(max2) # finds position of max age in 'ages2' list
    for i in range(len(names2)): print(names2[i], ages2[i]) # prints inputted info
    print("Oldest person is:", names2[index2], "at:", ages2[index2]) # prints the name and age of oldest person

def Guess2():
    from random import randint # imports module needed to make random number
    tries = 0 # counts how many tries it took
    ans = randint(0,100) # generates random number between 0 to 100, and gives it the name 'ans'
    while True: # runs until you get it correct
        inp = int(input("Guess > ")) # ask for your input
        if inp == ans: # if you guessed correct, it prints 'yay'
            print("Yay you got it!")
            print("it took", tries, "tries") # prints how many tries it took
            break # stops program, becuase you won
        elif inp > ans: # checks if your input is greater then the answer
            tries += 1 # adds one to tries
            print("Go Smaller") # if so it prints this
        elif inp < ans: # checks if input is smaller
            tries += 1
            print("Go Bigger")
        else:
            print("uh?")

def n3():

    x = 0
    while n != 1:
        x += 1
        if n % 2 == 0:
            print(str(n) + ', even')
            n /= 2
        else:
            print(str(n) + ', odd')
            n = n * 3 + 1
    print(x)

def fibo():
    # this generates the fibonacci sequence, with length entered

    length = int(input("How long to run it? > "))
    numbers = [1]
    currNum = 1
    for i in range(length):
        numbers.append(currNum)
        x = numbers.index(currNum)
        currNum = numbers[x - 0] + numbers[x - 1]
        print(currNum)

def fibo_n3():
    n = int(input('type number: '))
    x = 0
    numbers = [1]
    currNum = 1
    for i in range(n):
        x += 1
        if n % 2 == 0:
            n /= 2
        else:
            n = n * 3 + 1

        numbers.append(currNum)
        x = numbers.index(currNum)
        currNum = numbers[x - 0] + numbers[x - 1]

        currN = currNum * 99 / 4.2532484 / 3.62 * 3 * n + n * 8

        print(currNum, '     ', str(n), '     ', str(currN))

def fibo_recur(num):
    x = 0
    counter = num
    n = 1
    if (counter <= 0):
        return 0
    else:
        print(n)
        return x + fibo_recur(counter - 1)

def divisor(num):
    num = int(input("Number Please > "))
    Range = range(1, x + 1)
    count = 0
    for i in Range:
        if x % i == 0:
            count += 1
            print(i, ' : divisor')

    print("This many divisors: ", count)

Programs = dir()[10:]


if __name__ == '__main__':
    print("Available Programs: ", Programs)
    INPUT = str(input(("Choose > ")))
