import os, sys
import tkinter
import image# ImageTk
import time

root = tkinter.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))
root.focus_set()
root.bind("<Escape>", lambda e: e.widget.quit())
image = Image.open(image_path+f)
tkpi = ImageTk.PhotoImage(image)        
label_image = Tkinter.Label(root, image=tkpi)
label_image.place(x=0,y=0,width=w,height=h)
root.mainloop(0)