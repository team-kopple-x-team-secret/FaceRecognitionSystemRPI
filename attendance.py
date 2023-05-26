import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import merge
import cv2
import sys

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)
        self.bg_image = ImageTk.PhotoImage(Image.open("src/main/bg_main.png"))
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        
        # create a button to open the register form
        register_button = tk.Button(self.root, text="Register", font=font_style, command=self.open_register_form)
        register_button.place(x=600, y=500)

    def open_register_form(self):
        # Hide attendance window
        self.root.withdraw()

        # Open register form window
        register_window = tk.Toplevel()
        register_form = merge.Register(register_window)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()


            
