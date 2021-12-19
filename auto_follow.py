import csv
import time
import random
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

cl =None

root = Tk()
cl=Client()
cl.login('zantanite','J05hu@5728')
user_id=cl.user_id_from_username("dheeraj_joshi2006")
cl.user_follow(user_id)