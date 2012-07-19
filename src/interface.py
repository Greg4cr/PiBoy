# Gregory Gay
# PiBoy project
# File: interface.py

from Tkinter import *
import Image            
import ImageTk         
import sys
import getopt
from os import system
import subprocess as sub

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

	self.createInterface(canvas,w,h)

    #Draw interface
    def createInterface(self,canvas,w,h):
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
	self.settingsBg = canvas.create_rectangle(x0,y0,x1,y1,fill="white")
	self.objects.append(self.settingsBg)	

	#back arrow
	self.back = ImageTk.PhotoImage(file="../includes/back.png")
	self.objects.append(self.back)	
	self.backArrow = canvas.create_image(x1-60,y1-60,image=self.back,anchor=NW)
	self.objects.append(self.backArrow)	

	canvas.tag_bind(self.backArrow,"<Button-1>",lambda x: self.destroySettings(canvas,self.objects))

	#Copyright text and header
	self.objects.append(canvas.create_text(x0+5,y0+5,anchor=NW,font=("helvetica",16,"bold"),text="Settings"))
	self.objects.append(canvas.create_text(x0+5,y1-10,anchor=SW,font=("helvetica",8),text="PiBoy Version 0.1 (Pong)\nDesigned by Gregory Gay (greg@greggay.com)\nPlease do not use this software to play games that you don't own!"))

	#Options
	self.chooseBrightness = canvas.create_text(w/2.4,y0+50,anchor=NW,font=("helvetica",14,"bold"),text="Brightness",activefill="red")	
	self.objects.append(self.chooseBrightness)	
	canvas.tag_bind(self.chooseBrightness,"<Button-1>",lambda x: self.brightnessMenu(canvas,w,h,self.objects))
	

	self.chooseWallpaper = canvas.create_text(w/2.4,y0+75,anchor=NW,font=("helvetica",14,"bold"),text="Wallpaper",activefill="red")
	self.objects.append(self.chooseWallpaper)	
	canvas.tag_bind(self.chooseWallpaper,"<Button-1>",lambda x: self.wallpaperMenu(canvas,w,h,self.objects))

    def destroySettings(self,canvas,objects):
	for item in objects:
	    canvas.delete(item)

    def destroyAndReturn(self,canvas,objects,w,h):
	for item in objects:
	    canvas.delete(item)

	self.settingsMenu(canvas,w,h)

    def brightnessMenu(self,canvas,w,h,oldObjects):
	#erase settings menu
	self.destroySettings(canvas,oldObjects)
	
	x0=w/3
	x1=(w/3)+(w/3.4)
	y0=h/2.5
	y1=(h/2.5)+70

	self.objects = []
	#background
	self.settingsBg = canvas.create_rectangle(x0,y0,x1,y1,fill="white")
	self.objects.append(self.settingsBg)	

	#back arrow
	self.back = ImageTk.PhotoImage(file="../includes/back.png")
	self.objects.append(self.back)	
	self.backArrow = canvas.create_image(x1-60,y1-60,image=self.back,anchor=NW)
	self.objects.append(self.backArrow)	

	canvas.tag_bind(self.backArrow,"<Button-1>",lambda x: self.destroyAndReturn(canvas,self.objects,w,h))

    def wallpaperMenu(self,canvas,w,h,oldObjects):
	#erase settings menu
	self.destroySettings(canvas,oldObjects)

	#get number of images in the wallpaper directory
	call = sub.Popen('ls ../includes/wallpaper/ | wc -w', stderr=sub.STDOUT, stdout=sub.PIPE, shell=True)
	howManyWalls,error = call.communicate()
	howManyWalls=int(howManyWalls)-1

	x0=w/3.5
	x1=(w/3.5)+(w/2.5)
	y0=(h/2.5)-(100*int(howManyWalls/3))

	if y0<0:
		y0 = 0

	y1=y0+275+(100*int(howManyWalls/3))

	if y1 > h:
		y1 = h

	self.objects = []
	#background
	self.settingsBg = canvas.create_rectangle(x0,y0,x1,y1,fill="white")
	self.objects.append(self.settingsBg)	

	#back arrow
	self.back = ImageTk.PhotoImage(file="../includes/back.png")
	self.objects.append(self.back)	
	self.backArrow = canvas.create_image(x1-60,y1-60,image=self.back,anchor=NW)
	self.objects.append(self.backArrow)	

	canvas.tag_bind(self.backArrow,"<Button-1>",lambda x: self.destroyAndReturn(canvas,self.objects,w,h))

	#Current wallpaper
	self.objects.append(canvas.create_text(x0+10,y0+60,anchor=NW,font=("helvetica",14,"bold"),text="Current:"))
	self.currentWall= Image.open("../includes/wallpaper/default.jpg")
	self.objects.append(self.currentWall)
	self.currentWall.thumbnail((150,150),Image.ANTIALIAS)
	self.currentThumb = ImageTk.PhotoImage(self.currentWall)
	self.objects.append(self.currentThumb)
	self.currentThumbDisp =canvas.create_image((w/2.4),y0+25,anchor=NW,image=self.currentThumb)
	self.objects.append(self.currentThumbDisp)

	self.objects.append(canvas.create_text(x0+10,y0+170,anchor=NW,font=("helvetica",14,"bold"),text="Choose Wallpaper:"))
	
	#Display wallpaper options
	startX=x0+10
	startY=y0+45
	self.options=[]
	self.optionThumbs=[]
	self.optionThumbsDisp=[]

	for i in range(0,(howManyWalls-1)):
		#Update position
		if i % 3 == 0:
			startX=x0+10
			startY=startY+160
		else:
			startX=startX+160

		self.options.append(Image.open("../includes/wallpaper/wall"+str(i+1)+".jpg"))
		self.objects.append(self.options[i])
		self.options[i].thumbnail((150,150),Image.ANTIALIAS)
		self.optionThumbs.append(ImageTk.PhotoImage(self.options[i]))
		self.objects.append(self.optionThumbs[i])
		self.optionThumbsDisp.append(canvas.create_image(startX,startY,anchor=NW,image=self.optionThumbs[i]))
		self.objects.append(self.optionThumbsDisp[i])

		canvas.tag_bind(self.optionThumbsDisp[i],"<Button-1>",lambda x,choice=i: self.changeWallpaper(canvas,w,h,choice))


    def changeWallpaper(self,canvas,w,h,choice):
	system("mv ../includes/wallpaper/default.jpg temp")
	system("mv ../includes/wallpaper/wall"+str(choice+1)+".jpg ../includes/wallpaper/default.jpg")
	system("mv temp ../includes/wallpaper/wall"+str(choice+1)+".jpg")
	canvas.delete(ALL)
	self.createInterface(canvas,w,h)

    #Shut system down
    def shutdown(self):
	exit()

root = Tk()
app = MainInterface(root)
root.mainloop()
