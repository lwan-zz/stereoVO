import cv2
import numpy as np
from pyqtgraph.Qt import QtCore, QtGui
import pyqtgraph.opengl as gl

import features
import openImg
import triangulation


def update(globalpose, transformedPoints):
    global pts, pose

    pts =  transformedPoints.transpose()
    pts = pts.getA()
    
    pose  = globalpose
    
    plots.setData(pos = pts)
     
#    return (pose, pts)


def vis(pos):
    app = QtGui.QApplication([])
    w = gl.GLViewWidget()
    w.opts['distance'] = 100
    w.show()
    
    plots = gl.GLScatterPlotItem(pos=pos, color=(1,1,1,1),size=10,pxMode=True)

    w.addItem(pts)
    t = QtCore.QTimer()
    t.timeout.connect(update)
    t.start(50)



