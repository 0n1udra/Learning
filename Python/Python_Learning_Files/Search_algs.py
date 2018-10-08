

def isIn(L, v):
    for i in L:
        if i == v:
            print("True")
            break
# takes a list and value, goes through each item in list checks if current item is the value.
# if so it prints True and stops

list1 = [1, 2, 3, 4, 5]
isIn(list1, 3)

print(3 in list1)  # this does the same thing as the isIn function

print('_'*50, "\nBinary Search\n")
def binary_Search(L, v):

    left = 0
    right = len(L) - 1
    print("Left: {} | Right: {}".format(left, right))

    while left <= right:
        midpoint = (left + right) // 2
        print("Midpoint: ", midpoint)
        current_item = L[midpoint]
        print("Current Item: ", current_item)
        if current_item == v:
            print(midpoint)
            return midpoint
        else:
            if v < current_item:
                right = midpoint - 1
            else:
                left = midpoint + 1
        print("Left: {} | Right: {}".format(left, right))

    return None

print(binary_Search(list1, 2))

