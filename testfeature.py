import features
import cv2
import params

img1 = cv2.imread(params.IMGLOCATION+'/image_02/data/0000000000.png',0)
img2 = cv2.imread(params.IMGLOCATION+'/image_03/data/0000000000.png',0)

imgout = cv2.imread(params.IMGLOCATION+'image_02/data/0000000000.png')

size = [3,3]

kp1,desc1 = features.getFeatures(img1,size)
kp2,desc2 = features.getFeatures(img2,size)

leftCorres, rightCorres, matches = features.getCorres(desc1,desc2,kp1,kp2)

#img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,corres,imgout,flags=2)
#cv2.imshow("Display",img3)
#cv2.waitKey(0)

# View features
import pdb;pdb.set_trace()
#kpimg = cv2.drawKeypoints(img1,kp1,imgout)
#cv2.imshow("Display Window",kpimg)
#cv2.waitKey(0)
