#Button2.py  
from tkinter import *  
def click():  
 print("click button!")  
w = Tk() # Create the w(base) window where all widgets go  
w = Label(w, text="Hello,vvhsgvhgwvedhgvehgv world!") # Create a label with words  
self.Label.configure(text="w")
w.pack() # Put the label into the window  
Button1 = Button(w, text="Exit",command=click)  
Button1.pack()  
w.mainloop() # Start th