
# Transform matrix from Velodyne to camera then to pixels

#from open3d import *
import os
import numpy as np
#os.chdir("..")
#print(os.getcwd())
#P = np.matrix('1449.144043 0.000000 1199.158041 0.000000; 0.000 1456.590741 1036.123288 0.000000;0.0 0.0 1.000000 0.000000; 0.0 0.0 0.0 1')
P= np.loadtxt('working_data/transformations/P.txt')
"""
if(P.any==Ptry.any):
	print("Yes")
print(P)
print(Ptry)
"""
#Tcv = np.matrix('0.0 -1.0 -0.0 0.00;-0.0 0.0 -1.0 -0.45;1.0 0.0 -0.0 -0.64;0.0 0.0 0.0 1.000')
Tcv= np.loadtxt('working_data/transformations/Tcv.txt')


def conv2img(points):
	trans = np.matmul(P,Tcv)
	img = np.matmul(trans, points)
	img1=img/img[2,:]
	return img1


