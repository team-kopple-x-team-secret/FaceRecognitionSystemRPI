import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from attendance import Attendance
import sys

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.attributes('-fullscreen', True)
        # Load background image
        self.bg_image = ImageTk.PhotoImage(Image.open("src/login/login.png"))

        # Set window size to match image dimensions
        self.root.geometry(f"{self.bg_image.width()}x{self.bg_image.height()}")
        
        canvas = tk.Canvas(self.root, width=self.bg_image.width(), height=self.bg_image.height())
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        font_style = ("Rubik", 16)

        self.username_entry = tk.Entry(self.root, width=30, bg="#D8DEE9", bd=0, highlightthickness=0, font=font_style)
        self.username_entry.place(x=828, y=443, width=370, height=70)

        self.password_entry = tk.Entry(self.root, show="*", width=30, bg="#D8DEE9", bd=0, highlightthickness=0, font=font_style)
        self.password_entry.place(x=829, y=566, width=370, height=70)

        login_button = tk.Button(self.root, text="Login", bg="#3E806E", fg="#ECEFF4", bd=0, highlightthickness=0, font=font_style, command=self.login)
        login_button.place(x=721, y=718, width=475, height=70)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username == "user" and password == "1234":
            messagebox.showinfo("Login Successful", "You have successfully logged in!")
        
            # Hide login window
            self.root.withdraw()

            # Open attendance window
            attendance_window = tk.Toplevel()
            attendance = Attendance(attendance_window)

        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()

