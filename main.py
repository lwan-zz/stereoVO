
import cv2
import numpy as np

#custom modules
import params
import openImg
import triangulation
import PnP
import features
import svo


def main():


	#get all filenames
	(fileL,fileR) = openImg.getFilenames()
	for i in xrange(len(fileL)-1):
		(rot,trans,x3d)=svo.svoExecute(fileL[i],fileR[i],fileL[i+1],fileR[i+1])

		if i==0:
			x3d_Saved=x3d
		else:
			x3d_Saved=np.concatenate((x3d_Saved,x3d),axis=1)

		#import pdb;pdb.set_trace() #for debugging

if __name__ == '__main__':
    main()
