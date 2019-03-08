# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *
import numpy as np
import transmatrix

pcd = read_point_cloud("cropped_1.ply")
#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
#print(np.asarray(pcd.points))
draw_geometries([pcd])
#np.savetxt("text.csv", np.asarray(pcd.points), delimiter = ',')
print(pcd.get_max_bound()-pcd.get_min_bound())
print(pcd.get_max_bound())
print(pcd.get_min_bound())

ok = np.matrix()

x = transmatrix.conv2img(ok)
