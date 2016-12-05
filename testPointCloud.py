
# External modules
import cv2
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl



import params
import features
import openImg
import triangulation

leftpaths, rightpaths = openImg.getFilenames()


import sys
import pdb


for m in range(1):

# get features
    imgL,imgR = openImg.getImgs(leftpaths[m], rightpaths[m])
    kp1,desc1 = features.getFeatures(imgL, [2,2])
    kp2,desc2 = features.getFeatures(imgR, [2,2])

    leftCorres, rightCorres, leftCorresidx, rightCorresidx = features.getCorres(desc1, desc2, kp1,kp2)

    x3dSave, perrFin, idxSave = triangulation.triangulate(leftCorres,rightCorres)

    if m==0:
        x3d = x3dSave
    else:
        x3d = np.concatenate((x3d,x3dSave), axis =1)

    print(m)
import pdb; pdb.set_trace()

x3d = x3d.transpose()
pos = x3d.getA()
app = QtGui.QApplication([])
w = gl.GLViewWidget()
w.opts['distance'] = 20
w.show()

pts = gl.GLScatterPlotItem(pos=pos, color=(1,1,1,1),size=10,pxMode=True)
w.addItem(pts)
originpos = np.array([0,0,0])
origin = gl.GLScatterPlotItem(pos=originpos, color=(1,0,0,1),size=30,pxMode=True)
w.addItem(origin)
raw_input('Press enter to continue: ')



