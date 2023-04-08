import cv2
import numpy as np
import os

# Load the trained model
model_path = "face_recognizer_model.xml"
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(model_path)

# Load the cascades
face_cascade = cv2.CascadeClassifier('src\haarcascade_frontalface_default.xml')

# Load the folders
folders = os.listdir("Staff")

# Initialize camera
cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while True:
    # Read frame from camera
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

    for (x, y, w, h) in faces:
        # Extract the face ROI
        face_roi = gray[y:y + h, x:x + w]

        # Recognize the face
        label, confidence = face_recognizer.predict(face_roi)

        # Check the range of the label
        if label >= len(folders):
            person_name = "Unknown"
        else:
            # Get the corresponding folder name
            person_name = folders[label]

        # Draw the name and confidence level on the frame
        cv2.putText(frame, f"{person_name} - {confidence:.2f}%", (x, y - 10), font, 0.8, (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Show the frame
    cv2.imshow("Face Recognition", frame)

    # Exit when the 'q' key is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cam.release()
cv2.destroyAllWindows()
