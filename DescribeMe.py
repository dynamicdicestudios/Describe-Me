import cv2

from tkinter import *
from face_detect import detect_faces
from eyeglass_detector import detect_eyeglasses
from PhotoAgeGender import guessAgeGender

root = Tk()
root.title("CV Grammar")
root.geometry("300x180+500+250")

Label(root, text="Enter the file location:", font=("time new roman",10)).place(x=20,y=50)

file=Entry(root)

def describe(path):
    y_val = 50
    
    move_down = lambda y: y + 25
    
    glasses = detect_eyeglasses(path)
    
    #gets age and gender of person in the image (age first, gender last)
    guess = guessAgeGender(path)

    img = cv2.imread(path)

    if cv2.cvGetWindowHandle("Describe Me") != 0:
        # Close all cv2 windows
        cv2.destroyAllWindows()
    
    cv2.putText(img, "Age: " + str(guess[0]), (10, y_val), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    y_val = move_down(y_val)
    cv2.putText(img, "Gender: " + str(guess[1]), (10, y_val), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    y_val = move_down(y_val)
    if glasses:
        cv2.putText(img, "With Glasses", (10, y_val), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
        y_val = move_down(y_val)

    cv2.imshow("Describe Me", img)

def face_check():
    try:
        path = r""+str(file.get())
        face_count = detect_faces(path)
        if face_count > 1:
            Label(root, text="* Only one face can be described.", font=("time new roman",10), fg='red').place(x=20,y=20)
        else:
            describe(path)
        
    except FileNotFoundError:  Label(root, text="* Please use an existing file.", font=("time new roman",10), fg='red').place(x=20,y=20)
    except OSError:  Label(root, text="* No quotation marks in the file location.", font=("time new roman",10), fg='red').place(x=20,y=80)
    except: Label(root, text="* Please use an existing file.", font=("time new roman",10), fg='red').place(x=20,y=20)

file.place(x=150,y=50)
 
Button(root, text='Describe Me',width=10, command=face_check).place(x=110,y=130)

mainloop()
