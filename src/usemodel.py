import cv2
import os
import pandas as pd

path = os.path.dirname(__file__)

#All is going to be in a function to call it
def useModel():
    print("Loading model...")
    model = cv2.face.EigenFaceRecognizer_create()
    model.read(path + "/model.xml")

    video = cv2.VideoCapture(0)
    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml') #cv2 model
    labels = pd.read_csv(path + "/index.csv")


    print("Press 'q' to exit ")
    while True:
        ret, frame = video.read()
        auxframe = frame.copy()
    
        faces = faceClassif.detectMultiScale(
                frame, #The image
                scaleFactor = 1.1, #Reduce 10% the image
                minNeighbors = 6,
                minSize = (100,100))

        for (x,y, width, height) in faces:
            face = auxframe[y:y+height, x:x+width]
            face = cv2.resize(face, (150,150), cv2.INTER_AREA)
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
            ans = model.predict(face)

            final_l = labels[str(ans[0])][0]
            if ans[1] > 5000:
                final_l = "Unknown"
            cv2.putText(frame, f"{final_l}", (x-10,y-10), 1, 2, (255,255,255), 1, cv2.LINE_AA)

        cv2.imshow("Si", frame)

        if cv2.waitKey(1) == ord("q"):
            break
    video.release()
    cv2.destroyAllWindows()
