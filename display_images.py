from pathlib import Path
from tkinter import filedialog
import os
import cv2
import shutil

folder_path = filedialog.askdirectory()

# get current directory
curr_dir = os.getcwd()

# if they don't exist, make three directories 'great', 'good', 'reject' 
for folder in ['great', 'good', 'reject']:
    if not os.path.exists(os.path.join(curr_dir, folder)):
        os.makedirs(os.path.join(curr_dir, folder))

# find all the images in the folder recursively
for path in Path(folder_path).rglob('*.jpg'):

    # open the image
    img = cv2.imread(str(path))

    # display the image
    cv2.imshow('image', img)

    # wait for the user to press a key
    # if 'a', copy to great, if 'd', copy to good, if 'f', copy to reject
    key = cv2.waitKey(0)

    # if not 'a', 'd', or 'f', retry
    while key not in [ord('a'), ord('d'), ord('f'), ord('q')]:
        print(f'Invalid key: {key}')
        key = cv2.waitKey(0)

    if key == ord('q'):
        break

    loc = ['great', 'good', 'reject'][[ord('a'), ord('d'), ord('f')].index(key)]

    # if 'a', send to great
    cv2.imwrite(os.path.join(curr_dir, loc, path.name), img)

    # grab the label that matches
    for other_path in Path(folder_path).rglob(path.stem + '.*'):
        if other_path.suffix != '.jpg':
            
            # copy it to the same folder
            shutil.copy(other_path, os.path.join(curr_dir, loc, other_path.name))


    # print(path.name)
    
    # # find any other files with the same name not ending in .jpg
    # for other_path in Path(folder_path).rglob(path.stem + '.*'):
    #     if other_path.suffix != '.jpg':
    #         print(other_path.name)
