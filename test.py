import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

# Prompt the user to enter a name for the folder
folder_name = input("Enter a name for the folder: ")

# Set the directory where the folder will be created
directory = "test\\Faces\\"

# Create the folder
folder_path = os.path.join(directory, folder_name)
os.makedirs(folder_path)

# Open a file picker to select multiple pictures
Tk().withdraw()  # hide the tkinter root window
filenames = askopenfilenames()  # show the file picker

# Move the selected files to the created folder
for filename in filenames:
    shutil.move(filename, folder_path)
