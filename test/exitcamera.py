import cv2
import face_recognition
import pickle
import mysql.connector
import datetime

conn = mysql.connector.connect(
    host="127.0.0.1", port="3306", password="1234", user="root", database="databasee"
)

if conn.is_connected():
    print("Connected to database")
else:
    print("Not connected to database")

# Load the saved encodings
with open('test\EncodeFile.p', 'rb') as f:
    encodeListKnownWithIds = pickle.load(f)

# Extract the encodings and IDs
encodeListKnown = encodeListKnownWithIds[0]
studentIds = encodeListKnownWithIds[1]

# Initialize the video capture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FPS, 15)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

scanned_users = set()  # Use a set instead of a dictionary to store scanned users
last_logged_date = {}  # Dictionary to store the last logged date for each user

while True:
    ret, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(encodeListKnown, face_encoding)

        name = "Unknown"
        if True in matches:
            first_match_index = matches.index(True)
            name = studentIds[first_match_index]

        if name != "Unknown":
            # Check if the user ID has already been scanned in the current session
            if name not in scanned_users:
                # Check if the user has already been logged for the current date
                if name not in last_logged_date or last_logged_date[name] != datetime.date.today():
                    # Get the current date and time
                    current_datetime = datetime.datetime.now()
                    current_date = current_datetime.date()
                    current_time = current_datetime.time()

                    try:
                        cursor = conn.cursor()
                        query = "SELECT ID, First_name, Last_name, Department FROM log WHERE ID = %s"
                        cursor.execute(query, (name,))
                        results = cursor.fetchall()

                        if not results:
                            print("User details not found in the database.")
                        else:
                            for result in results:
                                user_id, first_name, last_name, department = result

                            # Insert the log into the database
                            query = "INSERT INTO `log` (`ID`, `Datee`, `TimeOut`, `First_name`, `Last_name`, `Department`) VALUES (%s, %s, %s, %s, %s, %s)"
                            values = (user_id, current_date, current_time, first_name, last_name, department,)
                            cursor.execute(query, values)
                            conn.commit()

                            # Update the last logged date for the user
                            last_logged_date[name] = current_date

                            # Add the user ID to the scanned users set
                            scanned_users.add(name)

                        cursor.close()

                    except mysql.connector.Error as error:
                        print("Error occurred while executing MySQL operation:", error)

        # Draw a box around the face and show the name
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 20), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    cv2.imshow('Face Recognition System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
