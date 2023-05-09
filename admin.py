import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import login
import sys


class Admin:
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

        login = login(tk.Toplevel(), self.root)
        self.root.withdraw()