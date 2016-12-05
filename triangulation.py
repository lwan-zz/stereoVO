import numpy as np #use as np.____
import cv2
import params



def triangulate (x2dL,x2dR): #x2d's must be of size 2 x N

	PL=params.P02
#	PL=np.eye(3,4)
	PR=params.P03

	x3d = cv2.triangulatePoints(PL,PR,x2dL,x2dR) #x3d will be of size 4 x N
	
	x3d /= x3d[3] #forcing homogeneity

	x3d = np.matrix(x3d)

	#calculating reprojection error between collected feature points and the reprojected 3d coord into 2d
	#matrix multiplication
	phatL = PL*x3d
	phatR = PR*x3d

	phatL /= phatL[2]
	phatR /= phatR[2] 

	x3d=x3d[:3]
	

	#might not be completely necessary.
	phatL = np.array(phatL)
	phatR = np.array(phatR)


#	np.vstack can add another row to a matrix
	pErrUnfilt = np.sum(np.power((x2dL-phatL[:2]),2) + np.power((x2dR-phatR[:2]),2),axis=0)


	pErrSave=np.zeros((pErrUnfilt.shape[0])) #302 
	idxSave = np.zeros((pErrUnfilt.shape[0]))
	x3dSave=np.matrix(np.zeros((x3d.shape[0],x3d.shape[1]))) #4,302

	x2dL=np.matrix(x2dL)
	x2dR=np.matrix(x2dR)
	x2dLSave=np.matrix(np.zeros((x2dL.shape[0],x2dL.shape[1])))
	x2dRSave=np.matrix(np.zeros((x2dR.shape[0],x2dR.shape[1])))

	a=1
	for i in xrange(pErrUnfilt.shape[0]):
		if pErrUnfilt[i] < 10:
			pErrSave[a] = pErrUnfilt[i]
			idxSave[a]=i
#			x3dSave[:4,a] = x3d[:4,i]
#			x2dLSave[:,a] = x2dL[:,a]
#			x2dRSave[:,a] = x2dR[:,a]
			a+=1

	pErrSave=pErrSave[:np.amax(np.nonzero(pErrSave))]
#	x3dSave=x3dSave[:4,:np.amax(np.nonzero(pErrSave))]
#	x2dLSave=x2dLSave[:,:np.amax(np.nonzero(pErrSave))]
#	x2dRSave=x2dRSave[:,:np.amax(np.nonzero(pErrSave))]
	
	pErrFin=np.sum(pErrSave)

#	import pdb;pdb.set_trace() #for debugging


	return (x3d,pErrFin,idxSave)