# only import all if you are using the module function A LOT, and it's the only main module you imported
from tkinter import *
import tkinter.messagebox as mb
# tkinter's message box modules
from tkinter import ttk
# widget themes. default is the defualt OS buttons and etc
# i would advicse using OS's style since it looks better, unless you are customizing

# root of window, other object/widget well be in root
root = Tk()
# new window
root.wm_title('My Program')
# sets program title
#iconImg = PhotoImage(file="Kirby.png")
# sets image variable
#root.tk.call('wm', 'iconphoto', root._w, iconImg)
# sets icon photo with iconImg

def func1(): print("This is a Function!")
# a test function for buttons and menu etc

def Basics():
    label = Label(root, text='Hello World!')
    # makes a label to show in root
    label.pack()
    # tells to pack the text wherever

def Buttons():

    ### Frame ###
    topFrame = Frame(root)
    topFrame.pack(side=TOP)
    # makes a frame on top


    bottomFrame = Frame(root)
    bottomFrame.pack(side=BOTTOM) # set frame position
    # makes a bottom frame

    ### Buttons ###
    button1 = Button(topFrame, text='1', fg='red') # red button with '1' as text
    button2 = Button(topFrame, text='2', fg='yellow') # yellow text button
    button3 = Button(topFrame, text='3', fg='blue')
    button4 = Button(topFrame, text='4', fg='cyan')
    # creates buttons
    # these well create the default tk buttons, for windows buttons look down
    button1.pack(side=LEFT)
    button2.pack(side=LEFT)
    button3.pack(side=LEFT)
    # these buttons well be in one row, and left to right
    button4.pack() # this well be on the bottom by it self
    # have to call pack for each button :(



    label2 = Label(root, text='Hello Friend', fg='red', bg='yellow')
    label2.pack(fill=X)
    # fills the bg color of label2 all of X axi, so in the row of label2 it'll all be yellow

    bot = Frame()
    ## Windows Buttons ##
    winB1 = ttk.Button(bottomFrame, text="Windows Button")
    winB2 = ttk.Button(bottomFrame, text="another Win Button")
    # creates buttons but with windows themed style
    winB1.pack()
    winB2.pack()
    # shows buttons

def moreButtons():
    button = ttk.Button(root, text='hi')
    # creates windows button
    photo = PhotoImage(file='Kirby.png')
    # gets image
    smallPhoto = photo.subsample(10,10)
    # down sizes it
    button.config(image=smallPhoto)
    # adds photo to button
    button.pack()
    button.state(['disabled'])
    # disables button
    print(button.instate(['!disabled']))
    # prints whether the button is not disabled(it's working)
    button.state(['!disabled'])
    # re-enables button, can not use ['enable']
    button.destroy()
    # destroys button
# more button stuff

def inputAndGrid():
    Name = Label(root, text="Name")
    Pass = Label(root, text="Pass")
    # creates labels for Name and Pass
    nameInp = Entry(root)
    passInp = Entry(root)
    # creates input boxes

    Name.grid(row=0, sticky=E)
    Pass.grid(row=1, sticky=E)
    # positions Name and Pass to a grid, with East(right) alignment

    nameInp.grid(row=0, column=1)
    passInp.grid(row=1, column=1)
    # puts the inputs to a grid also, right along the labels

    checkB = Checkbutton(root, text='Keep Logged In')
    # creactes checkbox with text Keep Logged In
    checkB.grid(columnspan=2)
    # positions to grid but with column span of 2, so it'll be in center
# entry() and grid()

def callFunc():

    def funcLeft(event):
        print("Hey you called this function!!!")
        print("1 + 1 = 2")
    # this function is for left click on button
    def funcRight(event):
        print("Hey another Function!!!!")
        print("2 + 2 = 4")
    # function for right click
    def funcMid(event):
        print("AND ANOTHER!")
        print("4 + 4 = 8")
    # middle click or mouse wheel
    # create functions too call for button

    button = Button(root, text='Call Function')
    # creates button
    button.bind("<Button-1>", funcLeft)
    # binds button to function when left click
    button.bind("<Button-3>", funcRight)
    # binds button to another function for right click
    button.bind("<Button-2>", funcMid)
    button.pack()
    # shows button
# button calling function

def getInfo():
    label = Label(root, text="Input Something")
    # new label
    label.grid(row=0)
    # puts on grid row 0

    usrInp = StringVar()
    # label
    inp = Entry(root)
    inp.grid(row=0, column=1)
    # entry box


    def getInp(event):
        print(usrInp)

    get = Button(root, text="Get Inputted")
    get.bind("<Button-1>", getInp)
    get.grid(row=1, columnspan=2)
# get input

class TK:
    def __init__(self, master):
        frame = Frame(master)
        # creates init instance
        frame.pack()

        self.print = Button(frame, text='Soemthing', command=self.printSomething)
        self.print.pack(side=LEFT)
        # does everything the same but in a class instance

        self.quit = Button(frame, text='Quit', command=frame.quit)
        self.quit.pack(side=RIGHT)

    def printSomething(self): print("This is SOMETHING!")
# class methods and functions

def Menus():

    def doSomething(): print("FUNCTION FUNCTION FUNCTION!!!")
    # test function to do something

    mainM = Menu(root)
    # creates a menu, this well be te strip and you can add cascading menus to it, e.g. File, Edit, Help, Tools, etc
    root.config(menu=mainM)
    # tells TK that mainM is a menu thingy

    subM = Menu(mainM)
    # creates a submenu
    mainM.add_cascade(label="FILE!!", menu=subM)
    # adds the subM item to the mainM
    subM.add_command(label='DO SOMETHING!', command=doSomething)
    # adds a action to subM which is under FILE!! in mainM
    subM.add_separator()
    # creates a line separator in submenu FILE!!
    subM.add_command(label='QUIT!!!', command=quit)
    # adds a quit button that quits the window, under the new separator under FILE!! under mainM
# menu bars, File, Edit, Help, View, etc

def ToolbarAndStatusB():

    toolBar = Frame(root)
    # new frame
    toolBar.config(bg='black')
    # frame background black

    insertImg = Button(toolBar, text='Insert Image', command=func1)
    # new button
    insertImg.pack(side=LEFT, padx=2, pady=2)
    # some padding for button
    toolBar.pack(side=TOP, fill=X)
    # makes frame fill the whole row



    status = Label(root, text="SOMETHING......", bd=1, relief=SUNKEN, anchor=W)
    # makes status bar, but only static text for now.
    # bd is border, relief adds a sunken border. anchor anchors the text to the west(right)
    status.config(bg='brown')
    # colors background of label
    status.pack(side=BOTTOM, fill=X)
    # positions to bottom, and fills all of bottom X axi
# toolbar actions, and status bar at bottom

def msBox():

    mb.showinfo("HI!", 'This is a friendly message.')
    # pops up a regular windows/mac message box. defualt is the blue i and OK button
    answer = mb.askquestion('Question', 'Liked the message?')
    # asks a Yes/No question, and saves the boolean answer in answer

    if answer == True: print("Thank You")
    else: print("I don't like you either!")
    # if/else statement base off the answer boolean
# OK message boxes

def canVas():
    canvas = Canvas(root, width=400, height=200)
    # creates canvas x by y pixels
    canvas.pack() # shows canvas

    blackLine = canvas.create_line(0,0, 200, 50, fill='red')
    # creates a red line starting 0x0 end 200x50  pixel coords
    Box = canvas.create_rectangle(10,20,100,100, fill='green')
    # makes a green box, upper-left corner 10x20, lower-left corner 100x100
# drawing shapes

def phoTo():
    photo = PhotoImage(file='Kirby.png')
    # opens up photo and stores in variable, kinda like f=open('file','r') but with photos
    photoLabel = Label(root, text='Kirby!!',image=photo)
    # creates a normal label but with image
    photoLabel.pack()
    root.config(background='#4286f4')
    # sets root window background to blue
# show images

def checkBoxs():
    cBoxVar = IntVar()
    # cBox Variable, saves cBox's variable state of checked/un-checked
    cBoxAns.get()
    # cBox Answer, gets the data
    def sayHi():
        if cBoxAns == 1: print("yay you checked it")
        # checkes whether you checked yes/no, 1 for yes, 0 for no
        else: print("boo you didn't check it")
        # if you didn't it prints out this
    # function that does different things if cBox is checked or not

    cBox = ttk.Checkbutton(root, text='Check Me', variable=checked, command=hi).grid(row=0, columnspan=2)
    # checkBox, creates check box, and when it is interacted with it calls sayHI, which well respond accordingly


    def textYN():
        answer = cBox2Var.get()
        # puts cBox2Var data into a simple variable. needs to be in the function so the variable can update when checkbox updates
        if answer == 1: ttk.Label(root, text='Yay Chcked').grid(row=3, columnspan=2)
        # makes a label that prints this out if cBox2 is checked
        else: ttk.Label(root, text='BOO YOU').grid(row=3, columnspan=2)
        # else.....


    cBox2 = ttk.Checkbutton(root, text='CHECK ME!!!', variable=checked2, command=textYN).grid(row=1, columnspan=2)
    # checkBox2. a new check box that well make update a label whether it's checked or not
# shows how to update text if check box are ticked or not

def lambdaCallback():

    def function(arg):
        print('You pressed', arg)
    # prints out "You pressed" + button number pressed

    B1 = ttk.Button(root, text="Button 1", command=lambda: function('Button 1')).pack()
    B2 = ttk.Button(root, text="Button 2", command=lambda: function('Button 2')).pack()
    B3 = ttk.Button(root, text="Button 3", command=lambda: function('Button 3')).pack()
    # you call the function with argument in a lambda.
    # if it gives you an lambda error about lmabda takes 0 args, just add one. e.g.
    # command = lambda e: function('hi')
    #                  ^

    # you can of course make a small lambda function right then and there

    # You CAN'T do this. this code won't work correctly. it'll still run though
    B4 = ttk.Button(root, text="This won't work", command=function("it's a bad button")).pack()
    # when you run this, it'll show the button, but call the function("it's a bad button"). the button won't work if you try to click on it.
# shows how to do a call back that needs arguments

def keyboardActions(): pass

def drawCanvas():

    C = Canvas(root, width=640, height=480, background='black')
    C.pack()

    def mouse_press(event):
        global prev # global prev
        prev = event
        print("Event Type: {}".format(event.type))
        # gets event type. 2 = Keyboard.  4 = Mouse
        print("Current Frame: {}".format(event.widget))
        # gets widget that is being interacted with
        print("Mouse Button: {}".format(event.num))
        # gets mouse button being pressed. 1 = left. 2 = middle. 3 = right
        print("Frame X: {}".format(event.x))
        print("Frame Y: {}".format(event.y))
        # gets x/y coords, but only in relation in teh canvas frame
        print("Screen X: {}".format(event.x_root))
        print("Screen Y: {}".format(event.y_root))
        # gets x/y coords in relation to whole screen(includes outside of frame and root)
        print('\n')

    if __name__ == '__main__':
        def draw(event):
            global prev # gets prev
            C.create_line(prev.x, prev.y, event.x, event.y, width=2, fill='white')
            # draws line from previous mouse coords to new ones, draws white line with thickness 2
            prev = event # updates previous coores
            # if you disable(comment out) this part, you get a cool affect. you hold you mouse down and move around the screen, and it looks like a fan


    C.bind('<ButtonPress>', mouse_press)
    C.bind('<B1-Motion>', draw)
# super simple drawing program, black bg and white paint

def scrollBar():
    text = Text(root, wrap='none') # new text field

    yScroller = ttk.Scrollbar(root, orient=VERTICAL, command=text.yview)
    # y scrollbar. makes a new Vertical scrollbar, and it links(commands) to text field
    xScroller = ttk.Scrollbar(root, orient=HORIZONTAL, command=text.xview)
    # x scrollbar. horizontal scrollbar

    yScroller.pack(side=RIGHT, fill=BOTH)
    # maps to right side of frame, fills on y
    xScroller.pack(side=BOTTOM, fill=X)
    # maps x scroll bar to the bottom
    text.pack(side=LEFT,expand=True, fill=BOTH)
    # most of the grid well be taken up by text field. make sure to have expand=True, if not the scrollbars well

    # puts scrollbar on grid, to the right of text, and sticks there.
    text.config(yscrollcommand=yScroller.set, xscrollcommand=xScroller.set)
    # have text to tell scrollbar where current position is, so the scrollbar can show visually
# scrollbars

def myBind():
    inp = ttk.Entry(root)
    # new entry box
    inp.pack()
    # use pack() on new line so you can call inp later on

    def odd(x): print("Odd Number!!!")
    def even(x): print("Even Number!!")
    # simple functions to print odd or even

    inp.event_add("<<odd>>", '1','3','5','7','9')
    # new virtual event, ('<<newName>>', 'triggers')
    inp.event_add("<<even>>", '0','2','4','6','8')
    # only gets triggered on odd number inputs

    inp.bind("<<odd>>", odd)
    inp.bind("<<even>>", even)
    # bind both events to inp
# make custom virtual event binds

class Survey:

    def __init__(self):
    # initialize the frames

    ### Main Frames ###
        self.headerFrame = Frame(root)
        # header frame with info about survey

        self.inputFrame = Frame(root)
        # lower field for data input

        self.headerFrame.pack(side=TOP)
        self.inputFrame.pack(side=BOTTOM)

    ## Header Data ##
        # Image #
        self.logoFile = PhotoImage(file='Kirby.png').subsample(2,2)
        self.companyLogo = ttk.Label(self.headerFrame, image=self.logoFile).grid(row=0, column=0, rowspan=2)

    # Header Text #
        self.welcomeHeader = Label(self.headerFrame, text="Kirby Survey",
                                        font=('verdana',18,'bold')).grid(row=0, column=1)
                                        # special font so it's bigger.
        self.extraHeaderText = Label(self.headerFrame, text="Thank you for taking this survey today").grid(row=1, column=1)
        # creates text and shows on grid. don't have to call grid() on new line since I well not be calling back to it for anything.

    # starts functions
        self.userInteract()

    def userInteract(self):
    # input fields, and text

    # Text #
        self.nameText = Label(self.inputFrame, text='Name:').grid(row=0, column=0, padx=5)
        self.emailText = Label(self.inputFrame, text='Email:').grid(row=0, column=1, padx=5)
        self.commentText = Label(self.inputFrame, text='Comments:').grid(row=2, column=0, padx=5, pady=10, columnspan=2)
        # name, email and comments title text labels. again call grid() on same line since don't need to call it again.

    # input fields #
        self.inputName = ttk.Entry(self.inputFrame)# textvariable=self.nameData)
        self.inputEmail = ttk.Entry(self.inputFrame)# textvariable=self.emailData) # puts data into variables so you can get them later
        self.inputComment = Text(self.inputFrame, bg='#b2b0b0', width=60, height=20) # changes background color, because Text() has no border

        self.inputName.grid(row=1, column=0, padx=5)
        self.inputEmail.grid(row=1, column=1, padx=5)
        self.inputComment.grid(row=3, column=0, padx=5, columnspan=2) # changes columnspan so it's centered.
        # here I do need to call grid() separately so I can call the input fields to get the data later with .get()

    # Submit and Clear buttons
        self.submitButton = ttk.Button(self.inputFrame, text='Submit', command=self.submitData).grid(row=4, column=0, pady=25)
        self.clearButton = ttk.Button(self.inputFrame, text='Clear', command=self.clearEntries).grid(row=4, column=1, pady=25)

    def submitData(self):
    # submit data, print to console and clear out from GUI, and let user know it has been submitted

        mb.showinfo("Done", "Your survey has been submitted. Thank You")
        # brings dialog saying Done and Thank you
        print("::User Data::")
        print("Name: {}".format(self.inputName.get()))
        print("Email:", self.inputEmail.get())
        print("Comment:", self.inputComment.get('1.0','end'))
        # prints out data, calls function to return data to print
        print("Thank You for taking this short survey!")
        quit()
        # quits program after click OK

    def clearEntries(self):
    # clears all input box data
        clearYesNo = mb.askyesno("Clear?", "Are you sure you want to clear?")
        # asks yes no if you want to clear fields
        if clearYesNo == True:
        # if click Yes
            self.inputName.delete('0', 'end')
            self.inputEmail.delete('0', 'end')
            self.inputComment.delete('1.0', 'end')
            # deletes all data in fields
            print("Cleared Fields.")
            # prints out that it's done

def runSurvey():
    print("Starting Survey...\nDone.")
    ins = Survey()
    # makes new instance
    root.resizable(False,False)
    root.mainloop()
    # opens window

def messageBoxes():
    # tk common message boxes
    #
    # this module provides an interface to the native message boxes
    # available in Tk 4.2 and newer.
    #
    # written by Fredrik Lundh, May 1997
    #

    #
    # options (all have default values):
    #
    # - default: which button to make default (one of the reply codes)
    #
    # - icon: which icon to display (see below)
    #
    # - message: the message to display
    #
    # - parent: which window to place the dialog on top of
    #
    # - title: dialog title
    #
    # - type: dialog type; that is, which buttons to display (see below)
    #

    from tkinter.commondialog import Dialog

    #
    # constants

    # icons
    ERROR = "error"
    INFO = "info"
    QUESTION = "question"
    WARNING = "warning"

    # types
    ABORTRETRYIGNORE = "abortretryignore"
    OK = "ok"
    OKCANCEL = "okcancel"
    RETRYCANCEL = "retrycancel"
    YESNO = "yesno"
    YESNOCANCEL = "yesnocancel"

    # replies
    ABORT = "abort"
    RETRY = "retry"
    IGNORE = "ignore"
    OK = "ok"
    CANCEL = "cancel"
    YES = "yes"
    NO = "no"

    #
    # message dialog class

    class Message(Dialog):
        "A message box"

        command = "tk_messageBox"

    #
    # convenience stuff

    # Rename _icon and _type options to allow overriding them in options
    def _show(title=None, message=None, _icon=None, _type=None, **options):
        if _icon and "icon" not in options:    options["icon"] = _icon
        if _type and "type" not in options:    options["type"] = _type
        if title:   options["title"] = title
        if message: options["message"] = message
        res = Message(**options).show()
        # In some Tcl installations, yes/no is converted into a boolean.
        if isinstance(res, bool):
            if res:
                return YES
            return NO
        # In others we get a Tcl_Obj.
        return str(res)

    def showinfo(title=None, message=None, **options):
        "Show an info message"
        return _show(title, message, INFO, OK, **options)

    def showwarning(title=None, message=None, **options):
        "Show a warning message"
        return _show(title, message, WARNING, OK, **options)

    def showerror(title=None, message=None, **options):
        "Show an error message"
        return _show(title, message, ERROR, OK, **options)

    def askquestion(title=None, message=None, **options):
        "Ask a question"
        return _show(title, message, QUESTION, YESNO, **options)

    def askokcancel(title=None, message=None, **options):
        "Ask if operation should proceed; return true if the answer is ok"
        s = _show(title, message, QUESTION, OKCANCEL, **options)
        return s == OK

    def askyesno(title=None, message=None, **options):
        "Ask a question; return true if the answer is yes"
        s = _show(title, message, QUESTION, YESNO, **options)
        return s == YES

    def askyesnocancel(title=None, message=None, **options):
        "Ask a question; return true if the answer is yes, None if cancelled."
        s = _show(title, message, QUESTION, YESNOCANCEL, **options)
        # s might be a Tcl index object, so convert it to a string
        s = str(s)
        if s == CANCEL:
            return None
        return s == YES

    def askretrycancel(title=None, message=None, **options):
        "Ask if operation should be retried; return true if the answer is yes"
        s = _show(title, message, WARNING, RETRYCANCEL, **options)
        return s == RETRY

    # --------------------------------------------------------------------
    # test stuff

    if __name__ == "__main__":
        print("info", showinfo("Spam", "Egg Information"))
        print("warning", showwarning("Spam", "Egg Warning"))
        print("error", showerror("Spam", "Egg Alert"))
        print("question", askquestion("Spam", "Question?"))
        print("proceed", askokcancel("Spam", "Proceed?"))
        print("yes/no", askyesno("Spam", "Got it?"))
        print("yes/no/cancel", askyesnocancel("Spam", "Want it?"))
        print("try again", askretrycancel("Spam", "Try again?"))

if __name__ == '__main__':
    runSurvey()