import tkinter as tk
from tkinter import filedialog	
from open3d import *
#root = tk.Tk()
def noobs():
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

noobs()
