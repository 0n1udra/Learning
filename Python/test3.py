print("Input First name, Last name, Age, Race(optional), and attributes. Separated by commas.")
print("Ex. Jane, Doe, 21, American, Fighter")

while (True):
    usrInput = raw_input("> ")
    try:
        usrInput = list(usrInput.split(','))
    except ValueError:
        continue
    else:
        if(len(usrInput) < 5)




