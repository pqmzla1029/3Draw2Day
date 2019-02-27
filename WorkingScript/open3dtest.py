# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *

pcd = read_point_cloud("./test_pcd/1547842929.701970000.pcd")
#print(pcd.get_max_bound())
#print(pcd.get_min_bound())

#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
