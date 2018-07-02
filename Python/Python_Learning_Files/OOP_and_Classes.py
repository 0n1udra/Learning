# go to Advance.py or Basic Concepts.py for some more on Classes
# This is all from Corey Schafer's YouTube Python OOP section in Python Tutorials
# ----- Terminology and Methods and etc-----
"""
--- Vocab/Glossary ---
Methods  --  a function that is related or in a class. class.classmethod() . x = 'hi' x.isalpha()  that's also a method
Attribute  --
class  --
instance
Instantiate
Method Resolution Order  --  this is the order python uses to look for data from inherited classes and stuff, use print(help()) to see order and more data

--- Class Methods/Dunders/etc ---
@classmethod  --  a method to do stuff with the class. But not needing an instance. Does have to be in class
@staticmethod  --  a method that doesn't rely on the class or any instance of it at all, just for readability sake and understandability. So like if it has a connection to the class

These are sometimes call Magic or Dunder methods
__init__  --  runs every time you create a instance of a class
__repr__  --  set what to show when print out a instance, usually used for debugging and other coders to see
__str__  --  returns string representation for user
__call__
"""

from datetime import date as d
def newL(str):
    print('-' * 10, str, '-' * 10)

# SHOULD NOT BE RUNNED IN  functions!, so remove function and un-indent everything

# ----- Basics -----
def Basics():
    newL('Employee')


    # creating a class and creating instance data after instance
    class Employee:
        pass

    # a blank class
    emp1 = Employee()
    emp2 = Employee()
    print(emp1, '\n', emp2)
    # this well print out the memory location of the instances of the class Employee

    emp1.name = 'Drake'
    emp1.age = 16
    emp1.mood = 'meh'

    emp2.name = 'Kirby'
    emp2.age = 10
    emp2.mood = 'Happy'

    print(emp1.name)
    print(emp1.age)
    print(emp1.mood)
    # print newly set data from emp1

    print(emp2.name)
    print(emp2.age)
    print(emp2.mood)
    # prints data from emp2


    # Passing in data to class instance when making class instance
    newL('Employee2')


    class Employee2:
        def __init__(self, name, age, mood):
            self.name = name
            self.age = age
            self.mood = mood


    emp1_1 = Employee2('Drake', 16, 'meh')
    emp2_1 = Employee2('Kirby', 10, 'Happy')

    print(emp1.name)
    print(emp1.age)
    print(emp1.mood)

    print(emp2.name)
    print(emp2.age)
    print(emp2.mood)

    # Same as Employee2 to pass in data, but use repr to print out data. Instead of using print over and over again
    newL('Employee3')


    class Employee3:
        def __init__(self, name, age, mood):
            self.name = name
            self.age = age
            self.mood = mood

        def __str__(self):
            # need self as a param, since when calling any class method(including the __ ones) the instance is passed
            # into the method by default
            return 'Info: {} {} {}'.format(self.name, self.age, self.mood)


    emp1_2 = Employee3('Drake', 16, 'meh')
    emp2_2 = Employee3('Kirby', 10, 'Happy')

    print(emp1_2)
    print(emp2_2)

    # Using class without (self)
    newL('Ex1')  # Example class


    class Ex1:
        def __init__(self, name):
            # you need self here
            self.name = name

        def func1(self): print("Hello", self.name)


    Ex1('Kirby').func1()
    # this creates a instance then runs a function, but you can't use instance again later.
    test1 = Ex1('Drake').func1()
    # this still won't let you call the test1 instance later
    test2 = Ex1("Rhino")
    # now you can call test2 over and over again
    Ex1.func1(test2)  # calls Ex1's func1 and passes the test2 instance of it, same as >
    test2.func1()
# basics of classes

def instVar_vs_classVar():
# Instance variable vs class variable, and some kwargs and default kwargs
    class Employee:
        RaiseAmount = 1.04  # default raise amount for when call pay_Raise()
        NumOfEmps = 0  # keeps track of number of Employees

        def __init__(self, name, last, age, pay=10_000, mood='OK'):
            # as you can see you can have default kwargs, but they should go last
            # you can also see here 10_000 has _ , that's so it's easier to see, 10,000 not allows. this works anywhere
            self.name, self.last = name, last
            self.age = age
            self.mood = mood
            self.pay = pay
            self.email = "{}.{}@Kmail.com".format(name, last)
            # this just combines the first and last names together to make an email

            Employee.NumOfEmps += 1  # this well add one each time init runs(every time a new employee is made)
            # since we don't want to edit/change with this var we don't have to use self

        def __str__(self):
            # need self as a param, since when calling any class method(including the __ ones) the instance is passed
            # into the method by default
            return 'Info: {} {} ${:,}'.format(self.name, self.age, self.pay)

        def Pay_Raise(self): self.pay *= self.RaiseAmount # need self to call a class var

    Kirby = Employee(name='Kirby', last='', age=10)  # you can pass in data in order or use kwargs like this
    Drake = Employee('Drake', 'Thomas', 16, mood='Uhg', pay=9_000)  # you can mix it up with regular args or kwargs

    print("Info on Kirby:", Kirby)
    print("Info on Drake:", Drake.__dict__)  # this is a attribute not a method, so it doesn't have the ()
    # shows all attributes about this employee, with __dict_-
    print("Kirby's pay:", Kirby.pay)
    print("Drake's pay:", Drake.pay)

    Employee.RaiseAmount = 1.06  # changes raise amount for everybody
    # you won't see this in any of the __dict__ for the instances but it'll be in the class __dict__
    print(Employee.__dict__)  # you'll see 'RaiseAmount': 1.06, since it affects everybody (if you call pay_Raise())
    print(Kirby.__dict__)  # you won't see the RaiseAmount in here

    Kirby.RaiseAmount = 1.065  # only changes Kirby raise amount
    print(Kirby.__dict__)  # but now you well see the RaiseAmount attr in this dict, since you changed it for Kirby specifiably
    # you could also just use a default kwarg in pay_Raise (raise=1.04) , then if you want to change it for a specific employee just change the var when calling it
# instance variables and class variables

def classMethod_staticMethod():
# What's a @classmethod or a @staticmethod

    class Employee:
        # most of the comments are taken out to save space and tidy things up, if you want to see what this does go to the before stuff, since it's just a copy of that with stuff taken out
        NumOfEmps = 0
        RaiseAmount = 1.0

        def __init__(self, name, last, pay=10_000):
            self.name, self.last = name, last
            self.pay = pay

        def __str__(self): return "{} {}. ${:,}".format(self.name, self.last, self.pay)

        def Pay_Raise(self): self.pay *= self.RaiseAmount

        @classmethod
        def Set_Pay_Raise(cls, amount):
            # cls is for class, since your changing class objects

            cls.RaiseAmount = amount

        @classmethod
        def String_Intake(cls, string):
            name, last, pay = string.split('-')
            # splits string into variables into name last name and pay from the string splitted by -
            return cls(name, last, int(pay))
            # creates a new instance or employee from data.

            # so it gets the data from string, then creates a new employee. and since this is a classmethod you don't need an instance already-
            # which makes since, Since you're trying to make a new employee duh. You could do this outside of class, but this better

        @staticmethod  # a static method. This well run just fine outside the class, but it has a logical connection to this class
        def Is_Work_Day():
            if d.weekday(d.today()) < 5:  # checks whether it's a weekday or a weekend
                print("It's work day!!")
        # this just checks if it's a workday or not

    Employee.Set_Pay_Raise(1.05)  # calls Set_Pay_Raise, to set RaiseAmount. As you can see don't need an class instance with Employee()
    Kirby = Employee(name='Kirby', last='', pay=10_000)  # create a employee

    Drake = 'Drake-Thomas-9_000'  # a string with employee info separated by -
    Drake = Employee.String_Intake(Drake)  # creates a new Employee from the string
    print(Kirby)
    print(Drake)
    Employee.Is_Work_Day()
    # runs function. Don't need an instance, if you do create an instance you'll have to create a new employee
# @classmethod and @staticmethod

def Inherit():
    class Employee:
        RaiseAmount = 1.04

        def __init__(self, name, last, pay):
            self.name, self.last = name, last
            self.pay = pay
            self.fName = "{} {}".format(self.name, self.last)  # sets full name from name and last

        def __str__(self): return "{}. ${:,}".format(self.fName, self.pay)

        def Pay_Raise(self): self.pay *= self.RaiseAmount
        # sets raise for a regular employee

    class Coder(Employee):
        RaiseAmount = 1.10

        def __init__(self, name, last, pay, level, lang):
            super().__init__(name, last, pay)
            self.lang = lang
            self.level = level

        def __str__(self):
            return "{}. Language: {} - Experience: {}".format(self.fName, self.lang, self.level)
            # a new repr for Coders, if you don't have this it'll just use the Employee one. So create a new one to show different info

    # Coder inherited from Employee so that means it has everything(attrs, var, funcs) from Employee, even the init

    class HTML_Coder(Coder, Employee): pass

    class HR(Employee):
        RaiseAmount = 1.11

        def __init__(self, name, last, pay, nice, exp):
            super().__init__(name, last, pay)
            self.nice = nice
            self.exp = exp

        def __str__(self): return "{}. How nice {}. Experience {}".format(self.fName, self.nice, self.exp)


    class Manager(Employee):
        RaiseAmount = 1.09

        def __init__(self, name, last, pay, *employees):
            super().__init__(name, last, pay)

            if not employees: self.employees = []
            else: self.Add_Emp(employees)
            # checks whether you added some employees or not, if you did it'll call the Add_Emps to add them

        def Add_Emp(self, *employees):
            for emp in employees:
                try: self.employees.append(emp)
                except: print("Failed To Add Employee")
            # goes through the list and adds them to employees list

        def Del_Emp(self, employee):
            try: self.employees.remove(employee)
            except: print("Failed To Remove Employee")

        def Print_Emps(self):
            print(self.name, ":Employees:")
            for emp in self.employees:
                print(emp)
            print("-----")
            # prints employee info one by one, uses the Employee __repr__


    Drake = Coder('Drake', 'Thomas', 10_000, 1, 'Python')
    # since Coder inhered from Employee, you can create a new instance and pass in data like you would with Employee()
    Kirby = HR('Kirby', '', 10_000, 10, 8)  # same here with Kirby but with HR

    print(help(HR))  # prints data about stuff, really useful

    print(Drake)
    print(Kirby)

    # --- Pay_Raise ---
    print("Drake Before Raise: {:,}".format(Drake.pay))
    print("Kirby Before Raise: {:,}".format(Kirby.pay))
    # shows pay before raise
    Drake.Pay_Raise()
    Kirby.Pay_Raise()
    # runs Pay_Raise, but the RaiseAmount is different since it's changed in Coder and HR class
    print("Drake After Raise: {:,}".format(Drake.pay))
    print("Kirby After Raise: {:,}".format(Kirby.pay))
    # shows pay after raise

    # --- Manager ---
    Sleepy = Employee("Z", '', 9_000)
    Rhino = Employee("Rhino", "Virus", 9_000)
    Bob = Employee("Bob", "Doe", 8_000)
    # creates some employees
    Emoji = Manager("Shades", '', 10_000)
    # creates a manager
    Emoji.Add_Emp(*[Sleepy, Rhino])
    # adds employees to Emoji's list of employees, one by one
    Emoji.Del_Emp(Bob)
    # removes Bob from Emoji's emoployee
    Emoji.Print_Emps()  # prints Emoji's employees
# class inheritance

def isInst_isSub():
# checks if instance of a class or a subclass of a class
    class Test: pass
    class Sub_Test(Test): pass

    x1 = Test()
    x2 = 'hi'

    print(isinstance(x1, Test))
    # prints bool if x1 is a instance of Test
    print(isinstance(x2, Test))

    print(issubclass(Sub_Test, Test))
    # prints bool if Sub_Test is a child class of Test
# isinstance() and issubclass()

def Duners():
# Special Methods in classes are called Magic Methods or Dunders
    class Employee:
        RaiseAmount = 1.04

        def __init__(self, name, last, pay):
            self.name, self.last = name, last
            self.pay = pay
            self.fName = "{} {}".format(self.name, self.last)  # sets full name from name and last

        def __repr__(self):
            return f"Employee({self.name}, {self.last}, {self.pay})"

        def __str__(self):
            return "Name: {} | Pay: ${:,}".format(self.fName, self.pay)

        def __add__(self, other):
            return "{:,}".format(self.pay + other.pay)
            # adds together employees pay

        def __sub__(self, other):
            raise NotImplemented
        # NotImplemented well go and see if any of the other Dunders can handle the operation if this one can't

        def __mul__(self, other): pass

        def __mod__(self, other): pass

        def __pow__(self, power, modulo=None): pass

        def __abs__(self): pass

        def __len__(self): return len(self.fName)
        # returns character length of first and last name. Including the space between name

        # you can also do __str__ = func()  so that when __str__ is called func() well run instead

    Kirby = Employee('Kirby', '', 10_000)
    Drake = Employee('Drake', 'Thomas', 10_000)

    # Dunder repr
    print(Kirby)
    print(Drake)

    print()
    # Dunder str
    print(repr(Kirby))  # this basically calls __repr__ from the class same as >
    print(Kirby.__repr__())  # this is what the above repr() is doing

    print(str(Drake))  # same here but with str
    print(Drake.__str__())

    # ----- Other Dunders -----
    # __add__
    print(Kirby + Drake)
    # the + tells python to call the __add__ Duner in the Employee class same as >
    print(Employee.__add__(Kirby, Drake))
    # if you didn't have the __add__ in the class, this would crash the program. since Python doesn't know how to add object like these

    # __len__
    print(len(Kirby))
    print(len(Drake))
    # this well return the char length of first and last name
# __str__ / __len__ / __add__

def property_Setter():
    class Employee:
        def __init__(self, first, last, mood):
            self.first, self.last = first, last
            self.mood = mood
            self.fullName = self.first, self.last

        @property
        def fName(self): return "{} {}".format(self.first, self.last)
        # gets full name function

        @fName.setter
        def fName(self, newName): self.first, self.last = newName.split(' ')
        # takes the newName string and splits it by the space, then updates the first and last names
        # the @fName.setter allows it so you can do x.fName = 'first last' . since fName is actually a function
        # but it'll call this when it sees the = sign

        @fName.deleter
        def fName(self): self.first = self.last = '_'

        @property
        def email(self): return "{}.{}@Kmail.com".format(self.first, self.last)
        # gets email addr

        @property
        def cMood(self): return "{} is very {} right now.".format(self.first, self.mood)



    emp1 = Employee('Drake', 'Thomas', 'meh')  # create new Employee

    print(emp1.email)  # this looks like it's getting a attribute, but it's actually calling a function. It has return so print() is used here

    print(emp1.cMood)  # prints mood
    emp1.mood = 'Happy'  # changes mood
    print(emp1.cMood)  # prints new mood

    print(emp1.fName)  # prints full name, don't need () since fName has @property
    emp1.fName = "Shades Emoji"  # updates name, first and last name
    print(emp1.fName)  # prints new name
    print(emp1.email)  # prints new email

    del(emp1.fName)  # deletes full name
    print(emp1.fName)  # prints deleted name, since I set the deleted name to _ to show it, irl you might want it empty or something else
    print(emp1.mood)  # shows mood, since mood was not affected
    # you could do del(first/last)  to actually delete the variable. It won't remove the name it'll delete the names variables
    del(emp1.first)
    del(emp1.last)
    print(emp1.fName)  # this well give error since you deleted first and last name variables
# @propety and @x.setter and x.deleter. @property well have function treated as a attribute > classInst.getName  vs classInst.getName()




