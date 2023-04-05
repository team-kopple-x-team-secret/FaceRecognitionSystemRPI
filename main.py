import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Login")
root.geometry("1366x768")

bg_image = Image.open("src/login.png")
bg_photo = ImageTk.PhotoImage(bg_image)

canvas = tk.Canvas(root, width=1366, height=768)
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

font_style = ("Rubik", 16)

username_entry = tk.Entry(root, width=30, bg="#D9D9D9", bd=0, highlightthickness=0, font=font_style)
username_entry.place(x=571, y=288, width=316, height=60)

password_entry = tk.Entry(root, show="*", width=30, bg="#D9D9D9", bd=0, highlightthickness=0, font=font_style)
password_entry.place(x=571, y=384, width=316, height=60)

login_button = tk.Button(root, text="Login", bg="#3E806E", fg="#D9D9D9", bd=0, highlightthickness=0, font=font_style)
login_button.place(x=479, y=509, width=408, height=60)

canvas.create_rectangle(479, 288, 571, 348, fill="#B97A7A", outline="")
canvas.create_rectangle(479, 384, 571, 444, fill="#B97A7A", outline="")

username_icon = Image.open("src/icon_username.png")
username_photo = ImageTk.PhotoImage(username_icon)
canvas.create_image(511, 302, image=username_photo, anchor="nw")

password_icon = Image.open("src/icon_password.png")
password_photo = ImageTk.PhotoImage(password_icon)
canvas.create_image(511, 398, image=password_photo, anchor="nw")


root.mainloop()
