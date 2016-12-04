import featureDetect
import cv2

img = cv2.imread('/home/lwan/dev/dataset/2011_09_26_drive_0029_sync/image_02/data/0000000000.png',0)
imgout = cv2.imread('/home/lwan/dev/dataset/2011_09_26_drive_0029_sync/image_02/data/0000000000.png')

size = [4,4]

kp = featureDetect.getFeatures(img,size)

kpimg = cv2.drawKeypoints(img,kp,imgout)
cv2.imshow("Display Window",kpimg)
cv2.waitKey(0)
