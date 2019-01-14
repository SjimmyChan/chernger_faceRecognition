import cv2
import sys

def takeshot(self):

    cameraCapture = cv2.VideoCapture(0)
    success, frame = cameraCapture.read()
    count = 0

    while(1):
        count += 1
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite("C:\Users\CN\Desktop\intern\chernger_faceRecognition\source-jimmy\jimmy" + str(count) + ".jpg", frame)
        elif cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cameraCapture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    takeshot()    