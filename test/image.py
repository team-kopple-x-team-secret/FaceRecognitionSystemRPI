import cv2
import numpy as np
import os

# Load the trained model
model_path = "face_recognizer_model.xml"
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read(model_path)

# Load the cascades
face_cascade = cv2.CascadeClassifier('src\haarcascade_frontalface_default.xml')

# Load image
image_path = "1.png"
img = cv2.imread(image_path)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)

for (x, y, w, h) in faces:
    # Extract the face ROI
    face_roi = gray[y:y + h, x:x + w]

    # Recognize the face
    label, confidence = face_recognizer.predict(face_roi)

    # Get the corresponding folder name
    folders = [name for name in os.listdir("Staff") if os.path.isdir(os.path.join("Staff", name))]
    if label < len(folders):
        person_name = folders[label]
    else:
        person_name = "Unknown"

    # Draw the name and confidence level on the frame
    cv2.putText(img, f"{person_name} - {confidence:.2f}%", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Show the image
cv2.imshow("Face Recognition", img)

# Wait for a key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
