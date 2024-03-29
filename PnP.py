import params
import numpy as np
import cv2

def camPose(x3d,x2dL,perror):
	#convert from matrix to array
	x3d=np.matrix(x3d)
	x2dL=np.matrix(x2dL)

	#### these are not used. however they might be useful elsewhere.
	#### rot and trans are actually outputs for the solvepnp
	#### formatting of the documentation confused me
	#rotation and translation between left and right cameras
	Rot = np.matrix.transpose(params.R02)*params.R03,(1,9)
	#Trans = np.asarray(params.t03).T.tolist()-params.R03/params.R02*np.asarray(params.t02).T.tolist()
	Trans = params.t03-params.R03/params.R02*params.t02

	
	#homo = np.matrix('0,0,0,1')
	#P2=np.concatenate((params.P02,homo),axis=0) #make projection matrix homogeneous
	
	x3d_PnP = np.matrix.transpose(x3d)
	x2dL_PnP = np.matrix.transpose(x2dL)


	dist = np.zeros((1,5))
	#import pdb;pdb.set_trace() #for debugging
	(ret,rotV,transV) = cv2.solvePnP(x3d_PnP,x2dL_PnP,np.eye(3),dist)
	[rotMat,jac]=cv2.Rodrigues(rotV)
	#conduct bundle adjustment for rectified rotation and translation matrices
	#rotRect,transRect) = bundleAdjust(perror,rotMat,transV)

	return (rotMat,transV)
	#return (rotRect,transRect)

def bundleAdjust(perror,rot,trans):
	return 0
