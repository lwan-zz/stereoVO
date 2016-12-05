
import cv2
import numpy as np

#custom modules
import params
import openImg
import triangulation
import PnP
import features
import svo
import updateData as data
import visualize as vis



def main():


    #get all filenames
    (fileL,fileR) = openImg.getFilenames()
    for i in xrange(10):
#        import pdb;pdb.set_trace()
        (rot,trans,x3d)=svo.svoExecute(fileL[i],fileR[i],fileL[i+1],fileR[i+1])
        print(i)

        transform = data.makeTransform(rot,trans)

        if i==0:
            x3d_Saved=x3d
            pos = np.array([[0,0,0]])
            newpos = data.posUpdate(pos,transform)
            pos = np.concatenate((pos,newpos),axis =0)
            prevpos = newpos

        else:
            x3d_Saved=np.concatenate((x3d_Saved,x3d),axis=1)
            newpos = data.posUpdate(prevpos,transform)
            pos = np.concatenate((pos,newpos),axis =0)
            prevpos = newpos


    import pdb;pdb.set_trace() #for debugging
if __name__ == '__main__':
    main()
