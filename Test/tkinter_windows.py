from tkinter import Tk, Label, Button, StringVar,filedialog
#from tkinter import filedialog	
from open3d import *

class MyFirstGUI:
    LABEL_TEXT = [
        "Main Screen \n 1. Help \n 2. Welp \n 3. Self",
        "Actually, this is our second GUI.",
        "We made it more interesting...",
        "...by making this label interactive.",
        "Go on, click on it again.",
    ]
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label_index = 0
        self.label_text = StringVar()
        self.label_text.set(self.LABEL_TEXT[self.label_index])
        self.label = Label(master, textvariable=self.label_text)
        self.label.bind("<Button-1>", self.cycle_label_text)
        self.label.pack()

        self.greet_button = Button(master, text="Open", command=self.greet)
        self.greet_button.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
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

