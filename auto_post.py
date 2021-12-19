import csv
import time
import random
import matplotlib
matplotlib.use('Agg')
from instagrapi import Client
from requests.api import request
from tkinter import *
from tkinter import filedialog as fd
import tkinter as tk
from tkinter import Button, ttk
import json
import time
import os
import json
import requests
import re
from instagrapi import Client
import json
from tkinter import Tk, filedialog
root = Tk()
cl =None
time_=Variable()
time_wait=time_.get()*3600

def select_posts_file():
    global filename
    filename = filedialog.askdirectory(
        title='Open a file',
        initialdir='/',
        )  
accounts={
    'zantanite':'J05hu@5728',
    }

def auto_post():
    file_last=filename.split("/")[-1]   
    username=file_last
    print(username)
    password=accounts[file_last]
    print(password)
    cl=Client()
    cl.login(username,password)
    print('login')
    path = filename

# list files in img directory
    files = os.listdir(path)
    all_paths=[]
    for file in files:
        # make sure file is an image
        if file.endswith(('.jpg', '.png', 'jpeg')):
            img_path = path +'/' +file
            all_paths.append(img_path)
    a=0
    for i in all_paths:
        print(a)
        cl.photo_upload(i,str(i).split('/')[-1].replace(".jpg",''))
        print('posr' +str(a))
        time.sleep(int(time_wait))
        a=a+1
        
root.geometry('500x500')
root.title("Instagram Auto Post ")
label_0 = Label(root, text="Choose the posts folder",font=("bold", 16))
label_0.place(x=90,y=53)

# open button

time_w = Entry(root, font=('arial', 15), textvariable=time_, width=15).place(x=220,y=330)

open_button = ttk.Button(root,text='Open a File',command=select_posts_file).place(x=220,y=130)
open_button_1 = ttk.Button(root,text='Open a File',command=auto_post).place(x=220,y=170)


root.mainloop()