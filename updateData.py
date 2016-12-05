import cv2
import numpy as np


def pointCloudTransform(points, transform)

    transformedpoints = np.zeros(points.shape[0],points.shape[1])
    for m in range(numel(points)):
        transformedpoints[m,:] = transform*points[m,:]

    return transformedPoints
            


def pointCloudUpdate(points, pointcloud)
    pointcloud = np.concatenate((pointcloud,points),axis=1)

    return pointcloud



def poseUpdate(globalPose, localPose, poses)

    globalPose = globalPose*localPose
    poses = np.concatenate(poses,localPose)

    return (globalPose, poses)

