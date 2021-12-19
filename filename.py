import os

# specify the img directory path
path = r'C:\Users\dell\Pictures'

# list files in img directory
files = os.listdir(path)

for file in files:
    # make sure file is an image
    if file.endswith(('.jpg', '.png', 'jpeg')):
        img_path = path + file
    

        