import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
import os
import shutil


class Add_File:
    def __init__(self, root, previous_window):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)
        self.bg_image = ImageTk.PhotoImage(Image.open("src/register_form/step2.png"))
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        font_color = "#ECEFF4"

        
        self.pickFile = tk.Button(self.root, text="Pick Photos", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.select_pictures)
        self.pickFile.place(x=72, y=833, width=226, height=63)
    
        self.backButton = tk.Button(self.root, text="Back", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.previous_window)
        self.backButton.place(x=72, y=965, width=226, height=63)

        self.address = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.address.place(x=72, y=221, width=771, height=63)

        self.email_address = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.email_address.place(x=72, y=432, width=771, height=63)

        self.phone_number = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.phone_number.place(x=72, y=643, width=771, height=63)


        self.previous_window = previous_window

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()

    def previous_window(self):
        self.root.withdraw()  # withdraw the current window
        self.previous_window.deiconify()  # restore the previous window

    def select_pictures(self):
        # Prompt the user to enter a name for the folder
        folder_name = simpledialog.askstring("Folder Name", "Enter a name for the folder:")
        if folder_name is None or folder_name.strip() == "":
            # User clicked cancel or entered an empty string
            return
        
        # Set the directory where the folder will be created
        directory = "test\\Faces\\"
        
        # Create the folder
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path)
        
        # Create a new window to hold the file picker dialog
        file_picker_window = tk.Toplevel(self.root)
        file_picker_window.withdraw()  # hide the new window initially
        
        # Open a file picker to select multiple pictures
        filenames = filedialog.askopenfilenames(parent=file_picker_window)
        
        # Destroy the new window after the file picker dialog is closed
        file_picker_window.destroy()
        
        # Move the selected files to the created folder
        for filename in filenames:
            shutil.move(filename, folder_path)
