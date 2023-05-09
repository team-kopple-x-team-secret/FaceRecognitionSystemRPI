import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import sys
from tkinter import filedialog, simpledialog, messagebox
import os
import shutil

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)
        self.bg_image = ImageTk.PhotoImage(Image.open("src/register_form/step1.png"))
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        
        font_color = "#ECEFF4"

        self.employee_id = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.employee_id.place(x=72, y=200, width=771, height=63)

        self.first_name = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.first_name.place(x=72, y=390, width=355, height=63)

        self.middle_initial = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.middle_initial.place(x=478, y=390, width=101, height=63)

        self.last_name = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.last_name.place(x=630, y=390, width=202, height=63)

        self.date_of_birth = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.date_of_birth.place(x=72, y=614, width=355, height=63)

        gender_options = ["Male", "Female", "Other"]

        self.selected_gender = tk.StringVar()

        combostyle = ttk.Style()
        combostyle.theme_create('nord', parent='alt', settings={
            'TCombobox': {
                'configure': {
                    'selectbackground': '#5E81AC',
                    'selectforeground': '#ECEFF4',
                    'fieldbackground': '#434C5E',
                    'background': '#3B4252',
                    'foreground': '#ECEFF4'
                }
            }
        })
        combostyle.theme_use('nord')

        gender_combo = ttk.Combobox(self.root, textvariable=self.selected_gender, values=gender_options, font=("Rubik", 14), state="readonly", style="nord.TCombobox")
        gender_combo.place(x=68, y=768, width=229, height=70)

        self.my_button = tk.Button(self.root, text="Click me", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.button_clicked)
        self.my_button.place(x=249, y=938, width=129, height=52)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()

    def button_clicked(self):
        employee_id = self.employee_id.get()
        first_name = self.first_name.get()
        middle_initial = self.middle_initial.get()
        last_name = self.last_name.get()
        date_of_birth = self.date_of_birth.get()
        selected_gender = self.selected_gender.get()

        addfile_window = tk.Toplevel()
        addFile = Add_File(addfile_window, self.root)
        self.root.withdraw()






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

        self.nextButton = tk.Button(self.root, text="Back", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.next_window)
        self.nextButton.place(x=349, y=965, width=226, height=63)

        self.full_address = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.full_address.place(x=72, y=221, width=771, height=63)

        self.email_address = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.email_address.place(x=72, y=432, width=771, height=63)

        self.phone_number = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.phone_number.place(x=72, y=643, width=771, height=63)


        self.previous_window = previous_window

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()

    def previous_window(self):
        self.root.withdraw()  # withdraw the current window
        self.previous_window.deiconify()  # restore the previous window

    def next_window(self):

        address = self.full_address.get()
        email = self.email_address.get()
        phone = self.phone_number.get()

        summary_window = tk.Toplevel()
        summary = Summary(summary_window, self.root)
        self.root.withdraw()
    
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

class Summary:
    def __init__(self, root, previous_summary_window):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)
        self.bg_image = ImageTk.PhotoImage(Image.open("src/register_form/step3.png"))
        self.previous_summary_window = previous_summary_window 
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        font_style = ("Rubik", 16)
        font_color = "#ECEFF4"

        self.backButton = tk.Button(self.root, text="Back", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.go_back)
        self.backButton.place(x=72, y=965, width=226, height=63)

        self.nextButton = tk.Button(self.root, text="Next", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.next_window)
        self.nextButton.place(x=349, y=965, width=226, height=63)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()


    def go_back(self):
        self.root.withdraw()  # withdraw the current window
        self.previous_summary_window.deiconify()  # restore the previous window

    def next_window(self):
        pass
