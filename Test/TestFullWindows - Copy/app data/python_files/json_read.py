import json
import numpy as np
#import objectpath
import os
from open3d import *
#os.chdir("..")
print(os.getcwd())

def get_values(directoryename):
	with open("working_data/json_crops/"+directoryename+"/cropped_1.json", "r") as wow:
	    json_string = json.load(wow)
	#print(json_string["bounding_polygon"])

	random_array=json_string["bounding_polygon"]
	myarray1 = np.asarray(random_array)


	random_array=json_string["bounding_polygon"]
	myarray2 = np.asarray(random_array)
	#print(myarray[1])

	#with open("working_data/json_crops/cropped_2.json", "r") as now:
	#    json_string = json.load(now)

	random_array=json_string["bounding_polygon"]
	myarray3 = np.asarray(random_array)
	#print(myarray2[:,2])
	pcd = read_point_cloud("working_data/ply_crops/cropped_1.ply")

	maxval=pcd.get_max_bound()
	minval=pcd.get_min_bound()
	myarray1[:,2] = maxval[2]
	#myarray2[:,2] = minval[2]
	myarray2[:,2]=-1.75
	#print(myarray3[0,2])
	#print(myarray3[2,2])
	#myarray1[:,2]=myarray3[0,2]
	#myarray2[:,2]=myarray3[2,2]
	#print(myarray1)
	return myarray1,myarray2,myarray3

def write_values_convert(myarray1,myarray2,myarray3):
	#print(myarray1)
	f= open("working_data/bounding_data/bound_data.txt","w+")
	r = myarray1.ndim
	#print(r)
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

def write_values_json(filename,myarray1,myarray2,myarray3,annotation_name):
	#print(myarray1)
	f= open("working_data/bounding_data/3D/"+filename+".txt","a+")
	r = myarray1.ndim
	#print(r)
	f.write(annotation_name)
	for i in range (0,4):
		for j in range (0,3):
			f.write(" "+str(myarray1[i,j]))
	for i in range (0,4):
		for j in range (0,3):
			f.write(" "+str(myarray2[i,j]))
	f.write("\n")
	f.close() 

def main(filename,annotation_name):
	directoryname=filename
	myarray1,myarray2,myarray3=get_values(directoryname)
	write_values_json(filename,myarray1,myarray2,myarray3)
	write_values_convert(myarray1,myarray2,myarray3,annotation_name)

#main()
