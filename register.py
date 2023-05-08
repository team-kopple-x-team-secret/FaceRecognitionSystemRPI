import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sys
from add_file import Add_File

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
