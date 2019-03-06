# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *
import numpy as np

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
print("Let\'s draw a cubic using LineSet")
points = [[0,0,0],[1,0,0],[0,1,0],[1,1,0],
          [0,0,1],[1,0,1],[0,1,1],[1,1,1]]
lines = [[0,1],[0,2],[1,3],[2,3],
         [4,5],[4,6],[5,7],[6,7],
         [0,4],[1,5],[2,6],[3,7]]
colors = [[1, 0, 0] for i in range(len(lines))]
line_set = LineSet()
line_set.points = Vector3dVector(points)
line_set.lines = Vector2iVector(lines)
line_set.colors = Vector3dVector(colors)
draw_geometries([line_set])