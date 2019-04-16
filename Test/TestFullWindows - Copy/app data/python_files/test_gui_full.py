import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasAgg
import matplotlib.backends.tkagg as tkagg
import numpy as np
import tkinter as tk
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

#global fig
#os.chdir("..")
os.chdir("..")
print(os.getcwd())


def draw_figure(canvas, figure, loc = (0,0)):

    figure_canvas_agg = FigureCanvasAgg(figure) 
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = tk.PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w/2, loc[1] + figure_h/2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


#------------------------------------------------------------------------------------------

#fig = plt.figure()
#ax = fig.add_subplot(111)
#x-values
#x = np.linspace(-np.pi*2, np.pi*2, 100)
#y-values
#y = np.sin(x)
amp=5
df=pd.read_csv('working_data/links/PCD-ImageMatches.txt', sep=",", header=None)
array_images=df[1]
size_of_array=array_images.shape[0]
placeholder_array = ["" for x in range(size_of_array)]
print(array_images[0])
for i in range(size_of_array):
    placeholder_array[i]=array_images[i].replace('.jpg', '')

print(placeholder_array)
def set_plot(amp, function):
    print(os.getcwd())
    im = np.array(Image.open('image_files/'+function+'.jpg'), dtype=np.uint8)

    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)
    global figure_w, figure_h
    exists = os.path.isfile("working_data/bounding_data/"+function+".txt")
    if exists:
        a = np.loadtxt("working_data/bounding_data/"+function+".txt", skiprows=0, usecols = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16))
        #color_array=["blue","red","green","cyan","orange","pink"]
        size_of_array=a.shape[0]
        color_array = cm.rainbow(np.linspace(0, 1, size_of_array))

        #for i in range(10):
        #	color_array.append('%06X' % randint(0, 0xFFFFFF))
        len_a=a.shape
        #print(len_a[0])
        for index_item in range(0,len_a[0]):
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

amp = 1
function=placeholder_array[0]
fig=set_plot(amp, function)
#------------------------------------------------------------------------------------------
bcolor = ('#F0F8FF', '#F0F8FF')
wcolor = ('#F0F8FF', '#F0F8FF')
#sg.ChangeLookAndFeel('GreenTan')
sg.ChangeLookAndFeel('#F0F8FF')
#sg.ChangeLookAndFeel('SandyBeach')
#sg.SetOptions (font =('Calibri',12,'bold')) 
#os.chdir("pcd_files")
i_vid = r'pcd_files/1547842929.701970000.pcd'
menu_def = [['&File', ['&Open', '&Save', '&Properties', 'E&xit' ]],
                ['&Edit', ['&Paste', ['Special', 'Normal',], 'Undo'],],
                ['&Toolbar', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&View Help', '&About']],]

column1 = [[sg.Text('Camera Display', font = ('Calibri', 18, 'bold'), background_color='#F0F8FF', pad=(250, 15))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],#,
          [sg.InputCombo(placeholder_array, size = (10, 4), key = '_function_', background_color='#F0F8FF', pad=(250, 15))],
            #sg.Text('Function', size = (10, 1),font = ('Calibri', 12, 'bold'))],
           [sg.ReadButton('Redraw Plot')],
           [sg.Text('_'  * 40,background_color='#F0F8FF')]
           ]
          
dirname="Executable Requirements/Logo/pencil-icon.png"
#pathname = os.path.join(dirname ,'3Draw2Day.png') 
column2=[
    [sg.Image(dirname,size=(60,60), background_color='#F0F8FF'),sg.Text('       3Draw2Day       ', background_color='#F0F8FF', font = ('Calibri', 18, 'bold'))],
    [sg.Text('_'  * 40, background_color='#F0F8FF')],
    #[sg.Text('_'  * 40, background_color='#F0F8FF')],
    [sg.Text('Select type of object to annotate :', background_color='#F0F8FF', font = ('Calibri', 14, 'bold'))],        
    #[sg.Listbox(values=('crop_file1', 'crop_file2', 'crop_file3'), size=(30, 3))],     
    #[sg.Spin(values=('No Comment', 'Comment'), initial_value='Select')],
    #[sg.Multiline(default_text='Enter Comments Here', size=(35, 3), key = '_comment_'),sg.Submit()],
    [sg.InputCombo(['car', 'bike', 'truck','person'], size = (8, 4), key = '_annoname_')],      
    #[sg.ReadButton('Meh')],
    #[sg.Text('_'  * 40)],
    #[sg.Text('File'), sg.In(i_vid,size=(30,1), key='input')],#sg.ReadButton('_filebrowse_')],
    #[sg.Button('Exit', image_data=image_file_to_bytes(orange64, (100,50)), font='Any 15', pad=(0,0), key='Open PCD'),],
    [sg.ReadButton('Open PCD')],
    [sg.Text('_'  * 40, background_color='#F0F8FF')]
    ]

column3 = [
           #[sg.Spin([sz for sz in range (1,5)], initial_value =1, size = (2,1), key = '_spin_'),
            #sg.Text('Amplitude', size = (10, 1), font = ('Calibri', 12, 'bold'))],
           [sg.InputCombo(placeholder_array, size = (10, 4), key = '_function_', background_color='#F0F8FF', pad=(250, 15))],
            #sg.Text('Function', size = (10, 1),font = ('Calibri', 12, 'bold'))],
           [sg.ReadButton('Redraw Plot')],
           [sg.Text('_'  * 40,background_color='#F0F8FF')]
           ]

#column4=[[sg.Column(column2, background_color='#F0F8FF')],
#         [sg.Column(column3, background_color='#F0F8FF')]]
column4=[[sg.Column(column1, background_color='#F0F8FF')],
         [sg.Column(column3, background_color='#F0F8FF')]]
#add  file name for image
  
layout = [
    
    [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
    #[sg.Text('3D Annotation Tool', size=(30, 1), font=("Helvetica", 25)),sg.Column(column1, background_color='#d3dfda')],      
    [sg.Column(column2, background_color='#F0F8FF',),sg.Column(column1, background_color='#F0F8FF')],
    #[sg.InputCombo(('PCD to Image', 'Image to PCD'), size=(20, 3))],     
    #[sg.Text('Choose A PCD to Annotate', size=(35, 1))],#sg.Text('Help  \n 1. Z - Lock in z-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n X - Lock in x-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n Q - Quit')],                  
    #[sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
     #sg.InputText('Default Folder'), sg.FolderBrowse()],      
    #[sg.Submit(), sg.Cancel()],
    [sg.Text('Status Bar', relief=sg.RELIEF_SUNKEN, size=(55,1),  pad=(0,3),key='_status_')]
]
dirname="Executable Requirements/Logo/pencil-icon.ico"
#window = sg.Window('Mobile Robotics', default_element_size=(40, 1)).Layout(layout)
window = sg.Window('3Draw2Day', force_toplevel = True,icon=dirname).Layout(layout).Finalize()
fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
#button, values = window.Read()
#sg.Popup(button, values)

def load_view_point(pcd, filename):
    vis = op3.VisualizerWithEditing()
    vis.create_window()
    ctr = vis.get_view_control()
    param = op3.read_pinhole_camera_parameters(filename)
    vis.add_geometry(pcd)
    ctr.convert_from_pinhole_camera_parameters(param)
    vis.run()
    vis.destroy_window()


os.chdir("pcd_files")
print(os.getcwd())

while True:
    print("trial")
    amp=5
    button, value = window.Read()
    if button == 'Redraw Plot':
        print(os.getcwd())
        currentloc=os.getcwd()
        os.chdir("..")
        print(os.getcwd())
        #amp = int(value['_spin_'])
        
        #PCD-ImageMatches
        function = value['_function_']
        fig=set_plot(amp,function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
        #os.chdir(currentloc)
        os.chdir("pcd_files")

    if button == '_filebrowse_':
        root = tk.Tk()
        root.withdraw()
        filename = filedialog.askopenfilename(parent=root, initialdir="./pcd_files", title='Please select a directory')
        print(filename)

    if button == 'Open PCD':
        os.chdir("..")
        print(os.getcwd())
        root = tk.Tk()
        root.withdraw()
        directoryname = filedialog.askopenfilename(parent=root, initialdir="./pcd_files", title='Please select a directory')
        filename=ntpath.basename(directoryname)
        print(filename)
        
        #directoryname = value['input']
        
        #filename=filename.replace('.pcd', '')
        #print(filename)
        df1=df
        print(df[0][0])
        df1.set_index(0, inplace=True)
        df1=df.loc[filename, : ]
        function=df1[1]
        print(function)
        filename=filename.replace('.pcd', '')
        function=function.replace('.jpg', '')
        #amp = int(value['_spin_'])
        #function = value['_function_']
        pcd = op3.read_point_cloud(directoryname)
        print("Open file "+filename)
        #op3.draw_geometries_with_editing([pcd])
        destinationf="working_data/viewpoint/viewpoint.json"
        load_view_point(pcd,destinationf)
        print("Done cutting")
        annotationname = value['_annoname_'].strip()
	
        cpd.main(filename)
        print("Done 1")
        jsr.main(filename,annotationname)
        print("Done 2")
        ctif.main(function,annotationname)
        print("Done 3")
        
        set_plot(amp,function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
	
        os.chdir("pcd_files")
        
    if button == 'View Help':
            #window.Disappear()
            sg.Popup('Help  ',' 1. Z - Lock in z-axis ',' 2. K - Lock for cropping ',' 3. Draw Bounding Box ',' 4. C - Save(Enter) ',' X - Lock in x-axis ',' 2. K - Lock for cropping ',' 3. Draw Bounding Box ',' 4. C - Save(Enter) ',' Q - Quit', grab_anywhere=True)
            #window.Reappear()
            
    if button == 'About':
            #window.Disappear()
            sg.Popup('About this program','Version 1.0', 'PySimpleGUI rocks...', grab_anywhere=True)
            #window.Reappear()
    if button is None:   
        break
