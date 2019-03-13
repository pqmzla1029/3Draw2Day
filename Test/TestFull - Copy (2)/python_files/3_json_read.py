import json
import numpy as np
#import objectpath
import os
from open3d import *
print(os.getcwd())

with open("working_data/json_crops/cropped_1.json", "r") as wow:
    json_string = json.load(wow)
#print(json_string["bounding_polygon"])

random_array=json_string["bounding_polygon"]
myarray1 = np.asarray(random_array)


random_array=json_string["bounding_polygon"]
myarray2 = np.asarray(random_array)
#print(myarray[1])

with open("working_data/json_crops/cropped_2.json", "r") as now:
    json_string = json.load(now)

random_array=json_string["bounding_polygon"]
myarray3 = np.asarray(random_array)
#print(myarray2[:,2])

with open("working_data/ply_crops/cropped_1.ply","r") as okok:
pcd = read_point_cloud(okok)
#myarray1[:,2]=myarray3[0,2]
myarray1[:,2] = pcd.get_min_bound()
myarray2[;,2] = pcd.get_max_bound()
#myarray2[:,2]=myarray3[2,2]
#print(myarray1)

f= open("working_data/bounding_data/bound_data.txt","w+")
r = myarray1.ndim
for i in range (0,4):
    for j in range (0,3):
        f.write(str(myarray1[i,j])+' ')
    f.write('1')    
    f.write('\r\n')
for i in range (0,4):
    for j in range (0,3):
        f.write(str(myarray2[i,j])+' ')
    f.write('1')   
    f.write('\r\n')
f.close() 
