# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *

pcd = read_point_cloud("file2.pcd")
#print(pcd.get_max_bound())
#print(pcd.get_min_bound())

#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])

vol = read_selection_polygon_volume("cropped.json")
chair = vol.crop_point_cloud(pcd)
draw_geometries([chair])
