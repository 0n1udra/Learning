##### Lists and Tuples #####

#### Lists ####

### Making lists ###
list1 = [1,2,3,4,5]
# basic list with integers
# integer is a whole number, float is a decimal
list2 = [1,'two',3]
# list with integers and strings
One = 1
list3 = [One, 2, 3.3, 'four']
# list with variables, integers, floats, and strings

### Printing ###
print(list1)
# prints all of list1

print(list2[1])
# prints SECOND item of list2
# it prints the second item because the computer counts a zero(0) as a number.

print(list3[1:])
# prints everything after the second item
print(list2[:2])
# reverse
print(list2[1:2])
# prints items from 1 to 2
print(list2[-1])
# prints last item

list5 = [1,2,3, [4,5,6], 7,8,9]
# a list in a list
print(list5[3])
# prints all items in position 3 in list5
print(list5[3][1])
# prints second item in the list in list
list6 = [1,[2,[3,4]]]
print(list6[1][1][1])
# prints 4, from list within list within a list :). can go on for ever!

### List Comprehension ###

x = [1,2,3,4,5] # new list
for i in x:
# loops 5 times, because that's how long list x is
    print(i * 2)
    # prints out list item of this loop and mulitplies by t2

# a faster way to do the same thing
print([j * 2 for j in x])
# does the same thing, but puts it in a list

#### Tuples ####


##### Dictionarys #####
dict1 = {'one' : 1, 'two' : 2, 'three' : 3}

dict_var = 'hi'
dict2 = {'variable' : dict_var, 'integer' : 10, 'float' : 10.123, 'strign' : 'HI!'}

print(dict1[1])