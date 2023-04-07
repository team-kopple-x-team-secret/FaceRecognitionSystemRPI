import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from attendance import Attendance
import sys

class Login:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Login")
        self.root.geometry("1366x768")

        # Load background image
        self.bg_image = ImageTk.PhotoImage(Image.open("src/login/login.png"))

        canvas = tk.Canvas(self.root, width=1366, height=768)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        font_style = ("Rubik", 16)

        self.username_entry = tk.Entry(self.root, width=30, bg="#D8DEE9", bd=0, highlightthickness=0, font=font_style)
        self.username_entry.place(x=571, y=288, width=316, height=60)

        self.password_entry = tk.Entry(self.root, show="*", width=30, bg="#D8DEE9", bd=0, highlightthickness=0, font=font_style)
        self.password_entry.place(x=571, y=384, width=316, height=60)

        login_button = tk.Button(self.root, text="Login", bg="#3E806E", fg="#ECEFF4", bd=0, highlightthickness=0, font=font_style, command=self.login)
        login_button.place(x=479, y=509, width=408, height=60)

        canvas.create_rectangle(479, 288, 571, 348, fill="#BF616A", outline="")
        canvas.create_rectangle(479, 384, 571, 444, fill="#BF616A", outline="")

        username_icon = Image.open("src/login/icon_username.png")
        username_photo = ImageTk.PhotoImage(username_icon)
        canvas.create_image(511, 302, image=username_photo, anchor="nw")

        password_icon = Image.open("src/login/icon_password.png")
        password_photo = ImageTk.PhotoImage(password_icon)
        canvas.create_image(511, 398, image=password_photo, anchor="nw")

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
