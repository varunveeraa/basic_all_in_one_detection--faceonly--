#import module from tkinter for UI
from tkinter import *
import os
from datetime import datetime;

#creating instance of TK
root=Tk()

root.configure(background="black")

#root.geometry("300x300")

def function1():
    
    os.system("face_detection_1.py")
    
def function2():
    
    os.system("face_detection_2.py")

def function3():

    os.system("face_smile_detection.py")

def function4():

    root.destroy()

#stting title for the window
root.title("Detections")

#creating a text label
Label(root, text="Detections Using Haar Cascades",font=("times new roman",20),fg="white",bg="black",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#initiating first button
Button(root,text="Face Detection",font=("times new roman",20),bg="#000000",fg='green',command=function1).grid(row=2,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#initiating second button
Button(root,text="Facial Features Detection",font=("times new roman",20),bg="#000000",fg='green',command=function2).grid(row=3,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#initiating third button
Button(root,text="Smile Detection",font=('times new roman',20),bg="#000000",fg="green",command=function3).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating an EXIT button
Button(root,text="Quit",font=('times new roman',20),bg="black",fg="red",command=function4).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

root.mainloop()

