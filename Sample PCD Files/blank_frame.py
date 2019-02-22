from tkinter import * # or(from Tkinter import Tk) on Python 2.x

def exit(event):
    root.quit()

root = Tk()

root.wait_visibility(root)
root.wm_attributes('-alpha',0.3)
root.wm_attributes("-fullscreen", True)

root.bind("<Escape>", exit)
root.mainloop()
root.attributes("-topmost", True)
