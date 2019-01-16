#-*-coding:utf8-*-
import os
import cv2

def readAllImg(path,*suffix):
    try:
        print(path, suffix)
        s = os.listdir(path)
        resultArray = []
        fileName = os.path.basename(path)
        resultArray.append(fileName)

        for i in s:
            if endwith(i, suffix):
                document = os.path.join(path, i)
                img = cv2.imread(document)
                resultArray.append(img)

    except IOError:
        print ("Error")

    else:
        print ("load picture success")
        return resultArray

def endwith(s,*endstring):
    resultArray = map(s.endswith,endstring)
    if True in resultArray:
       return True
    else:
       return False

if __name__ == '__main__':

  result = readAllImg(".\jimmy",'.pgm')
  print (result[0])
  # cv2.namedWindow("Image")
  # cv2.imshow("Image", result[1])
  # cv2.waitKey(0)
  # cv2.destroyAllWindows()
