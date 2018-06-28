import cx_Freeze, os, sys

# Tk environment
os.environ['TCL_LIBRARY'] = r'C:\Users\Drake\Anaconda3\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Drake\Anaconda3\tcl\tk8.6'

# Script info
name = 'Snake'
version = '1.2'
author = 'Drake Thomas'
description = 'Snake Game'
copyright = ''
trademark = ''

# Script Set up
script = 'py_Snake.py'
targetName = 'Snake.exe'  # name of the executable
icon = 'snake.ico'  # icon of executable
compressed = False  # creates a zip folder
shortcutName = None  # name of shortcut that'll be created when installing. ONLY MSI BUILD
shortcutDir = None  # where to place shortcut
base = None
if sys.platform == "win32": base = "Win32GUI"

# More script Config
includefiles = ['apple.png', 'snakehead.png']  # included files, like music, photos, etc
packages = ['pygame', 'random', 'time']  # packages that are NEEDED to use script
includes = ['DT']  # include other files, like other python files
excludes = [ ]  # exclude modules

cx_Freeze.setup(
                name=name, version=version, author=author, description=description,
                options={'build_exe': {'packages':packages, 'includes':includes, 'excludes':excludes, 'include_files': includefiles}},
                executables=[cx_Freeze.Executable(script=script, targetName=targetName, icon=icon, shortcutDir=shortcutDir, shortcutName=shortcutName, copyright=copyright, trademarks=trademark)],
                compressed=compressed
                )





