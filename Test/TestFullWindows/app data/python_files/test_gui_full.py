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
import io
import base64

orange64 = 'iVBORw0KGgoAAAANSUhEUgAAAiIAAADLCAMAAABkvgh7AAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAMAUExURQAAANtvJ99sId5tIt5uI91tJNxuJNxuJttvKN90NN91Ntt3PN52ONx3Otx3PNt4Pdp4Ptx4PepfD+pfEOtgD+piD+tkD+ttD+dnFOdoE+doFOVoFuNqG+JrHOFrHuFsHuRpGORpGuRqGORqGupgEOpiEOpkEOlmEOhnEupoEOpoEupqFettEetsF+tuFOxqFetrGOtsGetvHOxrGOxsGOxtGuxuG+xuHexxFutwH+xxGOxyGOxyGuxxHuBsIOJvJ+NvKORvKONwKeNwKuJxLONyLeJyLuRwKeRwKuRxLOtxIexyIexzJOx0JOx1Ju11KOx2KOx2Kux5Iux4Kux5Le1/LeFyMOFzMuB0NOB1Nux7MOx8MOx8Mu19NO1+NO1+Ntd7RdV8RtN+S9J/TdF/TtV9SNR9Stl5QNl6Qdh6Qth7RK+Tfa+Tfq6Ufr+JZb+JZr+KZ7uMbr6KaL6LaryMbLyNb7yOb7WPdLuNcLqOcLmOcrmPdLOQd7SQdrKReLKRerGSerCTfLCTfrmQde2AN+2AOO2BOu2COu6DPO6EPe6EPsWDV8OFXcOFXsOGXcOGXsaDWMSEWsqCVs+AUM2AUs6CU82CVMqDWMmEWtCAT9CAUMKHYMCIYsCIZMCKZu6FQO6GQe6GQu6HRO6IRe6JRu6KR+6KSO+LSu+MS++MTO+OTe+OTu+OUO+RUu+TVfCNTvCOTvCPUPCQUfCQUvCSU/CRVPCSVPCSVvCUV/CUWPCVWvGWWvGXXPGYXvCWYPGaYfGcYvGcZPKdZvKeZ/GdavKeaPKebfKebvKgavKhbPKibfGibvKjcPGkcfKmdPKiePOod/OpePSpePSqevSrfPSsfPSsfvSqg/SugfWwgvWwhPWyhfWyhvWxi/Wyj/W0ifW2jfa4j/a1kPW2kva2lfW2lvW4kPa6kfa7kva5lvW7lPa8lPW8lve+l/a4mva5nPa6nPa7nva+mPa+mva/nPa8oPa9ovbAm/bAnfXAnvbCofbEo/XGp/bGqPbIqQAAAC/NnaUAAAEAdFJOU////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////wBT9wclAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAGHRFWHRTb2Z0d2FyZQBwYWludC5uZXQgNC4xLjFjKpxLAAAJXElEQVR4Xu3de3zVdR3H8Xb9/sJh60LlOTtubdIZEyckSdedMzkdZyRGIePmZdqki8s0KllJmtGCTAXRlUAyrireUeZga2JRkooYRWR0JbXMLsIqZ5fT7/L5nRvj9/md0/fhw/Px/fyHP+D33fb4vPj+LvsxXpMA8IREgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgIFEgJF7Ih1Xf3bVsuu/AYXu+mUrL+u8iqbqIcdErvhme0V8SjQCIpwWe+0nli+k2R5NTolc0jYzqpQBcigV+UDltZ57SQ6JfLqyRRXRyiCIis7u7qAhj8B3Ip1tLdg/pFLR0Z+hOR/JbyIrWxGIZCp289E2Ep+J3HzEFqLKy0qhUJUfeUkZnf8lGnYWX4l0tDfTOg5VEqoJNNTXh6EgmaMLBKuaymmcJFLRSfPO5CuRtgitYisPBehDQUFrqC3O2EtUxRdo4Bn8JHJhlNawlNZh85Aj2JQeiRp9JY08nY9Euk+nFUwq1ECLgww1ZTRaS+R8mnk6PpEF8dTDkNIgLQxiHFdNw7U0d9PU07CJdLw+tRUVpy5Cxo19+bz9lYI+n5cNfdhcjWGZf2jsCTTJcDiUmnBR/HKaewqbSHfqQqSJrkLGvuuctZu3jOgBD1u99B7Fg6a+Vwrrk8kNfRX+0XE2+qg527adsc38M723d01yK3lbqhH1SZp7CpfIolnJw4udQk44ddPOn/3q6b+M6K8+/c2vF+jXVw29X/ALI7N+Z3jome+f/QZ7pOG6VCMtl9Dkk7hElifvd0uPs1cb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'


#global fig
#os.chdir("..")
os.chdir("..")
print(os.getcwd())
def image_file_to_bytes(image64, size):
    image_file = io.BytesIO(base64.b64decode(image64))
    img = Image.open(image_file)
    img.thumbnail(size, Image.ANTIALIAS)
    bio = io.BytesIO()
    img.save(bio, format='PNG')
    imgbytes = bio.getvalue()
    return imgbytes

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

def set_plot(amp, function):
    im = np.array(Image.open('image_files/'+function+'.jpg'), dtype=np.uint8)

    # Create figure and axes
    fig,ax = plt.subplots(1)

    # Display the image
    ax.imshow(im)
    global figure_w, figure_h
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
function="frame0001"
fig=set_plot(amp, function)
#------------------------------------------------------------------------------------------
bcolor = ('#F0F8FF', '#F0F8FF')
wcolor = ('#F0F8FF', '#F0F8FF')
#sg.ChangeLookAndFeel('GreenTan')
sg.ChangeLookAndFeel('#F0F8FF')
#sg.ChangeLookAndFeel('SandyBeach')
sg.SetOptions (font =('Calibri',12,'bold')) 
#os.chdir("pcd_files")
i_vid = r'pcd_files/1547842929.701970000.pcd'
menu_def = [['&File', ['&Open', '&Save', '&Properties', 'E&xit' ]],
                ['&Edit', ['&Paste', ['Special', 'Normal',], 'Undo'],],
                ['&Toolbar', ['---', 'Command &1', 'Command &2', '---', 'Command &3', 'Command &4']],
                ['&Help', ['&View Help', '&About']],]

column1 = [[sg.Text('Camera Display', font = ('Calibri', 18, 'bold'), pad=(250, 15))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(6, 2))]]
dirname="Executable Requirements/Logo/pencil-icon.png"
pathname = os.path.join(dirname ,'3Draw2Day.png') 
column2=[
    [sg.Image(dirname,size=(60,60), background_color='#F0F8FF'),sg.Text('       3Draw2Day       ', background_color='#F0F8FF', font = ('Calibri', 16, 'bold'))],
    [sg.Text('Choose A Crop To view', size=(35, 1))],        
    [sg.Listbox(values=('crop_file1', 'crop_file2', 'crop_file3'), size=(30, 3))],     
    [sg.Spin(values=('No Comment', 'Comment'), initial_value='Select')],
    [sg.Multiline(default_text='Enter Comments Here', size=(35, 3), key = '_comment_'),sg.Submit()],
    [sg.InputCombo(['car', 'bike', 'truck','person'], size = (8, 4), key = '_annoname_')],      
    [sg.ReadButton('Meh')],
    [sg.Text('_'  * 80)],
    [sg.Text('File'), sg.In(i_vid,size=(30,1), key='input'),sg.FileBrowse('_filebrowse_')],
    #[sg.Button('Exit', image_data=image_file_to_bytes(orange64, (100,50)), font='Any 15', pad=(0,0), key='Proceed'),],
    [sg.ReadButton('Proceed')],
    [sg.Text('_'  * 80)]
    ]

column3 = [
           [sg.Spin([sz for sz in range (1,5)], initial_value =1, size = (2,1), key = '_spin_'),
            sg.Text('Amplitude', size = (10, 1), font = ('Calibri', 12, 'bold'))],
           [sg.InputCombo(['frame0001', 'frame0008'], size = (8, 4), key = '_function_'),
            sg.Text('Function', size = (10, 1),font = ('Calibri', 12, 'bold'))],
           [sg.ReadButton('Redraw Plot')],
           [sg.Text('_'  * 80)]
           ]

column4=[[sg.Column(column2, background_color='#F0F8FF')],
         [sg.Column(column3, background_color='#F0F8FF')]]
#add  file name for image
   
layout = [
    
    [sg.Menu(menu_def, tearoff=False, pad=(20,1))],
    #[sg.Text('3D Annotation Tool', size=(30, 1), font=("Helvetica", 25)),sg.Column(column1, background_color='#d3dfda')],      
    [sg.Column(column4, background_color='#F0F8FF',),sg.Column(column1, background_color='#d3dfda')],
    #[sg.InputCombo(('PCD to Image', 'Image to PCD'), size=(20, 3))],     
    [sg.Text('Choose A PCD to Annotate', size=(35, 1))],#sg.Text('Help  \n 1. Z - Lock in z-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n X - Lock in x-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n Q - Quit')],                  
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
     sg.InputText('Default Folder'), sg.FolderBrowse()],      
    [sg.Submit(), sg.Cancel()],
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

while True:
    
    button, value = window.Read()
    if button == 'Redraw Plot':
        currentloc=os.getcwd()
        os.chdir("..")
        amp = int(value['_spin_'])
        function = value['_function_']
        fig=set_plot(amp,function)
        fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
        os.chdir(currentloc)

    #if button == '_filebrowse_':
        #os.chdir("pcd_files")
        #print("filebrowse pressed")

    if button == 'Proceed':
        os.chdir("..")
        print(os.getcwd())
        directoryname = value['input']
        filename=ntpath.basename(directoryname)
        filename=filename.replace('.pcd', '')
        print(filename)
        amp = int(value['_spin_'])
        function = value['_function_']
        pcd = op3.read_point_cloud(directoryname)
        print("Open file "+filename)
        #op3.draw_geometries_with_editing([pcd])
        destinationf="working_data/viewpoint/viewpoint.json"
        load_view_point(pcd,destinationf)
        print("Done cutting")
        annotationname = value['_annoname_'].strip()
	
        cpd.main(filename)
        print("Done 1")
        jsr.main(filename)
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
