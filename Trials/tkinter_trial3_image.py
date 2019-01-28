from tkinter import *
from PIL import ImageTk

canvas = Canvas(width = 200, height = 200, bg = 'blue')
canvas.pack(expand = YES, fill = BOTH)

image = ImageTk.PhotoImage(file ="car.jpg")
canvas.create_image(10, 10, image = image, anchor = NW)

mainloop()
