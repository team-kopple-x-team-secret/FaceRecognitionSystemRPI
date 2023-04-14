import cv2
import face_recognition
import pickle

# Load the saved encodings
with open('EncodeFile.p', 'rb') as f:
    encodeListKnownWithIds = pickle.load(f)
    
# Extract the encodings and IDs
encodeListKnown = encodeListKnownWithIds[0]
studentIds = encodeListKnownWithIds[1]

# Initialize the video capture object
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert the frame from BGR (OpenCV) to RGB (face_recognition)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Find all the faces and their encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in the current frame
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for any of the known faces
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)

        # If there's a match, determine the name of the person
        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = studentIds[first_match_index]

        # Draw a box around the face and show the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Face Recognition System', frame)

    # Quit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows()
