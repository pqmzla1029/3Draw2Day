
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *
import numpy as np
import transmatrix
import os
print(os.getcwd())
#pcd = read_point_cloud("cropped_1.ply")
#print(pcd)
 #   print(np.asarray(pcd.points))
# draw_geometries_with_editing([pcd])
# #print(np.asarray(pcd.points))
# draw_geometries([pcd])
# #np.savetxt("text.csv", np.asarray(pcd.points), delimiter = ',')
# print(pcd.get_max_bound()-pcd.get_min_bound())
# print(pcd.get_max_bound())
# print(pcd.get_min_bound())


a = np.loadtxt('working_data/bounding_data/bound_data.txt')


a = np.transpose(np.asmatrix(a))



x = transmatrix.conv2img(a)
print(x)

with open('working_data/bounding_data/image_matrix_bound.txt','w+') as f:
    for line in x:
        np.savetxt(f, line, fmt='%.2f')

#x = transmatrix.conv2img(a)
