# coding=utf-8
import cv2
import sys
import os

def take_photo(user_name):
    
    cameraCapture = cv2.VideoCapture(0)
    try:
        if cameraCapture.isOpened():
            count = 0
            success, frame = cameraCapture.read()
        else:
            success = False
        while success:
            cv2.imshow("capture", frame)
            success, frame = cameraCapture.read()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                count += 1
                cv2.imwrite("./source-img/%s_%d.jpg" % (user_name, count), frame)
            elif cv2.waitKey(1) & 0xff == ord('e'):
                cameraCapture.release()
                cv2.destroyAllWindows()
                break
    except:
        print("error accur!!")

def check_user_exist():
    user_name = input("your username : ")

    path = "C:\\Users\\CN\\Desktop\\intern\\chernger_faceRecognition\\dataset\\{}".format(user_name)

    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path + "\\source-{}".format(user_name))
        os.makedirs(path + "\\dataset")
        os.makedirs(path + "\\picTest")
    
    return user_name

if __name__ == "__main__":
    user_name = check_user_exist()
    take_photo(user_name)