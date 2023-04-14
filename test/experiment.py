import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
from register import Register
import cv2
import sys
import os

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance")
        self.root.geometry("1920x1080")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        self.bg_image = ImageTk.PhotoImage(Image.open("src/main/bg_main.png"))
        
        canvas = tk.Canvas(self.root, width=1920, height=1080)
        canvas.pack(fill="both", expand=True)
        canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        
        font_style = ("Rubik", 16)
        
        # create a button to open the register form
        register_button = tk.Button(self.root, text="Register", font=font_style, command=self.open_register_form)
        register_button.place(x=600, y=500)
        
        # Load the trained model
        model_path = "src/face_recognizer_model.xml"
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read(model_path)

        # Load the cascades
        self.face_cascade = cv2.CascadeClassifier('src/haarcascade_frontalface_default.xml')

        # Load the folders
        self.folders = os.listdir("Staff")

        # Initialize camera
        self.cam = cv2.VideoCapture(0)
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        
        # create a label to display the video feed
        self.video_label = tk.Label(self.root)
        self.video_label.place(x=1000, y=100)
        
        # start the video feed and face recognition
        self.show_video_feed()

    def show_video_feed(self):
        # read a frame from the camera
        ret, frame = self.cam.read()
        
        if ret:
            # convert the frame from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # detect faces in the frame
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
            
            for (x, y, w, h) in faces:
                # extract the face ROI
                face_roi = gray[y:y + h, x:x + w]
                
                # recognize the face
                label, confidence = self.face_recognizer.predict(face_roi)
                
                # check the range of the label
                if label >= len(self.folders):
                    person_name = "Unknown"
                else:
                    # get the corresponding folder name
                    person_name = self.folders[label]
                
                # draw the name and confidence level on the frame
                cv2.putText(frame, f"{person_name} - {confidence:.2f}%", (x, y - 10), self.font, 0.8, (0, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            
            # convert the frame to a PIL Image
            pil_image = Image.fromarray(frame)
            
            # resize        pil_image = pil_image.resize((640, 480), Image.ANTIALIAS)
        
        # convert the PIL Image to a Tkinter PhotoImage
        tk_image = ImageTk.PhotoImage(pil_image)
        
        # update the label with the new image
        self.video_label.config(image=tk_image)
        self.video_label.image = tk_image
    
    # schedule the next update in 10 milliseconds
    self.root.after(10, self.show_video_feed)

def open_register_form(self):
    # Hide attendance window
    self.root.withdraw()

    # Open register form window
    register_window = tk.Toplevel()
    register_form = Register(register_window)

def on_closing(self):
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # release the camera
        self.cam.release()
        
        self.root.destroy()
        sys.exit()
