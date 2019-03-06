# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *

pcd = read_selection_polygon_volume("ScreenCamera_2019-03-06-15-45-48.json")
#print(pcd.get_max_bound())
#print(pcd.get_min_bound())

#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
