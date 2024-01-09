import cv2
import numpy as np
import os
import sys
from initialfunctions import *

def help_():
    print("""
          Steps for using this app
          
          1. Use the option 2 ('Add Face'), first the program will ask you
          the name of the 'label' that is going to have the face that will detect in your
          camera, press 'q' to stop recording faces

          If you make any mistake and you don't want to have any face in your data, you can
          use the option 3 ('Remove Face') and eliminate some labels

          If you are not sure of which labels you have registered, don't worry, you can use the
          option 4 ('Read Actual Faces') to see all the labels that are registered

          2. Once you are ready to test and you have all the faces and labels that you wanted to register,
          it's time to compile the model using option 5 ('Generate Model'), every time that you want to
          modify the faces or labels, you'll need to compile the model

          3. When you have compiled the model, just use the option 1 ('Check Face'), and then the faces
          in the camera will be labeled by the model, press 'q' to exit.
          """)
    x = input("PRESS ENTER TO EXIT")
    return 0

def menu():
    option = None
    print("Which option do you want to use?")
    print("""
          1. Check Face
          2. Add Face
          3. Remove Face
          4. Read Actual Faces
          5. Generate Model
          6. Help
          7. Exit
          Default: 'Exit'
          """)

    option = input("-> ")
    
    match option:
        case "1":
            use()
        case "2":
            add_faces()
        case "3":
            remove_faces()
        case "4":
            read_faces()
        case "5":
            generate()
        case "6":
            help_()
        case _:
            sys.exit()


    return 0

def main():
    print("Facial Recognition App V 0.1")
    make_defaults()
    while True:
        clear()
        menu()

    return 0

if __name__ == '__main__':
    main()
