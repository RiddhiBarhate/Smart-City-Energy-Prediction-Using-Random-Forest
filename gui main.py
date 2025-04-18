# -*- coding: utf-8 -*-ss
"""
Created on Tue May  4 17:28:41 2021

@author: user
"""

import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time
from tkvideo import tkvideo
'''import detection_emotion_practice as validate'''

root=tk.Tk()

root.title("Electricity Demand Forecasting")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"Firefly.jpg")
bg_resized = bg.resize((w, h), Image.LANCZOS)  # Resize the image to fit the screen
bg_img = ImageTk.PhotoImage(bg_resized)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=0)


#bg.resize((2304,1792),Image.ANTIALIAS)
#print(w,h)
#bg_img = ImageTk.PhotoImage(bg)
#bg_lbl = tk.Label(root,image=bg_img)
#bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

# video_label =tk.Label(root)
# video_label.pack()
# # read video to display on label
# player = tkvideo("road1.mp4", video_label,loop = 1, size = (w, h))
# player.play()

w = tk.Label(root, text="Electricity Demand Forecasting",relief="solid",width=70,background="aliceblue",foreground="black",height=2,font=("Times new roman",30,"bold"))
w.place(x=0,y=0)

#label_l1 = tk.Label(root, text="FAKE JOB POSTINGS",font=("Times New Roman", 30, 'bold'), relief="solid", padx=5, pady=10,
                  #  background="aliceblue", fg="black", width=70, height=2)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="black")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])
def window():
  root.destroy()
  

wlcm=tk.Label(root,text="......Welcome to Electricity Demand Forecasting page ......",width=120,height=3,background="#79a8d8",foreground="white",font=("Times new roman",19,"bold"))
wlcm.place(x=0,y=720)




d2=tk.Button(root,text="Login",command=Login,width=20,bd=0,background="black",foreground="white",font=("times new roman",17,"bold"))
d2.place(x=100,y=300)


d3=tk.Button(root,text="Register",command=Register,width=20,bd=0,background="black",foreground="white",font=("times new roman",17,"bold"))
d3.place(x=100,y=400)

button4 = tk.Button(root, text="EXIT", command=window, width=20, font=("times new roman",17,"bold"),bd=0,bg="red", fg="white")
button4.place(x=100, y=500)

root.mainloop()
