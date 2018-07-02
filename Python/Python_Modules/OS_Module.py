import os
import time as t
from datetime import datetime as dt
def basics_Of_OS():
    # ------ Dirs/cwd -----
    cDir = os.getcwd()
    # gets the current working directory, put's it in cDIr
    print("Original dir:",cDir)

    os.chdir('/Users/drake') # changes directory, have to use full path can't use shortcuts like ~/ on a mac
    print("Moved dir:", os.getcwd()) # prints new dir path

    print(os.listdir())
    # lists the file/folder/etc in the current directory if don't give specific path
    # some IDEs might highlight a syntax error on os.listdir() , but it'll work just fine without a arg, it'll just printout the current dir


    # ----- Making -----
    os.chdir('/Users/drake/Desktop/Python')
    print("Current dir:", os.getcwd())

    # just moves to a python folder on desktop to play in
    print(os.listdir())

    os.mkdir("Folder")
    # makes folder in current dir Folder
    os.mkdir('/Users/drake/Desktop/Python/Folder2')
    # makes a folder Folder in specified path

    os.makedirs("upper/lower")
    # IF upper doesn't exist already it'll create it then create lower
    # DO NOT specify a whole path with this one, because it'll just create those folders in the current dir e.g. >
    # os.makedirs(Users/drake/Desktop/Python/upper/lowe) # this well make a Users folder and etc in the current dir, soooooo yeah, lol

    # for .makedirs() and .mkdir() if the folder already exists it'll crash the program, so you should probably use a if/else statment with .exists() to check if it's already there or not

    #t.sleep(5)
    # ----- Deleting -----
    # same as above with .makesdirs() and .mkdir()

    os.rmdir("Folder")
    os.rmdir("/Users/drake/Desktop/Python/Folder2")
    # same as .mkdir() but it deletes. and it'll also crash if it doesn't exist already, so if/else might be useful
    os.removedirs("upper/lower")
    # same as .makedirs() you can delete a folder hieracchy instead of just a folder, be extra careful with this one since you can delete a lot of stuff, same a .rmdirs() well crash if doesn't exists also
    # so I suggest you use .makesdirs() to make folders and .rmdirs() to delete folders for ease and safety

    # ----- if/else -----
    if not os._exists("Hello"): print("True")


    # ----- Renaming -----
    os.mkdir("Folder") # creates a folder
    os.rename("Folder", "AFolder")
    # renames Folder to AFolder, you do need the original name, and if Folder doesn't exist or already named that, it'll crash so if/else would be nice

    # A fun loop
    def rename_Loop():
        for i in range(99):
            t.sleep(5)

            if 'Kirby' in os.listdir():
                os.rename('Kirby', 'Drake')
                print("Renamed: Drake")
            t.sleep(5)
            if 'Drake' in os.listdir():
                os.rename('Drake', 'Kirby')
                print("Renamed: Kirby")


    # ----- Stats -----
    print(os.stat("AFolder")) # gets some data on a folder or a file
    # you can make it into a variable, or just print it
    mTime = os.stat("AFolder").st_size # this species to only get one thing about the file
    # usually you would put specific data into a var or something like that
    # mtime = modifaction time,
    # the time data well return in Unix time, so use datetime.datetime.fromtimestamp() to convert to human readable
    print("Modified Time of AFolder:", dt.fromtimestamp(mTime))
# learn some basics of OS

def more_Into_Dirs():
    os.chdir("/Users/drake/Desktop")
    print("Current Directory:", os.getcwd())
    def waking():
    # ----- walk() -----
        for dirpath, dirname, filename in os.walk(os.getcwd()):
            print("Current Path:", dirpath)
            print("Folders:", dirname)
            print("Files:", filename)
            print()


    print("Directory name:", os.path.dirname(os.getcwd()))
    # this well return the path to dst
    print("Base name:", os.path.basename(os.getcwd()))
    # this well only return the current location name, not the path
    print("Both:", os.path.split(os.getcwd()))
    # this well return the basename and dirname in a tuple

    print(os.environ)
    homeDir = os.environ.get("HOME")

    newFile = os.path.join(homeDir, 'Kirby.txt')
    # you should use .path.join() anytime you can, since paths might have missing / or some computers have // or some have \, and .path.join() takes care all of that for you

    # then you can use f = open(newFile, 'w') or with open(newFile, 'w'):
# more with directories with OS

def name_Changer():
    os.chdir("/Users/drake/Desktop/Python") # sets path of files
    print(os.getcwd()) # prints out current path, to make sure in correct dir

    for File in os.listdir(): # loops through each item in dir
        fileName, fileExt = os.path.splitext(File) # separates teh file name from its extension(.jpg) into a tuple, then puts it in the two vars
        if not fileName.startswith('.'): # makes sure it doesn't edit any hidden files. (yes python can see hidden files)
            file, name, extra, num = fileName.replace(' ', '').split('-')
            # replaces spaces in fileName with nothing then splits it by dashes then puts data in corresponding var, file = 'file', num = '1' etc

            num = num.zfill(2) # adds some padding to num, useful for sorting
            newFileName = str(num +' - ' + name + ' - ' + extra + fileExt)
            # the new name for the files

            os.rename(File, newFileName)
            print(""" "{}" --> "{}" """.format(File, newFileName))
name_Changer()