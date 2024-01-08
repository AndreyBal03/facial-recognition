import cv2
import numpy as np
import os
import sys
from initialfunctions import *



def menu():
    option = None
    print("Which option do you want to use?")
    print("""
          1. Check Face
          2. Add Face
          3. Remove Face
          4. Read Actual Faces
          5. Exit
          Default: 'Exit'
          """)

    option = input("-> ")
    
    match option:
        case "1":
            pass
        case "2":
            add_faces()
        case "3":
            remove_faces()
        case "4":
            read_faces()
        case _:
            sys.exit()


    return 0

def main():
    print("Facial Recognition App V 0.1")
    make_defaults()
    menu()

    return 0

if __name__ == '__main__':
    main()
