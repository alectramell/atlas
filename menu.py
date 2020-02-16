import os
import sys
import time
from tkinter import *

def upDate(xvar):

	time.sleep(xvar)
	Tk.update(root)

def runHOST(self):

	import os
	os.system('START /B chlink')
	XCOM = str('START /B http://localhost:8888')
	YCOM = str('START /B php -S localhost:8888 -t "C:/Users/%USERNAME%/Desktop/atlas/www"')
	os.system(XCOM)
	os.system(YCOM)

def exitAPP(self):

	import os
	import sys
	import time
	time.sleep(0.5)
	sys.exit()

APPNAME = str('ATLAS')
APPVERS = str('v.10')
XTITLE = str(APPNAME+' '+APPVERS)

root = Tk()
root.geometry("400x500")
root.config(background='#000000')
root.title(XTITLE)
root.iconbitmap(r'media/app.ico')
exitPhoto = PhotoImage(file='media/exit.png')
exitOPT = Button(root, relief='flat', bg='#000000', borderwidth=10, image=exitPhoto)
exitOPT.pack(anchor='ne')
exitOPT.bind('<Button-1>', exitAPP)
startPhoto = PhotoImage(file='media/bg.png')
startOPT = Button(root, relief='sunken', bg='#000000', borderwidth=0, image=startPhoto)
startOPT.pack(side='top')
startOPT.bind('<Button-1>', runHOST)
upDate(0.5)
root.mainloop()

