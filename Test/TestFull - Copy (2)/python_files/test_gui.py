import PySimpleGUI as sg
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os
os.chdir("..")

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
im = np.array(Image.open('image_files/frame0000.jpg'), dtype=np.uint8)

# Create figure and axes
fig,ax = plt.subplots(1)

# Display the image
ax.imshow(im)
#fig = plt.figure()
#ax = fig.add_subplot(111)
#x-values
#x = np.linspace(-np.pi*2, np.pi*2, 100)
#y-values
#y = np.sin(x)
a = np.loadtxt('working_data/bounding_data/image_matrix_bound.txt')
#print(a)
x_number_values= np.zeros(5)
y_number_values= np.zeros(5)
rv=4
for k in range(0,2):
    start_val=(k*rv)
    # List to hold x values.
    for i in range(start_val,(rv+start_val)+1):
        j=(i%4)+start_val
        x_number_values[i-start_val] = a[0,j]

    # List to hold y values.
    for i in range(start_val,(rv+start_val)+1):
        j=(i%4)+start_val
        y_number_values[i-start_val] = a[1,j]
    #print(x_number_values, y_number_values)
    # Create a Rectangle patch
    #rect = patches.Rectangle((463,930),(930-463),971,linewidth=1,edgecolor='r',facecolor='none')
    plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')

for i in range(0,4):
    x_number_values = [a[0,i],a[0,i+4]]
    y_number_values = [a[1,i],a[1,i+4]]
    #print(x_number_values, y_number_values)
    plt.plot(x_number_values, y_number_values, linewidth=3, color='blue')

ax.set_title('sin(x)')
figure_x, figure_y, figure_w, figure_h = fig.bbox.bounds
#------------------------------------------------------------------------------------------

sg.ChangeLookAndFeel('GreenTan')


column1 = [[sg.Text('Plot Test - PySimpleGUI and Matplotlib', font = ('Calibri', 18, 'bold'))],
          [sg.Canvas(size = (figure_w, figure_h), key = '_canvas_')],
          [sg.OK(pad=((figure_w / 2, 0), 3), size=(6, 2))]]
   
layout = [      
    [sg.Text('3D Annotation Tool', size=(30, 1), font=("Helvetica", 25))],      
    [sg.Text('Choose A Crop To view', size=(35, 1))],        
    [sg.Listbox(values=('crop_file1', 'crop_file2', 'crop_file3'), size=(30, 3))],     
    [sg.Spin(values=('No Comment', 'Comment'), initial_value='Select')],
    [sg.Multiline(default_text='Enter Comments Here', size=(35, 3)),sg.Submit()],      
    [sg.Text('_'  * 80)],
    [sg.InputCombo(('PCD to Image', 'Image to PCD'), size=(20, 3))],     
    [sg.Text('Choose A PCD to Annotate', size=(35, 1)),sg.Text('Help  \n 1. Z - Lock in z-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n X - Lock in x-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n Q - Quit')],                  
    [sg.Text('Your Folder', size=(15, 1), auto_size_text=False, justification='right'),      
     sg.InputText('Default Folder'), sg.FolderBrowse()],      
    [sg.Submit(), sg.Cancel()]      
]

window = sg.Window('Mobile Robotics', default_element_size=(40, 1)).Layout(layout)
#fig_photo = draw_figure(window.FindElement('_canvas_').TKCanvas, fig)
button, values = window.Read()
sg.Popup(button, values)
