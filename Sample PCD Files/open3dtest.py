# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *

pcd = read_point_cloud("file1.pcd")
#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
