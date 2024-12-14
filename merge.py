import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import sys
from tkinter import filedialog, simpledialog, messagebox
import os
import shutil
import mysql.connector

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
        self.employee_id.place(x=68, y=185, width=771, height=63)

        self.first_name = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.first_name.place(x=72, y=335, width=355, height=63)

        self.last_name = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.last_name.place(x=484, y=335, width=355, height=63)

        self.date_of_birth = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.date_of_birth.place(x=68, y=524, width=355, height=63)

        self.department = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.department.place(x=68, y=675, width=230, height=63)

        self.fulladdress = tk.Entry(self.root, font=font_style, bg="#434C5E", border=0, fg=font_color)
        self.fulladdress.place(x=68, y=814, width=767, height=63)

        self.newbutton = tk.Button(self.root, text="Confirm", bg="#434C5E", fg="#ECEFF4", font=("Rubik", 14), command=self.select_pictures)
        self.newbutton.place(x=68, y=987, width=226, height=63)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
            sys.exit()





    def select_pictures(self):

        

        employee_id = self.employee_id.get()
        first_name = self.first_name.get()
        last_name = self.last_name.get()
        date_of_birth = self.date_of_birth.get()
        address = self.fulladdress.get()
        get_department = self.department.get()
        

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


        
        
        try:

            conn = mysql.connector.connect(
                host="127.0.0.1", port="3306", password="1234", user="root", database="databasee"
            )

            cursor = conn.cursor()

            sql = "INSERT INTO faculty (id, First_name, Last_name, Address, Birthday, Department) VALUES (%s, %s, %s, %s, %s, %s)"

            values = (employee_id, first_name, last_name,date_of_birth, address, get_department)

            cursor.execute(sql, values)

            conn.commit()

            cursor.close()
            conn.close()

        except mysql.connector.Error as error:
            print("Error occurred while executing MySQL operation:", error)
