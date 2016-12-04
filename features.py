import numpy as np
import cv2
import operator
import collections

def getFeatures(img, sizeWindowArray ):
    
    height, width= img.shape

    xstep = int(width/sizeWindowArray[1])
    ystep = int(height/sizeWindowArray[0])
    arrayidx = 0
    sift = cv2.xfeatures2d.SIFT_create(100)
    windowidx = 0
    
#    desc = np.zeros(1)
    kp = []
    # Loop through windows
    for y in range(0,ystep*sizeWindowArray[0],ystep):

        for x in range(0,xstep*sizeWindowArray[1],xstep):
            
            # Find SIFT features
            kpTemp, desctemp = sift.detectAndCompute(img[y:y+ystep-1,x:x+xstep-1],None)
            
            for idx in range(len(kpTemp)):
                # Compensate for global offset
                kpTemp[idx].pt = tuple(map(operator.add,  kpTemp[idx].pt, (x,y)))

            if x==0 and y==0:
                desc = desctemp
            else:
                desc = np.concatenate((desc,desctemp), axis=0)

            kp = kp + kpTemp
    
    returns = (kp,desc)
    return returns



def getCorres(desc1, desc2, kp1, kp2):

    k = 2
    ratio = 0.75

# Brute force with ratio test
    bf = cv2.BFMatcher()
    matches = bf.knnMatch(desc1, desc2, k)
    
    good = []
    for m,n in matches:
        if m.distance < ratio*n.distance:
            good.append([m])

    leftCorres = np.float32([ kp1[m[0].queryIdx].pt for m in good ]).reshape(-1,2,1)
    rightCorres = np.float32([ kp2[m[0].trainIdx].pt for m in good ]).reshape(-1,2,1)


    returns = (leftCorres, rightCorres)
    return returns











