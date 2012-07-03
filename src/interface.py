# File: interface.py

from Tkinter import *
import Image            
import ImageTk         
import sys
import getopt
from os import system

class MainInterface (object):

    def __init__(self,master):
	#Fullscreen
	w, h = master.winfo_screenwidth(), master.winfo_screenheight()
	master.overrideredirect(1)
	master.geometry("%dx%d+0+0" % (w, h))	
	master.focus_set() 
      
	#Create canvas
	canvas = Canvas(master,width=w, height=h)
	canvas.pack(expand='yes',fill='both')
 
	#Set wallpaper
	self.wall = ImageTk.PhotoImage(file="/home/whalen/code/piboy/includes/wallpaper/wall1.jpg")
	self.background = canvas.create_image(0,0,image=self.wall,anchor=NW)
	
	#Display Raspberry Pi logo
	self.logo = ImageTk.PhotoImage(file="/home/whalen/code/piboy/includes/rpilogo.png")
	self.logoDispArea = canvas.create_image(w/2.5,0,image=self.logo,anchor=NW)
	
	#Buttons
        self.quit = Button(canvas, text="QUIT", fg="red", command=canvas.quit)
        self.quit.pack(side='bottom')

        self.gedit = Button(canvas, text="gEdit", command=self.launchGEdit)
        self.gedit.pack(side='bottom')

    # Application launchers
    # Launches an application and closes the main GUI
    def launchGEdit(self):
	system("gedit &")
	exit()	

root = Tk()
app = MainInterface(root)

root.mainloop()
