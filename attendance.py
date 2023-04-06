import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import sys

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance")
        self.root.geometry("1366x768")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("src/bg_main.png"))
        
        canvas = tk.Canvas(self.root, width=1366, height=768)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()

        
