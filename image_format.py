import cv2
import os

#catch every picture that fits frontalface 
def readPicSaveFace(path):

    img = cv2.imread(path, -1)
    
    #cascadePath = "haarcascade_frontalface_alt.xml"
    #catch_face = cv2.CascadeClassifier(cascadePath)
    #faceRect = catch_face.detectMultiScale(imageGray, scaleFactor=1.1, minNeighbors=1, minSize=(1,1))

readPicSaveFace(r'C:\Users\CN\Desktop\20181027-intern\chernger_faceRecognition\source_pic\1.jpg')

