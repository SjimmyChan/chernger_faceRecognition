# -*- coding:utf-8 -*-
import cv2
from train_model import Model
from read_data import read_name_list
from photo_shot import check_user_exist

class Camera_reader(object):
    def __init__(self):
        self.model = Model()
        self.img_size = 128

    def set_userName(self, name):
        self.set_userName(user_name)
        self.model.load()

    def build_camera(self):
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        name_list = read_name_list("C:\\Users\\CN\\Desktop\\intern\\chernger_faceRecognition\\dataset")

        cameraCapture = cv2.VideoCapture(0)
        success, frame = cameraCapture.read()

        while success and cv2.waitKey(1) == -1:
             success, frame = cameraCapture.read()
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
             faces = face_cascade.detectMultiScale(gray, 1.3, 5) 
             for (x, y, w, h) in faces:
                 ROI = gray[x:x + w, y:y + h]
                 ROI = cv2.resize(ROI, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                 label,prob = self.model.predict(ROI)  
                 if prob > 0.7:   
                     show_name = name_list[label]
                 else:
                     show_name = 'Stranger'
                 cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  
                 frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  
             cv2.imshow("Camera", frame)

        cameraCapture.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    camera = Camera_reader()
    user_name, path = check_user_exist()
    camera.set_userName(user_name)
    camera.build_camera()


