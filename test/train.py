import cv2
import os
import numpy as np
from sklearn.preprocessing import LabelEncoder

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Load the pre-trained deep learning face recognition model
model = cv2.face.LBPHFaceRecognizer_create()

# Define the dataset directory and the labels for each person
data_dir = 'test/Images/'
labels = os.listdir(data_dir)

# Initialize empty arrays to store the face data and labels
face_data = []
face_labels = []

# Initialize the label encoder
le = LabelEncoder()

# Loop through each person in the dataset
for label in labels:
    # Define the path to the person's image directory
    label_dir = os.path.join(data_dir, label)

    # Loop through each image in the person's image directory
    for file in os.listdir(label_dir):
        # Load the image
        img = cv2.imread(os.path.join(label_dir, file))

        # Convert the image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect the face in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Loop through each detected face
        for (x, y, w, h) in faces:
            # Crop the face from the image
            face = gray[y:y+h, x:x+w]

            # Resize the face to a fixed size (e.g., 100x100)
            face = cv2.resize(face, (100, 100))

            # Append the face data and label to the arrays
            face_data.append(face)
            face_labels.append(label)

# Transform the face labels to integer values using the label encoder
face_labels = le.fit_transform(face_labels)

# Convert the face data and labels to numpy arrays
face_data = np.array(face_data)
face_labels = np.array(face_labels).astype(np.int32)

# Train the face recognition model using the face data and labels
model.train(face_data, face_labels)

# Save the trained model for later use
model.save('test/trained_model.xml')
