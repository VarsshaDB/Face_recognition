import cv2
import sys
#giving path to the XML file
cascPath = "haarcascade_frontalface_default.xml"
#creating variable to classifier
faceCascade = cv2.CascadeClassifier(cascPath)
#creating varible to caoture the video data
video_capture = cv2.VideoCapture(0)

while True:
    #create a variable for faces
    f = 0
    #get the data from the variable
    ret, frame = video_capture.read()
    #convert into grayscale to reduces the proccesing 
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #start detecting  and get the value
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    #makin rectangles to the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        #counting the rectangles i mean faces
        f = f+1
    #select the font
    font = cv2.FONT_HERSHEY_COMPLEX
    #inserting the face data into the image
    frame = cv2.putText(frame, "NO OF FACE:" + str(f), (10, 30), font, 1, (0, 0, 255), 2, cv2.LINE_AA)
    #showing the video
    cv2.imshow('I CAN COUNT FACE', frame)
    #To terminate form the window
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
