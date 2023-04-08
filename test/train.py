import cv2
import numpy as np
import os

# Path to the face detection cascade file
cascade_path = "src/haarcascade_frontalface_default.xml"

# Path to the dataset folder
dataset_path = "Staff"

# Load the face detection cascade
face_cascade = cv2.CascadeClassifier(cascade_path)

# Load images and labels
images = []
labels = []
label_names = []

for label_name in os.listdir(dataset_path):
    label_path = os.path.join(dataset_path, label_name)
    if os.path.isdir(label_path):
        for image_name in os.listdir(label_path):
            image_path = os.path.join(label_path, image_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

            # Detect faces in the image
            faces = face_cascade.detectMultiScale(image, scaleFactor=1.2, minNeighbors=5)

            # Crop and resize the face regions
            for (x, y, w, h) in faces:
                face = cv2.resize(image[y:y+h, x:x+w], (100, 100))
                images.append(face)
                labels.append(len(label_names))
            label_names.append(label_name)

# Train the model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.train(images, np.array(labels))

# Save the trained model
model_path = "src/face_recognizer_model.xml"
face_recognizer.write(model_path)

print("Training complete. Model saved to", model_path)
