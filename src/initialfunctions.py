import os
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
    return 0

def add_faces():
    print("Label of the new face")
    label = input("->: ")
    os.system(f"python addfaces.py {label}")

    return 0

