
import cv2
import numpy as np

#custom modules
import params
import openImg
import triangulation
import PnP
import features


def main():

	#get all filenames
	(fileL,fileR) = openImg.getFilenames()

	#initialize
	(imL0,imR0) = openImg.getImgs(fileL[0],fileR[0])
	(imLprev,imRprev) = openImg.getImgs(fileL[0],fileR[0])
	(imLnext,imRnext) = openImg.getImgs(fileL[1],fileR[0])

	size=[3,3]


	#get key points
	#kpL0,descL0 = features.getFeatures(imL0,size)
	#kpR0,descR0 = features.getFeatures(imR0,size)
	kpLprev,descLprev = features.getFeatures(imLprev,size)
	kpRprev,descRprev = features.getFeatures(imRprev,size)

	#correspondences
	#corL0, corR0 = features.getCorres(descL0,descR0,kpL0,kpR0)
	corLprev_St, corRprev_St,matchKeptL_St,matchKeptR_St = features.getCorres(descLprev,descRprev,kpLprev,kpRprev)
	
	#changing matrix from 3D to 2D for correspondences
	#corL0 = np.matrix.transpose(np.concatenate((corL0[:,0],corL0[:,1]),axis=1))
	#corR0 = np.matrix.transpose(np.concatenate((corR0[:,0],corR0[:,1]),axis=1))

	corLprev_St = np.matrix.transpose(np.concatenate((corLprev_St[:,0],corLprev_St[:,1]),axis=1))
	corRprev_St = np.matrix.transpose(np.concatenate((corRprev_St[:,0],corRprev_St[:,1]),axis=1))

	#triangulate must be of the form 2 x N
	#[x3d0,perr0] = triangulation.triangulate(corL0,corR0)
	[x3dprev,pErrPrev,matchKept_3d] = triangulation.triangulate(corLprev_St,corRprev_St)
	
	#Get temporal correspondences
	kpLnext,descLnext = features.getFeatures(imLnext,size)
 
	corLprev_T,corLnext_T,matchKeptPrev_T,matchKeptNext_T = features.getCorres(descLprev,descLnext,kpLprev,kpLnext)

	#Find the overlapping indices
	#matchKeptNext_T, matchKeptL_St need to be overlapping with each other
	
	
	#find the keypoints from LEFT CAM at TIME=K-1 that were preserved all the way through 3D coordinate generation
	for i in xrange(len(matchKept_3d)):
		comparePrev_T= matchKeptL_St[matchKept_3d[i]]




	#Get updated camera pose
	#[rot,trans]=PnP.camPose(x3dprev_OL,corLnext_OL,pErrPrev)

	import pdb;pdb.set_trace() #for debugging

	storeIdx=np.shape(x3d) #may be extraneous. used for keeping track of x3d for further concatenation

	a = storeIdx;	
	for i in xrange(2,len(fileL)):

		(imLnext,imRnext) = openImg.getImgs(fileL[i],fileR[i])

		######
		#feature detection and correspondance matching calls go here
		######


		[x3dtemp,projerr] = triangulation.triangulate(xL,xR)
		[rec,rot,trans]=PnP.camPose(x3d,xL,projerr)

		import pdb;pdb.set_trace() #for debugging

		#x3d=hstack(x3d,x3dtemp) #this doesnt work, but need to concatenate the 3d coordinate matrices

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
