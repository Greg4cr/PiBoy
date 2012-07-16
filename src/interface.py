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
	canvas = Canvas(master,width=w, height=h, bd=0, highlightthickness=0)
	canvas.pack(expand='yes',fill='both')

	#Set wallpaper
	self.wall = ImageTk.PhotoImage(file="../includes/wallpaper/wall1.jpg")
	self.background = canvas.create_image(0,0,image=self.wall,anchor=NW)
	
	#Display Raspberry Pi logo
	self.logo = ImageTk.PhotoImage(file="../includes/rpilogo.png")
	self.logoDispArea = canvas.create_image(w/2.5,0,image=self.logo,anchor=NW)
	
	#Buttons
	self.nes = ImageTk.PhotoImage(file="../includes/nes.png")
	self.nesDispArea = canvas.create_image(w/2.65,h/2.8,image=self.nes,anchor=NW)
	canvas.tag_bind(self.nesDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.snes = ImageTk.PhotoImage(file="../includes/snes.png")
	self.snesDispArea = canvas.create_image(((w/2.65)+150),h/2.8,image=self.snes,anchor=NW)
	canvas.tag_bind(self.snesDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.gb = ImageTk.PhotoImage(file="../includes/gb.png")
	self.gbDispArea = canvas.create_image(w/2.65,((h/2.8)+150),image=self.gb,anchor=NW)
	canvas.tag_bind(self.gbDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.gba = ImageTk.PhotoImage(file="../includes/gba.png")
	self.gbaDispArea = canvas.create_image(((w/2.65)+150),((h/2.8)+150),image=self.gba,anchor=NW)
	canvas.tag_bind(self.gbaDispArea,"<Button-1>",lambda x: self.launchGEdit())

    # Application launchers
    # Launches an application and closes the main GUI
    def launchGEdit(self):
	system("gedit &")
	exit()	

root = Tk()
app = MainInterface(root)

root.mainloop()
