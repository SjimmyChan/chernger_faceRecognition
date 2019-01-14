import cv2
import sys

def takeshot():

    cameraCapture = cv2.VideoCapture(0)
    success, frame = cameraCapture.read()
    count = 0

    try:
        while cv2.waitKey(1) & 0xFF == ord('q'):
            count += 1
            cv2.imshow("capture", frame)
            cv2.imwrite(".\source-jimmy\jimmy{}.jpg".foramt(count), frame)
    except:
        print("error accur!!")

    cameraCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    takeshot()    