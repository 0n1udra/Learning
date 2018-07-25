import os
# 
class File_System:
    def __init__(self):
        print("Current directory:", os.getcwd())

    # Changes directory from input in entry box
    def change_Dir(self, path):
        try:
            # Go into directory
            os.chdir(path)
        except OSError:
            print(f"Error: {path} not accessible")
            return 0
        else:
            print("Current directory now:", os.getcwd())
            return os.getcwd()

    def go_To_Parent(self):
        try:
            # Gets the parent directory using current from splitting by /
            os.chdir('/'.join(os.getcwd().split('/')[:-1]))
        except OSError:
            print("Error: Can't go to parent directory")
            return 0
        else:
            print("Current Directory now:", os.getcwd())
            return os.getcwd()

    def rename_File(self, file, rename):
        try:
            os.rename(file, rename)
        except OSError:
            print(f"Error: Can't rename {file} to {rename}")
            return 0
        else:
            print(f"Renamed: {file} > {rename}")
            return rename

    def delete_File(self, file):
        try:
            os.remove(file)
        except OSError:
            print(f"Error: Can't delete {file}")
            return 0
        else:
            print(f"{file} Deleted")
            return 1

    def get_Dir_Items(self, path):
        return os.listdir(path)

    def create_Blank_File(self, file):
        try:
            open(file, 'a').close()
        except OSError:
            print(f"Error: {file} not created")

    def __str__(self):
        return "Current location:", os.getcwd()
