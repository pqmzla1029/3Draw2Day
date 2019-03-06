# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""

from open3d import *
from pathlib import Path
import string
f = open('Filenames.txt', 'r')
filenamex=""
#fileName=f.readline()
temp = f.read().splitlines()
'''
for line in f:
    fileName=line#+"\b.pcd"
    fileName.rstrip()
    print (fileName)
    #break
    #compoundedString=""
    #fh = open(fileName, 'r')
    #for line in fh:
    #    compoundedString=compoundedString+line
'''

#allow user to choose option
choiceopt=1
filename=str(temp[choiceopt])+".pcd"
#fileName.rstrip()
#fileName=str(filename)
print(filename)

filename1="file2.pcd"

#compoundedString.replace("\n","")
pcd = read_point_cloud(filename)

#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
