# Drake Thomas

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import os
import logging

# Currently only works on Mac OS

class File_System:
    def __init__(self, path='~/Desktop'):
        print("Current directory:", os.getcwd())

    # Changes directory from input in entry box
    def change_Dir(self, path):
        try:
            # Go into directory
            os.chdir(path)
        except OSError:
            print(f"Error: {path} not accessible")
        else:
            print("Current directory now:", os.getcwd())
            return os.getcwd()

    def go_To_Parent(self):
        try:
            # Gets the parent directory using current from splitting by /
            os.chdir('/'.join(os.getcwd().split('/')[:-1]))
        except OSError:
            print("Error: Can't go to parent directory")
        else:
            print("Current Directory now:", os.getcwd())
            return os.getcwd()

    def rename_File(self, file, rename):
        try:
            os.rename(file, rename)
        except OSError:
            print(f"Error: Can't rename {file} to {rename}")
        else:
            print(f"Renamed: {file} > {final_filename}")

    def __str__(self):
        return "Current location:", os.getcwd()

class Renaming_Window:
    def __init__(self, master, file_sys):
        self.master = master
        master.geometry('1000x500')
        master.title('Change File Names')

        # Setup left frame
        left = ttk.Frame(master)
        left.pack(side=tk.LEFT)

        # Path entry box and Label. Binds Enter
        ttk.Label(left, text='Path').pack()
        self.change_dir_box = ttk.Entry(left)
        self.change_dir_box.pack()
        self.change_dir_box.bind("<Return>", self.change_Dir_Entry)

        # Rename entry Box and Label
        ttk.Label(left, text='Rename').pack()
        self.rename_box = ttk.Entry(left)
        self.rename_box.pack()

        # Setup right frame
        right = ttk.Frame(master)
        right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        # treeview column
        self.show_file_win = ttk.Treeview(right, columns=('files'), show='headings')

        # Files column
        self.show_file_win.heading('files', text='Files')

        # Double click a directory to enter
        self.show_file_win.bind('<Double-1>', self.go_Into_Dir)

        # Fills and expands treeview so it fills right frame correctly
        self.show_file_win.pack(expand=True, fill=tk.BOTH)

        # Bottom right frame
        bottom_right = tk.Frame(right)
        bottom_right.pack(side=tk.BOTTOM, anchor=tk.CENTER)

        # Go up a directory (parent directory)
        ttk.Button(bottom_right, text="Up a Directory", command=self.go_Up_Directory).pack(side=tk.LEFT)

        # Refreshes table
        ttk.Button(bottom_right, text='Refresh', command=self.update_Files()).pack(side=tk.LEFT)
        ttk.Button(left, text='Change Names', command=self.change_Name).pack()

    def change_Name(self):
        make_sure = mb.askyesno('Change Names',  'Are you sure you want to rename these files?')

        name_inp = self.rename_box.get()

        if make_sure and name_inp:
            x = 0
            for file in os.listdir():
                # Don't edit hidden linux files
                if file.startswith('.'): continue

                if "<x>" in name_inp:
                    new_filename = name_inp.replace("<x>", f"_{x}_")

                    # Checks where <x> in the rename box so you don't get file names like. Ex.
                    # _1_file.txt , _1_file_1_.txt , file_1_.txt . you get 1_file.txt , 1_file_1.txt , file_1.txt , etc

                    # <x>filename<x> >> x_filename_x
                    if new_filename[-1] == '_' and new_filename[0] == '_':
                        final_filename = new_filename[1:-1]
                    # filename<x> >> filename_x
                    elif new_filename[0] == '_':
                        final_filename = new_filename[1:]
                    # <x>filename >> x_filename.
                    elif new_filename[-1] == '_':
                        final_filename = new_filename[:-1]
                    else:
                        final_filename = new_filename
                else:
                    final_filename = name_inp
                x += 1

                final_filename = final_filename + '.' + ''.join(file.split('.')[1:])
                file_sys.rename_File(file, final_filename)

            self.update_Files()

    # Updated treeview with files and folders
    def update_Files(self):

        # Clears and sets new text in entry box
        self.change_dir_box.delete('0', 'end')
        self.change_dir_box.insert('0', os.getcwd())

        # Clears all items in the treeview before listing more, by using tree.get_chidren()
        self.show_file_win.delete(*self.show_file_win.get_children())

        # Two loops to show folders first then files. Probably will find better solution
        for file in os.listdir():
            if not os.path.isdir(file):
                self.show_file_win.insert('', 0, values=file)

        for dir in os.listdir():
            # Adds three dots if the item is a directory
            if os.path.isdir(dir):
                self.show_file_win.insert('', 0, values=dir+'...')

    # Goes up a directory from current position
    def go_Up_Directory(self):
        file_sys.go_To_Parent()
        self.update_Files()

    # Functionn for change_dir_entry box
    def change_Dir_Entry(self, _):
        file_sys.change_Dir(self.change_dir_box.get())
        self.update_Files()

    # Go into directory from double click in treeview
    def go_Into_Dir(self, _):
        # Double click directory in treeview. get text value from current selection and removes trailing ...
        current_item = str( self.show_file_win.item( self.show_file_win.selection() )['values'][0][:-3] )
        file_sys.change_Dir(current_item)
        self.update_Files()

root = tk.Tk()

file_sys = File_System()

renaming = Renaming_Window(root, file_sys)

root.mainloop()

# EOF