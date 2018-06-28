# if on 32bit OS:
# import Image
# else:
from PIL import Image # import Image tools from PIL, pillow for 32bit
import numpy as np # numpy
import matplotlib.pyplot as plt # matplotlib to show image
import time as t
from collections import Counter

i = Image.open('sentdex.png')
# opens image
iar = np.array(i)
# makes array from image data


# this well open up all the number pictures, read them, and put all of the array data into a text file.
# !!! RUN only once, if don't have text file already
def createExample():
    numberAE = open('numArEx.txt', 'a')
    # number array example, makes a text file
    numbersWeHave = range(0,10)
    versionWeHave = range(1,10)
    # ranges for the file names

    for eachNum in numbersWeHave:
    # for each number in numbers we have
        for eachVer in versionWeHave:
        # for each version in versions we have
            Current = str(eachNum) + '.' + str(eachVer)
            # loops through and makes file names 0.1 to 9.9. 0.1 - 0.9 then 2.1 to 2.9, and so on
            imgFileP = 'numbers/' + Current + '.png'
            # image file path for the paths of the png numbers
            ei = Image.open(imgFileP)
            # opens file of this instance
            eiar = np.array(ei)
            # then converting to array
            eiar1 = str(eiar.tolist())

            lineTW = str(eachNum) +'::'+ (Current) + '::'+eiar1+'\n'
            # line to write,
            numberAE.write(lineTW)
            # then writes lineWT to numArEx.txt


# this takes a image and converts it to black and white by it's threshold
def threshhold(imageArray):
    balanceAr = [] # blank balance array
    newAr = imageArray
    for eachRow in imageArray: # loops through each row in the image array
    # for each row in image array
        for eachPix in eachRow: # then loops through each pixel array
            # t.sleep(1)
            avgNum = reduce(lambda x, y: x + y, eachPix[:3])/ len(eachPix[:3])
            # finds average number for each pixel
            balanceAr.append(avgNum)
            # appends the average pixel to balanceAr
    print(balanceAr)
    balance = reduce(lambda x, y: x + y, balanceAr) / len(balanceAr)
    # finds the average in the pixels averages

    for eachRow in newAr:
        for eachPix in eachRow:
            if reduce(lambda x, y: x + y, eachPix[:3])/ len(eachPix[:3]) > balance:
               # checks to see if the average is above 255 or below
               for i in range(4): eachPix[i] = 255
               # if above it changes all the data to 255
            else:
                for j in range(3):
                    eachPix[j] = 0
                    eachPix[3] = 255
                    # if below changes to 0 with 255 alpha
    return newAr # returns the new threshold array




def whatNum(filePath):
    matchedAr = []
    # matched array, for matched files
    loadEx = open('numArEx.txt', 'r').read().split('\n')
    # opens the numArEx text file, reads it, and splits it by newline

    i = Image.open(filePath)
    # opens file
    iar = np.array(i)
    # gets image array data
    iarl = iar.tolist()
    # ???

    inQ = str(iarl) # number rin question
    # in question

    for eachEx in loadEx:
    # for each example in load examples
        if len(eachEx) > 3:
            splitEx = eachEx.split('::') # splits up data
            # split example by '::' the double colons
            cNum = splitEx[0] # sets current number
             # current Number is splitEx's first item
            cAr = splitEx[2] # sets current array
            # current array is splitEx's 3rd item
            eachPixEx = cAr.split('],') # gets each pixel arrays
            # splits up by ], the brackets, so breaks up data into just the arrarys

            eachPixInQ = inQ.split('],') # each pixel in qestion
            # gets each pixel from file in question

            Count = 0
            while Count < len(eachPixEx):
            # runs for each pixel array in eachPixEx
                if eachPixEx[Count] == eachPixInQ[Count]:
                # checks to see if the x pixel from the example file is the same from the user chosen file
                    matchedAr.append(cNum)
                    # if so appends that to matched array

                Count += 1
    x = Counter(matchedAr)
    # checks to see which one matched the most
    print 'similarities', x

    graphX = []
    graphY = []
    # blank lists
    for eachT in x:
        # for each thing in x
        graphX.append(int(eachT))
        graphY.append(x[eachT])
        # appends the number and the corresponding data to the graphX and graphY


    MaxY = max(graphY)
    # finds the maximum
    Max = graphY.index(MaxY)
    # finds the position of the maximum
    mX = graphX[Max]
    # get's the numeber that corresponds with graphY

    print 'should be ' + str(mX) + ' with ' + str(MaxY) + '/400 accuracy.'
    # prints out should be x with x/400 accuracy


    fig = plt.figure()
    av1 = plt.subplot2grid((4,4), (0,0), rowspan=1, colspan=4)
    plt.title("It's most likely: " + str(mX))
    # adds title. It's most likey: x

    av2 = plt.subplot2grid((4,4), (1,0), rowspan=3, colspan=4)


    av1.imshow(iar)
    # shows inputted image
    av1.axes.get_yaxis().set_visible(False)
    av1.axes.get_xaxis().set_visible(False)
    # disables x and y tick labels and marks

    Bars = av2.bar(graphX, graphY, align='center')
    # graphs the similarities with bars, higher the better
    Bars[Max].set_color('r')
    # fills the guessed number red


    #plt.ylim(400)

    xloc = plt.MaxNLocator(12)
    # sets the ticks
    av2.xaxis.set_major_locator(xloc)

    plt.show()

whatNum('test.png')
