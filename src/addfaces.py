import cv2
import sys
import os

#To allow call the whole program and pass the label
#from another file, Everything is going to be inside a function

def addFace(label):
    path = os.path.dirname(__file__) + f"/data/{label}"

    if not os.path.exists(path):
        os.makedirs(path)

    video = cv2.VideoCapture(0) 
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #cv2 model
    num_of_faces = len(os.listdir(path))

    print("Press 'q' to exit")
    while True:
        ret, frame = video.read()
        auxframe = frame.copy()
    
        faces = faceClassif.detectMultiScale(
                frame, #The image
                scaleFactor = 1.1, #Reduce 10% the image
                minNeighbors = 6, 
                minSize = (100,100))

        if len(faces) != 0:
            num_of_faces += 1
        print(f"Number or faces register: {num_of_faces}", end = "\r")

    #Get the faces and add rectangles
        for (x, y , width, height) in faces:
            face = auxframe[y:y+height, x:x+width]
            cv2.rectangle(frame, (x,y), (x+width, y+height), (0,255,0), 3)
            cv2.imwrite(f"{path}/face_{num_of_faces}.jpg", cv2.resize(face, (150, 150),cv2.INTER_AREA ))
        cv2.imshow(label,frame)

        if cv2.waitKey(1) == ord("q"): #Press q to exit
            break
    

    video.release()
    cv2.destroyAllWindows()
