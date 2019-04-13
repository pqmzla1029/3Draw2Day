import numpy as np

import os
#os.chdir("..")
import transmatrix
#print(os.getcwd())
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

def convert_to_image(filename,annotation_name):
	
	a = np.loadtxt('working_data/bounding_data/bound_data.txt')


	a = np.transpose(np.asmatrix(a))



	x = transmatrix.conv2img(a)
	#print(x)

	#lengthimg=
	x=np.around(x,decimals=3)
	f=open("working_data/bounding_data/"+str(filename)+".txt",'a+')
	#for line in x:
	#np.savetxt(f, line, fmt='%.2f')
	f.write(annotation_name)
	for i in range(0,8):
		f.write(" "+str(x[0,i]))
		f.write(" "+str(x[1,i]))
		#np.savetxt(f, x[i,:], fmt='%.2f')
	f.write("\n")
	
	#x = transmatrix.conv2img(a)

def main(annotationname):
	filename="frame0001"
	annotation_name=annotationname
	convert_to_image(filename,annotation_name)
	#print("done")

#main()

