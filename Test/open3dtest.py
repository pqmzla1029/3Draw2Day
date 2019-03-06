# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 20:21:39 2019

@author: johnp
"""
import tkinter as tk
from tkinter import filedialog	
from open3d import *
from pathlib import Path
import string
f = open('Filenames.txt', 'r')
filename="pcd_files/"
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

root = tk.Tk()
filename = filedialog.askopenfilename(parent=root, initialdir="./pcd_files",
                                    title='Please select a directory')

#allow user to choose option

#filename=filename+filenameadd+".pcd"
#fileName.rstrip()
#fileName=str(filename)
print(filename)


#compoundedString.replace("\n","")
pcd = read_point_cloud(filename)

#print(pcd)
 #   print(np.asarray(pcd.points))
draw_geometries_with_editing([pcd])
