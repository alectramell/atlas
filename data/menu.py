import os
import sys
import time
from tkinter import *

def upDate(xvar):

	time.sleep(xvar)
	Tk.update(root)

def facebookURL():

	import os
	XCOM = str('START https://www.facebook.com')
	os.system(XCOM)

def runHOST(self):

	import os
	XCOM = str('START /B http://localhost:8888')
	YCOM = str('START /B php -S localhost:8888 -t "C:/Users/%USERNAME%/Desktop/site/www"')
	os.system(XCOM)
	os.system(YCOM)

def exitAPP(self):

	import os
	import sys
	import time
	time.sleep(0.5)
	sys.exit()

root = Tk()
root.geometry("800x500")
root.config(background='#000000')
root.title('ATLAS v1.0')
root.iconbitmap(r'app.ico')
exitOPT = Button(root, relief='sunken', bg='#000000', fg='#ffffff', padx=25, pady=15, text='Exit', font='pixel 24 normal', borderwidth=0)
exitOPT.pack(anchor='ne')
exitOPT.bind('<Button-1>', exitAPP)
# facebookOPT = Button(root, relief='flat', bg='#000000', padx=25, pady=15, fg='#ffffff', text='facebook', font='Klavika-Bold 24 bold', borderwidth=0, command=facebookURL)
# facebookOPT.pack(anchor='nw')
atlasPhoto = PhotoImage(file='atlasSTART.png')
atlasOPT = Button(root, relief='sunken', bg='#000000', borderwidth=0, image=atlasPhoto)
atlasOPT.pack(side='top')
atlasOPT.bind('<Button-1>', runHOST)
upDate(0.5)
root.mainloop()
