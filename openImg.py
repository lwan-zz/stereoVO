import numpy as np #use as np.____
import cv2
import params
import os



def getFilenames():

    fullpathL=[None]*params.numPics
    fullpathR=[None]*params.numPics

    pathL = params.IMGLOCATION+'/image_02/data/'
    pathR = params.IMGLOCATION+'/image_03/data/'

    for i in xrange(params.numPics):
        if i < 10:
            fullpathL[i] = pathL+'000000000'+str(i) +'.png'
            fullpathR[i] = pathR+'000000000'+str(i) +'.png'
        elif i >= 10 and i < 100:
            fullpathL[i] = pathL+'00000000'+str(i) +'.png'
            fullpathR[i] = pathR+'00000000'+str(i) +'.png'
        else:
            fullpathL[i] = pathL+'0000000'+str(i) +'.png'
            fullpathR[i] = pathR+'0000000'+str(i) +'.png'
    return (fullpathL, fullpathR)

def getImgs(fL,fR):

    imgL=cv2.imread(fL,0)
    imgR=cv2.imread(fR,0)

    return (imgL, imgR)
