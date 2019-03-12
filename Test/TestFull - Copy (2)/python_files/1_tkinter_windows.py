from tkinter import Tk, Label, Button, StringVar,filedialog
#from tkinter import filedialog	
from open3d import *
import os
#os.chdir("..")
#print(os.getcwd())
class MyFirstGUI:
    LABEL_TEXT = [
        "Main Screen \n Help \n 1. Z - Lock in z-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n X - Lock in x-axis \n 2. K - Lock for cropping \n 3. Draw Bounding Box \n 4. C - Save(Enter) \n Q - Quit",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("3D Annotation Tool")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Open", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Proceed", command=master.quit)
        self.close_button.pack()

    def greet(self):
        filename = filedialog.askopenfilename(parent=root, initialdir="./pcd_files",title='Please select a directory')
        pcd = read_point_cloud(filename)
        print("Open file "+filename)
        draw_geometries_with_editing([pcd])

    def cycle_label_text(self, event):
        self.label_index += 1
        self.label_index %= len(self.LABEL_TEXT) # wrap around
        self.label_text.set(self.LABEL_TEXT[self.label_index])

root = Tk()
root.geometry("500x500")
my_gui = MyFirstGUI(root)
root.mainloop()

