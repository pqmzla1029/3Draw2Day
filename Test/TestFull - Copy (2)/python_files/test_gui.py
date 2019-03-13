import PySimpleGUI as sg

sg.ChangeLookAndFeel('GreenTan')

column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10, 1))],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],      
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]      
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
button, values = window.Read()
sg.Popup(button, values)
