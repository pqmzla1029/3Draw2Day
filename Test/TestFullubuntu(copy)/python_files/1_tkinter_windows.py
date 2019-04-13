from tkinter import Tk, Label, Button, StringVar,filedialog
#from tkinter import filedialog	
from open3d import *
import os
#os.chdir("..")
#print(os.getcwd())
class MyFirstGUI:
    LABEL_TEXT = [
        "Instructions \n\n 1. Press Z to lock the z-axis \n 2. Press K to lock for cropping \n 3. Draw your 2D bounding box using the mouse \n 4. Press C, then Enter, to save the crop \n 5. Press X to lock the x-axis \n 6. Press K to lock for cropping \n 7. Draw your 2D bounding box using the mouse \n 8. Press C, then Enter, to save the crop \n 9. Press Escape \n 10. Press 'Proceed' \n",
        # "Actually, this is our second GUI.",
        # "We made it more interesting...",
        # "...by making this label interactive.",
        # "Go on, click on it again.",
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

