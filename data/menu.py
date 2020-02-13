import os
import sys
import time
from tkinter import *

def upDate(xvar):

	time.sleep(xvar)
	Tk.update(root)

root = Tk()
root.geometry("800x500")
root.title('ATLAS v1.0')
root.iconbitmap(r'app.ico')
upDate(0.5)
root.mainloop()