# Gregory Gay
# PiBoy project
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
	self.wall = ImageTk.PhotoImage(file="../includes/wallpaper/default.jpg")
	self.background = canvas.create_image(0,0,image=self.wall,anchor=NW)
	
	#Display Raspberry Pi logo
	self.logo = ImageTk.PhotoImage(file="../includes/rpilogo.png")
	self.logoDispArea = canvas.create_image(w/2.5,0,image=self.logo,anchor=NW)
	
	#Buttons
	self.nes = ImageTk.PhotoImage(file="../includes/nes.png")
	self.nesDispArea = canvas.create_image(w/2.85,h/3,image=self.nes,anchor=NW)
	canvas.tag_bind(self.nesDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.snes = ImageTk.PhotoImage(file="../includes/snes.png")
	self.snesDispArea = canvas.create_image(((w/2.85)+225),h/3,image=self.snes,anchor=NW)
	canvas.tag_bind(self.snesDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.settings = ImageTk.PhotoImage(file="../includes/settings.png")
	self.settingsDispArea = canvas.create_image(((w/2.85)+112),((h/3)+100),image=self.settings,anchor=NW)
	canvas.tag_bind(self.settingsDispArea,"<Button-1>",lambda x: self.settingsMenu(canvas,w,h))

	self.gb = ImageTk.PhotoImage(file="../includes/gb.png")
	self.gbDispArea = canvas.create_image(w/2.85,((h/3)+200),image=self.gb,anchor=NW)
	canvas.tag_bind(self.gbDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.gba = ImageTk.PhotoImage(file="../includes/gba.png")
	self.gbaDispArea = canvas.create_image(((w/2.85)+225),((h/3)+200),image=self.gba,anchor=NW)
	canvas.tag_bind(self.gbaDispArea,"<Button-1>",lambda x: self.launchGEdit())

	self.powerOff = ImageTk.PhotoImage(file="../includes/power.png")
	self.powerDispArea = canvas.create_image(w-60,h-60,image=self.powerOff,anchor=NW)
	canvas.tag_bind(self.powerDispArea,"<Button-1>",lambda x: self.shutdown())

    # Application launchers
    # Launches an application and closes the main GUI
    def launchGEdit(self):
	system("gedit &")
	exit()	

    #Settings menu
    def settingsMenu(self,canvas,w,h):
	x0=w/3.5
	x1=(w/3.5)+(w/2.5)
	y0=h/3
	y1=(h/3)+(h/2.5)

	self.objects = []
	#background
	self.objects.append(canvas.create_rectangle(x0,y0,x1,y1,fill="white"))
	
	#back arrow
	self.objects.append(ImageTk.PhotoImage(file="../includes/back.png"))
	self.objects.append(canvas.create_image(x1-60,y1-60,image=self.objects[1],anchor=NW))
	canvas.tag_bind(self.objects[2],"<Button-1>",lambda x: self.destroySettings(canvas,self.objects))

	#Copyright text and header
	self.objects.append(canvas.create_text(x0+5,y0+5,anchor=NW,font=("helvetica",16,"bold"),text="Settings"))
	self.objects.append(canvas.create_text(x0+5,y1-10,anchor=SW,font=("helvetica",8),text="PiBoy Version 0.1 (Pong)\nDesigned by Gregory Gay (greg@greggay.com)\nPlease do not use this software to play games that you don't own!"))

	#Options
	self.objects.append(canvas.create_text(w/2.4,y0+50,anchor=NW,font=("helvetica",14,"bold"),text="Change Wallpaper",activefill="red"))
		 
    def destroySettings(self,canvas,objects):
	for item in objects:
	    canvas.delete(item)

    #Shut system down
    def shutdown(self):
	exit()

root = Tk()
app = MainInterface(root)
root.mainloop()
