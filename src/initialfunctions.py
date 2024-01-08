import os
import shutil
"""This is suppose to be the 'preload file,
and do stuff likem check if the data dir exists,
add the needed functions to the program, etc.'"""

PATH = os.getcwd()

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

    return len(faces)

def add_faces():
    print("Label of the new face")
    label = input("->: ")
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




