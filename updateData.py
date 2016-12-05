import cv2
import numpy as np

def makeTransform(rot,trans):
    transform = np.concatenate((rot,trans), axis=1)
    transform = np.asmatrix(transform)
    lastRow = np.matrix([0,0,0,1])
    transform = np.concatenate((transform,lastRow), axis=0)

    return transform


def pointCloudTransform(points, transform):

    transformedpoints = np.zeros(points.shape[0],points.shape[1])
    for m in range(numel(points)):
        transformedpoints[m,:] = transform*points[m,:]

    return transformedPoints
            


def pointCloudUpdate(points, pointcloud):
    pointcloud = np.concatenate((pointcloud,points),axis=1)

    return pointcloud



def posUpdate(pos, transform):
    # input array, output matrix
#    import pdb;pdb.set_trace()
    pos =  np.asmatrix(pos)
    pos = pos.T
    one = np.matrix(1)
    pos = np.concatenate((pos,one),axis=0)
    newpos = transform*pos
    newpos = newpos[0:3,:]
    newpos = newpos.T
    newpos = np.asarray(newpos)
#    newpos = newpos[0]
#   output array
    return (newpos)

