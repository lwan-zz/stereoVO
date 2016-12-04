import numpy as np #use as np.____
import numpy as np #use as np.____
import cv2
import params
import os

pathL = params.IMGLOCATION+'/image_02/data/'
pathR = params.IMGLOCATION+'/image_03/data/'
tstampPathL = params.IMGLOCATION+'/image_02/timestamps.txt'
tstampPathR = params.IMGLOCATION+'/image_03/timestamps.txt'
img=[]

tstampL = open(tstampPathL,'r')
tstampR = open(tstampPathR,'r')

#for i in 
#leftcam=cv2.imread(params.IMGLOCATION)