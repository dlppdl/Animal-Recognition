#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:37:42 2019

@author: dlppdl
"""

#Importing the necessary modules
from tkinter import Tk,Frame,Label,Button,LEFT,RIGHT,BOTTOM,TOP,filedialog
from PIL import ImageTk, Image
from AnimalRecognize import animalrecognition

root = Tk()
root.title("DESKTOP GUI")
root.geometry("1366x700+0+0")
root.configure(background='light Blue')
path = ''

def home():
    destroy()
    title()
    frame()
    select()
    
#The 10 animals you see on the GUI
def frame():
    left = Frame(root, width = 600, height = 600, bd = 0 , relief = "raise")
    left.pack(side=LEFT)
    img = Image.open("ars_1.jpg")
    img = ImageTk.PhotoImage(img)
    lbl = Label(left, image = img)
    lbl.image = img 
    lbl.pack()
    
    right = Frame(root, width = 600, height = 600, bd = 0 , relief = "raise")
    right.pack(side=RIGHT)
    img1 = Image.open("ars_2.jpg")
    img1 = ImageTk.PhotoImage(img1)
    lbl1 = Label(right, image = img1)
    lbl1.image = img1 
    lbl1.pack()

#Title of the top
def title():
    top = Frame(root, width = 1366, height = 100, bd = 0 , relief = "raise")
    top.pack()
    img = Image.open("ars_3.png")
    img = ImageTk.PhotoImage(img)
    lbl = Label(top, image = img)
    lbl.image = img 
    lbl.pack()

def destroy():
    for window in root.winfo_children():
        window.destroy()

def openfn():
    filename = filedialog.askopenfilename(title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    return filename

#Resizing the input image t fit in the screen
def resize():
    global path
    path = openfn()
    hsize = 600
    print(path)
    img = Image.open(path)
    wpercent = (hsize / float(img.size[1]))
    wsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    return img

def open_img():
    global button
    img = resize()
    
    destroy()
    title()
    
    btn2 = Button(root,
                  text='Homepage',
                  command=home,
                  font=("Arial Bold",20))
    
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack(side=LEFT)
    
    btn2.pack(side=TOP)
    button = Button(root,text='Recognize',
                    command=recognize,
                    font=("Arial Bold",20))
    button.pack(side=BOTTOM)

def select():
    btn = Button(
            root, text='SELECT\nIMAGE', 
            command=open_img,
            font=("Arial Bold",25))
    btn.pack( anchor='center',side = 'top')

def recognize():
    recognize = animalrecognition(path) #calling the function of AnimalRecognize.py
    if recognize == "Not Found":
        recognize = recognize
    else:
        recognize = 'The animal\nin the image \nis ' + recognize
        
    lbl1 = Label(root,text=recognize,
                font=("Arial Bold",33),
                fg = 'blue'
                )
    lbl1.pack(anchor='center')
    button.destroy()

if __name__ == '__main__':
    home()
    
root.mainloop()
