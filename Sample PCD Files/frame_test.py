#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image, ImageTk
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Style
from open3d import *

        


def main():

    #root = Tk()
    #root.geometry('300x280+300+300')
    #app = Example()
    pcd = read_point_cloud('1547842929.701970000.pcd')
    bard = draw_geometries_with_editing([pcd])
    root2 = Tk()
    #root2.geometry('300x280+300+300')
    root2.wait_visibility(root2)
    root2.wm_attributes('-alpha', 0.3)
    root2.attributes("-fullscreen", True)
    root2.mainloop()



    #root.mainloop()


if __name__ == '__main__':
    main()

