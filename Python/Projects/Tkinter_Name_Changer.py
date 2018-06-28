from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import os

""" this well do stuff """

extensions = []
oldPath = ''
Paths = []
def updateFiles(path, newFileName='_'):
    global Paths
    dir_path = path
    os.chdir(dir_path)  # sets path of files
    chDirInput.delete('0', 'end')  # clears chDirInput whole entry box
    chDirInput.insert('0', os.getcwd())  # updates chDirInput entry box with the current dir
    Paths.append(os.getcwd())

    num = len(os.listdir())
    del (extensions[:])  # clears list items before updating it

    print(Paths)

    # gets the length of how many items in directory

    showFileWin.delete(*showFileWin.get_children())
    # clears all items in the treeview before listing more, by using tree.get_chidren()

    for item in os.listdir():

        extensions.append(os.path.splitext(item)[1])  # appends file extension to a list

        if os.path.isdir(item): item = item + '...'
        # adds three dots if the item is a directory

        showFileWin.insert('', 0, text=num, values=(item, '>', '  ' + newFileName))
        # shows every item in treeview
        num -= 1  # subtracts 1 from num, have to do it in reverse since it well show the numbers in reverse

    print('\n')


def changeDir(x):
    print("INFO: changeDir | chDirWin Input:", chDirInput.get())
    updateFiles(chDirInput.get())
    # this function well take the chDirInput entry box data and call updateFiles to update the files to show in treeview




def updateOldPath():
    global oldPath
    oldPath = '/'.join(os.getcwd().split('/')[:-1])
    # gets current directory, then splits it by / , then gets everything but the last item, then rejoins it with /.
    # Ex. /Users/drake/Desktop/Python > /Users/drake/Desktop


def goIntoDir(dir):
    # this well run when double click on a directory on the treeview
    c_item = str(showFileWin.item(showFileWin.selection(), 'values')[0])[:-3]
    # gets data(a dictionary) from selected treeview item, then only grabs the Original Name column data, then grabs
    # everything except the three dots
    try:
        updateFiles(os.getcwd() + '/' + c_item)  # updates the treeview with new files from new directory
        updateOldPath()

    except: print("ERROR: goIntoDir | Item not Directory.")


def goUpDirectory():
    try:
        updateOldPath()  # this is so you can go back more even when you type a full directory. Without this an
        # inputted a path then want to go back one directory; it won't work
        updateFiles(oldPath)  # updates treeview

    except: print("ERROR: goBackDirectory | Can't go back")

def goBackDirectory(): updateFiles(Paths[-2])

def refresh():
    updateFiles(Paths[-1], newNameInput.get())

def changeNames(newFileNames=''):
    # this well rename the files, and adds number to front
    make_sure = mb.askyesno('Change Names',
                            'Are you sure that you want to rename these files?')  # ('window title', 'main message')
    # asks to make sure you want to rename files
    gotInput = False
    # this is so if you didn't input anything it won't change the file names, even if you say yes to make_sure
    try:
        nameInp = newNameInput.get()
        if len(nameInp) > 1:
        # checks to see if got any input in rename box
            gotInput = True  # if so allows renaming, if not doesn't do anything

            try: nameInpList = nameInp.split('<x>')
            # tries to split input with <x>
            except: print('INFO: New Name Input | <x> not specified')

        else: print("INFO: New Name Input | No input")

    except: print("INFO: New Name Input | No input")
    print('nameInp: changeNames |', nameInp)
    print('nameInpList: changeNames |', nameInpList)

    if make_sure and gotInput:  # if yes...
        x = 0
        for file in os.listdir(os.getcwd()):  # loops through each file in current directory

            if not file.startswith('.'):  # makes sure it doesn't rename any files that starts with '.' which are usually hidden files
                xReplaced = nameInp.replace('<x>', '_{}_'.format(x))
                # replaces <x> in nameInp with _x_

                # this checks where you put the <x> in the rename box so you don't get file names like. Ex.
                # _1_file.txt , _1_file_1_.txt , file_1_.txt . you get 1_file.txt , 1_file_1.txt , file_1.txt , etc

                if nameInpList[-1] is '' and nameInpList[0] is '':
                    final_filename = '{}{}'.format(xReplaced[1:-1], extensions[x])
                # <x>...<x> >> x_..._x
                elif nameInpList[0] is '':
                    final_filename = '{}{}'.format(xReplaced[1:], extensions[x])
                # ...<x> >> ..._x
                elif nameInpList[-1] is '':
                     final_filename = '{}{}'.format(xReplaced[:-1], extensions[x])
                # <x>... >> x_...
                else: final_filename = '{}_{}{}'.format(x, nameInp, extensions[x])
                # if you didn't input name with any <x>, it'll add number at beginning, 1_file.txt

                os.rename(file, final_filename)
                print('INFO: changeName |', file, ':Renamed To:', final_filename)
                # renames the file
            x += 1
        updateFiles(os.getcwd())


### Button, treeview and layout ###


root = Tk()  # creates root window
root.geometry('1000x500')  # sets default window size, still resizable
root.title('Change File Names')  # sets window title

left = ttk.Frame(root)
left.pack(side=LEFT)
# creates left and right frames, right for data entry and other to see the files

inputDirLabel = ttk.Label(left, text='Path').pack()
# creates a label
chDirInput = ttk.Entry(left)
chDirInput.pack()
chDirInput.bind("<Return>", changeDir)
# a text entry, when press Enter it'll change Directory and print it's content


newNameInputText = ttk.Label(left, text='New Name').pack()
newNameInput = ttk.Entry(left)
newNameInput.pack()  # if you want to call or interact with an object later you can't use the .pack() on the object itself, has to be called after it's made
newNameInput.bind('<Return>', changeNames)
# entry box for new name

right = ttk.Frame(root)
right.pack(side=RIGHT, expand=True, fill=BOTH)
showFileWin = ttk.Treeview(right, columns=('oN', '_', 'nN'))  # original Name, -, New Name
# treeview, #| Original Name | _ | New Name
showFileWin.heading('#0', text='#')
showFileWin.column('#0', width=35, stretch=False)
# '#' column, change width, and won't stretch when changing window size
showFileWin.heading('oN', text='Original Files')
# Original file column
showFileWin.heading('_', text='>')
showFileWin.column('_', width=10, stretch=False)
# _ column only have >
showFileWin.heading('nN', text='New Files')
# New file name
showFileWin.bind('<Double-1>', goIntoDir)
# sets the heading text and the width for som eof them
showFileWin.pack(expand=True, fill=BOTH)
# fills and expands treeview so it fills right frame


bRight = Frame(right)
bRight.pack(side=BOTTOM, anchor=CENTER)
goUpDir = ttk.Button(bRight, text='Up', command=goUpDirectory).pack(side=LEFT)
# creates a back button, and it just goes up a directory

goBackDir = ttk.Button(bRight, text='Back', command=goBackDirectory).pack(side=LEFT)
# goes back to previous directory, not always up a parent just the previous dir were in

refreshButton = ttk.Button(bRight, text='Refresh', command=refresh).pack(side=LEFT)
# refreshes table to see output names before chaning them
changeFileButton = ttk.Button(left, text='Change Names', command=changeNames).pack()
chDirInput.insert(0, '/Users/drake/Desktop/test')
root.mainloop()
