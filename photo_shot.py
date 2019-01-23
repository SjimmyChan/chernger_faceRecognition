# coding=utf-8
import cv2
import sys
import os

def take_photo(user_name, path):
    
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
                cv2.imwrite(path + "\\source-img\\%s_%d.jpg" % (user_name, count), frame)
            elif cv2.waitKey(1) & 0xff == ord('e'):
                cameraCapture.release()
                cv2.destroyAllWindows()
                print("save %d pictures to %s" % (count, path + "\\source-img"))
                break
    except:
        print("error accur!!")

def check_user_exist():
    user_name = input("your username : ")

    path = "C:\\Users\\jimmychen\\Desktop\\chernger\\chernger_faceRecognition\\dataset\\{}".format(user_name)

    if not os.path.exists(path):
        os.makedirs(path)
        os.makedirs(path + "\\source-img")
        os.makedirs(path + "\\picked-faces")
    
    return user_name, path

if __name__ == "__main__":
    user_name, path = check_user_exist()
    take_photo(user_name, path)