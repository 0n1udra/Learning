# Drake Thomas

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import os
import logging


def update_Files(path, newFileName='_'):
    os.chdir(path)
    # Clears and sets new text in entry box
    change_dir_box.delete('0', 'end')
    change_dir_box.insert('0', os.getcwd())

    # Clears all items in the treeview before listing more, by using tree.get_chidren()
    show_file_win.delete(*show_file_win.get_children())

    index_num = len(os.listdir())
    # Two loops to show folders first then files. Probably will find better solution
    for file in os.listdir():
        if not os.path.isdir(file):
            show_file_win.insert('', 0, text=index_num, values=(file, '>', '  ' + newFileName))
            index_num -= 1

    for dir in os.listdir():
        # Adds three dots if the item is a directory
        if os.path.isdir(dir):
            show_file_win.insert('', 0, text=index_num, values=(dir + '...', '>', '  ' + newFileName))
            index_num -= 1

# Changes directory from input in entry box
def change_Dir(_):
    try:
        # Update treeview with new directory
        update_Files(change_dir_box.get())
    except OSError:
        print("Error: Directory not exist")
    else:
        print("Changing directory to:", change_dir_box.get())

# Go into directory from double click in treeview
def go_Into_Dir(_):
    # Double click directory in treeview. from current selection then 'values' in dict then remove the ...
    current_item = str(show_file_win.item(show_file_win.selection(), 'values')[0])[:-3]

    try:
        update_Files(os.getcwd() + '/' + current_item)
    except Exception:
        print("Error: Item not Directory")

# Goes up a directory from current position
def go_Up_Directory():
    try:
        # Gets the parent directory using current from splitting by /
        update_Files('/'.join(os.getcwd().split('/')[:-1]))
    except OSError:
        print("Error: Can't go to parent directory")

# Shows what new file names would look like before renaming permanently
def refresh_Treeview():
    update_Files(os.getcwd(), rename_box.get().replace("<x>", "_x_"))

def change_Name():
    make_sure = mb.askyesno('Change Names',
                            'Are you sure that you want to rename these files?')
    name_inp = ""

    try:
        name_inp = rename_box.get()
    except ValueError:
        print("No input in rename_box")

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
            print(f"{file} > {final_filename}")
            os.rename(file, final_filename)

        update_Files(os.getcwd())

# Setting up root window
root = tk.Tk()
root.geometry('1000x500')
root.title('Change File Names')

# Setup left frame
left = ttk.Frame(root)
left.pack(side=tk.LEFT)

# Path entry box and Label. Binds Enter
input_dir_label = ttk.Label(left, text='Path').pack()
change_dir_box = ttk.Entry(left)
change_dir_box.pack()
change_dir_box.bind("<Return>", change_Dir)

# Rename entry Box and Label
new_name_input_text = ttk.Label(left, text='Rename').pack()
rename_box = ttk.Entry(left)
rename_box.pack()
rename_box.bind('<Return>', change_Name)

# Setup right frame
right = ttk.Frame(root)
right.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

# treeview column names: #| Original Name | _ | New Name
show_file_win = ttk.Treeview(right, columns=('oN', '_', 'nN'))
# # column
show_file_win.heading('#0', text='#')
show_file_win.column('#0', width=35, stretch=False)
# Original file column
show_file_win.heading('oN', text='Original Files')
# _ column only have >
show_file_win.heading('_', text='>')
show_file_win.column('_', width=10, stretch=False)
# New file name
show_file_win.heading('nN', text='New Files')

# Double click a directory to enter
show_file_win.bind('<Double-1>', go_Into_Dir)

# Fills and expands treeview so it fills right frame correctly
show_file_win.pack(expand=True, fill=tk.BOTH)

# Bottom right frame
bottom_right = tk.Frame(right)
bottom_right.pack(side=tk.BOTTOM, anchor=tk.CENTER)

# Go up a directory (parent directory)
go_up_dir = ttk.Button(bottom_right, text="Up a Directory", command=go_Up_Directory).pack(side=tk.LEFT)

# Refreshes table
refresh_button = ttk.Button(bottom_right, text='Preview rename', command=refresh_Treeview).pack(side=tk.LEFT)
change_File_button = ttk.Button(left, text='Change Names', command=change_Name).pack()
change_dir_box.insert(0, '/Users/drake/Desktop/')

root.mainloop()

# EOF