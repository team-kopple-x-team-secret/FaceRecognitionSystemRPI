import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import sys
from add_file import Add_File

class Summary:
    def __init__(self, root):
        self.root = root
        self.root.title("Register Form")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.attributes('-fullscreen', True)
        self.bg_image = ImageTk.PhotoImage(Image.open("src/register_form/step3.png"))
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        
        font_color = "#ECEFF4"

        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()
