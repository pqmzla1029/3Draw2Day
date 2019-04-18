import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import numpy as np
import os
import open3d as op3
import matplotlib.cm as cm
import copy_data as cpd
import json_read as jsr
import convert_to_image_frame as ctif
from random import randint
import ntpath
import pandas as pd
from tkinter import filedialog
import tkinter as tk

#---------------------------------------Open3D custom viewpoints----------------------------------------------

def load_view_point(pcd, filename):
    vis = op3.VisualizerWithEditing()
    vis.create_window()
    ctr = vis.get_view_control()
    param = op3.read_pinhole_camera_parameters(filename)
    vis.add_geometry(pcd)
    ctr.convert_from_pinhole_camera_parameters(param)
    vis.run()
    vis.destroy_window()

#---------------------------------------PySimpleGUI Add Matplot----------------------------------------------

def draw_figure(canvas, figure, loc = (0,0)):

    figure_canvas_agg = FigureCanvasAgg(figure) 
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo

#---------------------------------------Matlab Plotting Image----------------------------------------------

#print(placeholder_array)
def set_plot( function):
    print(os.getcwd())
    im = np.array(Image.open('image_files/'+function+'.jpg'), dtype=np.uint8)

    # Create figure and axes
    fig,ax = plt.subplots(1,figsize=(7.5,6))#,figsize=(20,10))
    #fig,ax = plt.subplots(1,figsize=(10,8))#,figsize=(10,8))
    # Display the image
    ax.imshow(im)
    global figure_w, figure_h
    exists = os.path.isfile("working_data/bounding_data/2D/"+function+".txt")
    if exists:
        x = np.loadtxt("working_data/bounding_data/2D/"+function+".txt", skiprows=0, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
        size_of_array=x.shape[0]
        a = np.zeros([2,16])
        color_array = cm.rainbow(np.linspace(0, 1, size_of_array))
        len_a=x.shape
        if x.ndim > 1: a = x
        else:
            a[0] = x
            size_of_array = 1
        
        for index_item in range(0,size_of_array):
                x_number_values= np.zeros(5)
                y_number_values= np.zeros(5)
                
                count=0
                for i in range(0,5):
                        x_number_values[i] = a[index_item][count%8]
                        y_number_values[i] = a[index_item][count%8+1]
                        count=count+2
                plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])
                #plt.show()

                start=count-2
                count=8
                for i in range(0,5):
                        x_number_values[i] = a[index_item,count%8+start]
                        y_number_values[i] = a[index_item,count%8+1+start]
                        count=count+2
                plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])

                count=0
                inter=8
                for i in range(0,4):
                    x_number_values = [a[index_item,count],a[index_item,count+inter]]
                    y_number_values = [a[index_item,count+1],a[index_item,count+1+inter]]
                    #print(x_number_values, y_number_values)
                    plt.plot(x_number_values, y_number_values, linewidth=3, color=color_array[index_item])
                    count=count+2

    ax.set_title(function+" Plot")
    figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
    return fig



#-------------------------------------------Begin--------------------------------------------------


#Uncomment Following Line to Begin Debug Process
os.chdir("..")
print(os.getcwd())
logodirname="Executable Requirements/Logo/Pencil-icon.png"
icondirname="Executable Requirements/Logo/Pencil-icon.ico"
global_frame=0

df=pd.read_csv('working_data/links/PCD-ImageMatches.txt', sep=",", header=None)
array_images=df[1]
size_of_array=array_images.shape[0]
placeholder_array = ["" for x in range(size_of_array)]
#print(array_images[0])
for i in range(size_of_array):
    placeholder_array[i]=array_images[i].replace('.jpg', '')
function=placeholder_array[0]
fig=set_plot(function)



#-----------------------------------GUI Build and Display ------------------------------------------

bcolor = '#F0F8FF'
wcolor = ('#F0F8FF', '#F0F8FF')
#sg.ChangeLookAndFeel('GreenTan')
sg.ChangeLookAndFeel(bcolor)
#sg.ChangeLookAndFeel('SandyBeach')
#sg.SetOptions (font =('Calibri',12,'bold'))

menu_def = [['&File', ['&Open', 'E&xit' ]],
                #['&Edit', ['&Paste', ['Special', 'Normal',], 'Undo'],],
                #['&Toolbar', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&View Help', '&About']],]

column1 = [[sg.Text('Camera Display', font = ('Calibri', 18, 'bold'), background_color='#F0F8FF', pad=(250, 15))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')]#,
           ]

column2=[
    [sg.Image(logodirname,size=(60,60), background_color=bcolor),sg.Text('       3Draw2Day       ', background_color=bcolor, font = ('Calibri', 18, 'bold'))],
    [sg.Text('_'  * 40, background_color=bcolor)],
    [sg.Text('Select type of object to annotate :', background_color=bcolor, font = ('Calibri', 14, 'bold'))],        
    [sg.InputCombo(['car', 'bike', 'truck','person'], size = (8, 4), key = '_annoname_')],      
    [sg.ReadButton('Open PCD')],
    [sg.Text('_'  * 40, background_color=bcolor)]
    ]

column3 = [
           [sg.InputCombo(placeholder_array, size = (10, 4), key = '_function_', background_color=bcolor, pad=(250, 15)),sg.ReadButton('Redraw Plot')],
           [sg.Text('_'  * 40,background_color=bcolor)]
           ]

column4 = [[sg.Listbox(values=placeholder_array, change_submits=True, size=(28, len(placeholder_array)), key='func')],
               [sg.T(' ' * 12, background_color=bcolor), sg.Exit('End',size=(5, 2))]]          

#i_vid = r'pcd_files/1547842929.701970000.pcd'
#extracolumn=[
    #[sg.Listbox(values=('crop_file1', 'crop_file2', 'crop_file3'), size=(30, 3))],     
    #[sg.Spin(values=('No Comment', 'Comment'), initial_value='Select')],
    #[sg.Multiline(default_text='Enter Comments Here', size=(35, 3), key = '_comment_'),sg.Submit()],
    #[sg.ReadButton('Meh')],
    #[sg.Text('_'  * 40)],
    #[sg.Text('File'), sg.In(i_vid,size=(30,1), key='input')],#sg.ReadButton('_filebrowse_')],
    #[sg.Button('Exit', image_data=image_file_to_bytes(orange64, (100,50)), font='Any 15', pad=(0,0), key='Open PCD'),],
    #[sg.Spin([sz for sz in range (1,5)], initial_value =1, size = (2,1), key = '_spin_'),
    #sg.Text('Amplitude', size = (10, 1), font = ('Calibri', 12, 'bold'))],
    #[sg.InputCombo(placeholder_array, size = (10, 4), key = '_function_', background_color=bcolor, pad=(250, 15)),sg.ReadButton('Redraw Plot')],
    #sg.Text('Function', size = (10, 1),font = ('Calibri', 12, 'bold'))],
    #[sg.Text('_'  * 40,background_color=bcolor)],
    #[sg.InputCombo(('PCD to Image', 'Image to PCD'), size=(20, 3))],     
    #[sg.Text('Choose A PCD to Annotate', size=(35, 1))],#sg.Text('Help  \n 1. Z - Lock in z-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n X - Lock in x-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n Q - Quit')],                  
    #[sg.Text('3D Annotation Tool', size=(30, 1), font=("Helvetica", 25)),sg.Column(column1, background_color='#d3dfda')],
    #[sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
    #sg.InputText('Default Folder'), sg.FolderBrowse()],      
    #[sg.Submit(), sg.Cancel()]
    #]

#column5=[[sg.Column(column2, background_color=bcolor)],[sg.Column(column3, background_color=bcolor)]]
column5=[[sg.Column(column2, background_color=bcolor)],
         [sg.Column(column4, background_color=bcolor)]]

  
layout = [
    
    [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
    [sg.Column(column5, background_color=bcolor,),sg.Column(column1, background_color=bcolor)],
    [sg.Text('Status Bar', relief=sg.RELIEF_SUNKEN, size=(55,1),  pad=(0,3),key='_status_')]
]
#window = sg.Window('Mobile Robotics', default_element_size=(40, 1)).Layout(layout)
window = sg.Window('3Draw2Day', force_toplevel = True,icon=icondirname, return_keyboard_events=True, use_default_focus=True, grab_anywhere=False).Layout(layout).Finalize()
window.Finalize()
fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
#button, values = window.Read()
#sg.Popup(button, values)

#------------------------------------Conditional Check--------------------------------------------------


os.chdir("pcd_files")
print(os.getcwd())

while True:
    global_frame=0
    #print("trial")
    button, value = window.Read()#(timeout=0)
    print(button)
    if button == 'Redraw Plot':
        print(os.getcwd())
        currentloc=os.getcwd()
        os.chdir("..")
        print(os.getcwd())
        #amp = int(value['_spin_'])
        
        #PCD-ImageMatches
        function = value['_function_']
        fig=set_plot(function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
        #os.chdir(currentloc)
        os.chdir("pcd_files")
        os.chdir("Wow")

    if button == '_filebrowse_':
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(parent=root, initialdir="./pcd_files", title='Please select a directory')
        print(filename)

    if button == 'Open PCD' or button == 'Open':
        os.chdir("..")
        print(os.getcwd())
        root = tk.Tk()
        root.withdraw()
        directoryname = filedialog.askopenfilename(parent=root, initialdir="./pcd_files", title='Please select a directory')
        filename=directoryname
        
        #print("Test Begin")
        #if(filename!=""):
        try:
            filename=ntpath.basename(directoryname)
            #directoryname = value['input']
            #filename=filename.replace('.pcd', '')
            #print(filename)
            df=pd.read_csv('working_data/links/PCD-ImageMatches.txt', sep=",", header=None)
            df1=df
            df1.set_index(0, inplace=True)
            df1=df1.loc[filename, : ]
            function=df1[1]
            print(function)
            filename=filename.replace('.pcd', '')
            function=function.replace('.jpg', '')
            #amp = int(value['_spin_'])
            #function = value['_function_']
            pcd = op3.read_point_cloud(directoryname)
            print("Open file "+filename)
            destinationf="working_data/viewpoint/viewpoint.json"
            load_view_point(pcd,destinationf)
            exists = os.path.isfile("cropped_1.ply")
            if exists:
                
                print("Done cutting")
                annotationname = value['_annoname_'].strip()
                
                cpd.main(filename,annotationname)
                print("Done 1")
                jsr.main(filename,annotationname)
                print("Done 2")
                ctif.main(function,annotationname)
                print("Done 3")
                
                fig=set_plot(function)
                fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
                global_frame=1
        except:
            pass
        #print("Test End")        
        os.chdir("pcd_files")
        print(os.getcwd())

    
        
    if button == 'View Help':
            #window.Disappear()
            sg.Popup('Offline Help',' ','             ----To Create a Crop----',' ','1 .  Press ‘Z’ to enter orthogonal view along Z axis','2 .  Press ‘K’ to lock camera','3 .  Mouse left button + drag to create a selection rectangle','4 .  Press ‘C’ to save the crop','5 .  Choose the ‘app_data’ directory','6 .  Press ‘Q’ to exit the .pcd',' ','             ----General Editing Control----',' ','F - Enter freeview mode','X - Enter orthogonal view along X axis, press again to flip','Y - Enter orthogonal view along Y axis, press again to flip','Z - Enter orthogonal view along Z axis, press again to flip','K - Lock / unlock camera','Q/Esc	Exit window',' ','             ----General Mouse Control----',' ','Left button + drag  ->  Rotate','Ctrl + left button + drag  -> Translate','Wheel button + drag -> Translate','Shift + left button + drag -> Roll','Wheel -> Zoom in/out',' ', grab_anywhere=True)
            #window.Reappear()
            
    if button == 'About':
            #window.Disappear()
            sg.Popup('About this program','Version 2.0', 'You can annotate 3D to 2D .Not tomorrow, definitely not yesterday but today.', grab_anywhere=True)
            #window.Reappear()
    """
    if button is not sg.TIMEOUT_KEY:
        print("wow")
    """   
    if button is None or button == 'Exit' or button is 'End':
        window.Close()
        break

    try:
        if global_frame==0:
            #print("Refreshing")
            os.chdir("..")
            print(os.getcwd())
            try:
                function = value['func'][0]
                print(function)
                fig=set_plot(function)
                fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
            except:
                pass
            os.chdir("pcd_files")
            print(os.getcwd())
    except:
        pass
