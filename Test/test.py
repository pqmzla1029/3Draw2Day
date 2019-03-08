import tkinter as tk
from tkinter import filedialog	
root = tk.Tk()
filename = filedialog.askopenfilename(parent=root, initialdir="./pcd_files",
                                    title='Please select a directory')
