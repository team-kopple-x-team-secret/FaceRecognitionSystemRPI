import cv2
import face_recognition
import pickle
import os


# Importing student images
folderPath = 'test/Faces'
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
studentIds = []
for student in pathList:
    studentPath = os.path.join(folderPath, student)
    imagesList = os.listdir(studentPath)
    for path in imagesList:
        imgList.append(cv2.imread(os.path.join(studentPath, path)))
        studentIds.append(os.path.splitext(student)[0])

print(studentIds)


def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")
