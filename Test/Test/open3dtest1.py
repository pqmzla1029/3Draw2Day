
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *
import numpy as np
#import transmatrix

#pcd = read_point_cloud("1547842929.701970000.pcd")
#draw_geometries_with_editing([pcd])
#print(pcd)
 #   print(np.asarray(pcd.points))
# draw_geometries_with_editing([pcd])
# #print(np.asarray(pcd.points))
# draw_geometries([pcd])
# #np.savetxt("text.csv", np.asarray(pcd.points), delimiter = ',')
# print(pcd.get_max_bound()-pcd.get_min_bound())
# print(pcd.get_max_bound())
# print(pcd.get_min_bound())
def load_view_point(pcd, filename):
    vis = VisualizerWithEditing()
    vis.create_window()
    ctr = vis.get_view_control()
    param = read_pinhole_camera_parameters(filename)
    vis.add_geometry(pcd)
    ctr.convert_from_pinhole_camera_parameters(param)
    vis.run()
    vis.destroy_window()


pcd = read_point_cloud("1547842929.701970000.pcd")
load_view_point(pcd, "viewpoint1.json")
#a = np.loadtxt('bound_data.txt')


#a = np.transpose(np.asmatrix(a))



#x = transmatrix.conv2img(a)
#print(x)

#x = transmatrix.conv2img(a)
