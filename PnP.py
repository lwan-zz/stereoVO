import params
import numpy as np
import cv2

def camPose(x3d,x2dL,perror):
	#convert from matrix to array
	x3d=np.array(x3d)
	x2dL=np.array(x2dL)

	#rotation and translation between left and right cameras
	Rot = np.reshape(np.asarray(params.R02).T.tolist()*params.R03,(1,9))

	import pdb;pdb.set_trace() #for debugging

	#Trans = np.asarray(params.t03).T.tolist()-params.R03/params.R02*np.asarray(params.t02).T.tolist()
	Trans = params.t03-params.R03/params.R02*params.t02

	distCoef = np.zeros(4)
	#homo = np.matrix('0,0,0,1')
	#P2=np.concatenate((params.P02,homo),axis=0) #make projection matrix homogeneous
	
	x3d_PnP = np.array(np.asarray(x3d[:3]).T.tolist())
	x2dL_PnP = np.array(np.asarray(x2dL).T.tolist())

	import pdb;pdb.set_trace() #for debugging

	(ret,rot,trans) = cv2.solvePnP(x3d_PnP,x2dL_PnP,params.P02,distCoef=None,Rot,Trans,True)

	#conduct bundle adjustment for rectified rotation and translation matrices
	(rotRect,transRect) = bundleAdjust(perror,rot,trans)

	return (rot,trans)
	#return (rotRect,transRect)

def bundleAdjust(perror,rot,trans):
	return 0
