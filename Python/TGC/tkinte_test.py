from tkinter import *
from os import *
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        self.increase_button = Button(self)
        self.increase_button["text"] = "Increase"
        self.increase_button["command"] = self.increase_value
        self.increase_button.pack(side="right")

        self.increase_button = Button(self)
        self.increase_button["text"] = "Decrease"
        self.increase_button["command"] = self.decrease_value
        self.increase_button.pack(side="left")

        self.increase_button = Button(self)
        self.increase_button["text"] = "pwd"
        self.increase_button["command"] = self.doSomething
        self.increase_button.pack(side="bottom")
    def doSomething(self):
        print(system('pwd'))


    def increase_value(self):
        global mainval
        mainval *= 2
        print(mainval)
    def decrease_value(self):
        global mainval
        mainval /= 2
        print(mainval)

mainval = 1.0

root = Tk()
app = Application(master=root)
app.mainloop()


