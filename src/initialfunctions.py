import os
import time
import shutil
"""This is suppose to be the 'preload file,
and do stuff likem check if the data dir exists,
add the needed functions to the program, etc.'"""

PATH = os.getcwd()
def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def make_defaults():
    #By first instance this is the only needed to start
    #besides the execution file
    if os.path.exists(PATH + "/data"):
        return 0
    else:
        os.makedirs("data")
    return 0

def read_faces():
    #This will be based on the idea
    #that all the directories will have the
    #same name as the label of the pictures
    faces = os.listdir(PATH + "/data")
    
    print("Faces: ")
    for i in faces:
        print(i)
    
    time.sleep(2)
    return len(faces)

def add_faces():
    print("Label of the new face")
    print("write -1 if you want to exit")
    label = input("-> ")
    if label == "-1":
        return 0
    os.system(f"python addfaces.py {label}")

    return 0

def remove_faces():
    num_faces = read_faces()
    
    print("How many faces do you want to remove?")
    n = int(input("-> ")) 

    if not n > 0:
        return 0

    if not num_faces > n:
        n = num_faces

    while n != 0:
        print("Introduce the name of the label")
        print("write -1 to exit")
        option = input("-> ")

        if option == "-1":
            return 0

        if os.path.exists(f"{PATH}/data/{option}"):
            shutil.rmtree(f"{PATH}/data/{option}")
            n-=1

    return 0

def generate():
    if not len(os.listdir(f"{PATH}/data")) != 0:
        print("There is not enough faces to create a model :(")
        time.sleep(3)
        return -1

    os.system("python generatemodel.py")
    time.sleep(1)

    return 0

def use():

    #Check needed files
    if not os.path.exists(f"{PATH}/model.xml"):
        print("The model hasn't been created, please use the other functions to create one")
        time.sleep(3)
        return -1
    if not os.path.exists(f"{PATH}/index.csv"):
        print("Label map is missing :(, generate again the model")
        time.sleep(3)
        return -1

    os.system("python usemodel.py")

    return 0


