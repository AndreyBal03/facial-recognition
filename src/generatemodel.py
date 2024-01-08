import cv2
import os
import numpy as np
import pandas as pd

path = f"{os.getcwd()}/data"
labels = []
faces = []
label_map = {}
label = 0

for name in os.listdir(path):
    label_map[label] = name
    for frame in os.listdir(f"{path}/{name}"):
        labels.append(label)
        faces.append(cv2.imread(f"{path}/{name}/{frame}"))
    label+=1

path = os.getcwd()

#Generate the new model :D
model = cv2.face.EigenFaceRecognizer_create()
model.train(faces, np.array(labels))

#Save :D
#Model
if os.path.exists(f"{path}/model.xml"):
    if not os.path.exists(f"{path}/old_models"):
        os.makedirs("old_models")
    os.rename(f"{path}/model.xml", f"{path}/old_models/model{len(os.listdir(path + '/' + 'old_models'))}.xml")

model.write("model.xml")

#Data
data = pd.DataFrame(label_map, index = [0])
if os.path.exists(f"{path}/index.csv"):
    if not os.path.exists(f"{path}/index"):
        os.makedirs("old_index")
    os.rename(f"{path}/index.csv", f"{path}/old_index/index{len(os.listdir(path + '/' + 'old_models'))}.csv")


data.to_csv("index.csv")

print("Model ready")
