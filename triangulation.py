import numpy as np #use as np.____
import cv2
import params



def triangulate (x2dL,x2dR): #x2d's must be of size 2 x N

	PL=params.P02
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

	#might not be completely necessary.
	phatL = np.array(phatL)
	phatR = np.array(phatR)
	print x2dL
	print phatL
#	np.vstack can add another row to a matrix
	perror = np.sum(np.sum(np.power((x2dL-phatL[:2]),2) + np.power((x2dR-phatR[:2]),2)))

	return (x3d,perror)