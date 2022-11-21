from tkinter import *
import os
def parkin():
    os.startfile(r'Parking inside.py')
    w.destroy()
    pass
def parkout():
    os.startfile(r'Unpark.py')
    w.destroy()
    pass
w=Tk()
b1=Button(w,text="Park In",command=lambda:parkin())
b2=Button(w,text="Park Out",command=lambda:parkout())
b1.pack()
b2.pack()
w.mainloop()
