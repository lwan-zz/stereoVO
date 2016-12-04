
import params
import openImg
import cv2
import numpy as np
import triangulation
import PnP


def main():

	#get all filenames
	(fileL,fileR) = openImg.getFilenames()

	#initialize
	(imL0,imR0) = openImg.getImgs(fileL[0],fileR[0])
	(imLprev,imRprev) = openImg.getImgs(fileL[1],fileR[1])
	
	#dummy correspondences
	xL = np.matrix('1.,2.,3.,4.,5.,6.;1.5,2.5,3.5,4.5,5.5,6.5') 
	xR = np.matrix('1.,2.,3.,4.,5.,6.;1.5,2.5,3.5,4.5,5.5,6.5')

	######
	#feature detection and correspondance matching calls go here
	######

	#triangulate must be of the form 2 x N
	[x3d,projerr] = triangulation.triangulate(xL,xR)
	
	storeIdx=np.shape(x3d) #may be extraneous. used for keeping track of x3d for further concatenation

	#pass in a subset of x3d coords.

	#more dummy correspondences
	xL1 = np.matrix('1.1,2.1,3.1,4.1,5.1,6.1;1.51,2.51,3.51,4.51,5.51,6.23') 
	xR1 = np.matrix('1.8,2.8,3.73,4.4,5.2,6.4;1.53,2.54,3.2,4.3,5.3,6.62')

	a = storeIdx;
	for i in xrange(2,len(fileL)):

		(imLnext,imRnext) = openImg.getImgs(fileL[i],fileR[i])

		######
		#feature detection and correspondance matching calls go here
		######


		[x3dtemp,projerr] = triangulation.triangulate(xL,xR)
		[rec,rot,trans]=PnP.camPose(x3d,xL,projerr)

		import pdb;pdb.set_trace() #for debugging

		#x3d=hstack(x3d,x3dtemp) #this doesnt ork, but need to concatenate the 3d coordinate matrices

		storeIdx=np.shape(x3d) #may be extraneous


		#update the images for next iteration
	#	imLprev=imLnext
	#	imRprev=imRnext



#	cv2.imshow('left image',imL)
#	cv2.waitKey(0)
#	cv2.imshow('right image',imR)
#	cv2.waitKey(0)

if __name__ == '__main__':
    main()
