import numpy as np
import cv2

import params
import openImg
import triangulation
import PnP
import features

def idxMerge(matchKeptL_St,matchKept_3d,x3dprev,corLnext_T,matchKeptPrev_T,matchKeptNext_T):
	#Find the overlapping indices

	#find the keypoints from LEFT CAM at TIME=K-1 that were preserved all the way through 3D coordinate generation
	comparePrev_T=[]
	for i in xrange(len(matchKept_3d)):
		comparePrev_T.append(matchKeptL_St[0,int(matchKept_3d[i])])

	comparePrev_T=np.array(comparePrev_T)
	finPrev_T=[]
	finNext_T=[]


	#find where the PREVIOUS LEFT CAMS intersect when finding the 3d coordinates at TIME=K-1 and finding correspondences at TIME=K
	for j in xrange(matchKeptPrev_T.shape[1]):
		#print np.where(comparePrev_T==matchKeptPrev_T[0,j])[0]
		#print j
		if not np.any(np.where(comparePrev_T==matchKeptPrev_T[0,j])[0]) == False:
			finPrev_T.append(matchKeptPrev_T[0,j])
			finNext_T.append(matchKeptNext_T[0,j])
	

	comparePrev_T=np.array(comparePrev_T)
	
	x3dprev_final = np.matrix(np.zeros((x3dprev.shape[0],len(finPrev_T))))
	x2dnext_final = np.matrix(np.zeros((corLnext_T.shape[0],len(finNext_T))))
	for k in xrange(len(finPrev_T)):
		x3dIdx = (((np.where(comparePrev_T==finPrev_T[k]))[0])[0])
		x2dIdx = (((np.where(matchKeptNext_T==finNext_T[k]))[0])[0])
		x3dprev_final[:,k] = x3dprev[:,x3dIdx]
		x2dnext_final[:,k] = np.matrix(corLnext_T)[:,x2dIdx]

	return (x3dprev_final,x2dnext_final)

def svoExecute(fpathL1,fpathR1,fpathL2,fpathR2):

	#initialize
	(imLprev,imRprev) = openImg.getImgs(fpathL1,fpathR1)
	(imLnext,imRnext) = openImg.getImgs(fpathL2,fpathR2)

	size=[2,2]

	#get key points
	kpLprev,descLprev = features.getFeatures(imLprev,size)
	kpRprev,descRprev = features.getFeatures(imRprev,size)

	#correspondences
	corLprev_St, corRprev_St,matchKeptL_St,matchKeptR_St = features.getCorres(descLprev,descRprev,kpLprev,kpRprev)

	#triangulate must be of the form 2 x N
	[x3dprev,pErrPrev,matchKept_3d] = triangulation.triangulate(corLprev_St,corRprev_St)
	
	#Get temporal correspondences
	kpLnext,descLnext = features.getFeatures(imLnext,size)
 
	corLprev_T,corLnext_T,matchKeptPrev_T,matchKeptNext_T = features.getCorres(descLprev,descLnext,kpLprev,kpLnext)
	
	(x3dprev_final,x2dnext_final)=idxMerge(matchKeptL_St,matchKept_3d,x3dprev,corLnext_T,matchKeptPrev_T,matchKeptNext_T)

	#Get updated camera pose
	[rot,trans]=PnP.camPose(x3dprev_final,x2dnext_final,pErrPrev)

#	a = storeIdx;	
#	for i in xrange(2,len(fileL)):

#		(imLnext,imRnext) = openImg.getImgs(fileL[i],fileR[i])

		######
		#feature detection and correspondance matching calls go here
		######


#		[x3dtemp,projerr] = triangulation.triangulate(xL,xR)
#		[rec,rot,trans]=PnP.camPose(x3d,xL,projerr)

#	import pdb;pdb.set_trace() #for debugging

		#x3d=hstack(x3d,x3dtemp) #this doesnt work, but need to concatenate the 3d coordinate matrices

#		storeIdx=np.shape(x3d) #may be extraneous


		#update the images for next iteration
	#	imLprev=imLnext
	#	imRprev=imRnext



#	cv2.imshow('left image',imL)
#	cv2.waitKey(0)
#	cv2.imshow('right image',imR)
#	cv2.waitKey(0)
	return (rot,trans,x3dprev_final)