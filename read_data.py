#-*-coding:utf8-*-
import os
import cv2
import numpy as np
from read_img import endwith

def read_file(path):
    img_list = []
    label_list = []
    user_number = 0 # total user number
    IMG_SIZE = 128

    for child_dir in os.listdir(path):
        child_path = os.path.join(path, child_dir)
        child_path = child_path + "\\picked-faces"
        for dir_image in  os.listdir(child_path):
            if endwith(dir_image,'jpg'):
                img = cv2.imread(os.path.join(child_path, dir_image))
                resized_img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                recolored_img = cv2.cvtColor(resized_img,cv2.COLOR_BGR2GRAY)
                img_list.append(recolored_img)
                label_list.append(user_number)
        
        user_number += 1
    
    img_list = np.array(img_list)

    return img_list, label_list, user_number

def read_name_list(path):
    name_list = []
    for child_dir in os.listdir(path):
        name_list.append(child_dir)
    return name_list



if __name__ == '__main__':
    img_list,label_list = read_file("C:\\Users\\jimmychen\\Desktop\\chernger\\chernger_faceRecognition\\dataset")
    print (counter)


