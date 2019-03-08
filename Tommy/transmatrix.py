
# Transform matrix from Velodyne to camera then to pixels

from open3d import *
import numpy as np
P = np.matrix('1449.144043 0.000000 1199.158041 0.000000; 0.000 1456.590741 1036.123288 0.000000;0.0 0.0 1.000000 0.000000; 0.0 0.0 0.0 1')
Tcv = np.matrix('0.0 -1.0 -0.0 0.00;-0.0 0.0 -1.0 -0.45;1.0 0.0 -0.0 -0.64;0.0 0.0 0.0 1.000')
def conv2img(points):
	trans = np.matmul(P,Tcv)
	img = np.matmul(trans, points)
	img1=img/img[2,:]
	return img1


