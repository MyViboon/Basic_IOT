from ctypes import pointer
from email.mime import image
from tkinter import *
from tkinter.font import BOLD
from PIL import Image, ImageTk
from threading import Thread
import time
import tkinter as tk

GUI = Tk()
GUI.geometry("900x600")
GUI.title("Dashboard ระบบควบคุม IoT ควบคุม Smart farm")
GUI.state("zoomed")

#กระดานวาดภาพ
canvas = Canvas(GUI, width=1300, height=900)
canvas.place(x=0, y=0) 

#ใส่ Background
background = ImageTk.PhotoImage(Image.open('farm.png'))
canvas.create_image(200,30,anchor=NW, image=background)

################### DOOR ###############################
#วาดสี่เหลี่ยม
canvas.create_polygon([532,257,576,283,576,327,532,300],fill='#10f00c', outline=None,tags='d1')
#ใส่ข้อความ
canvas.create_text(200,200, text="ประตูฟาร์มกำลังเปิด", fill='green', font=('Angsana New',30,'bold'),tags='d1')
#ใส่ Line
canvas.create_line(313,214,550,292,fill='gray', width=3,tags='d1')


door_stage = True
def DoorOnOff(event):
    global door_stage
    door_stage = not door_stage
    canvas.delete('d1')
    if door_stage == True:
        canvas.create_polygon([532,257,576,283,576,327,532,300],fill='#10f00c', outline=None,tags='d1')
        canvas.create_text(200,200, text="ประตูฟาร์มกำลังเปิด", fill='green', font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(313,214,550,292,fill='gray', width=3,tags='d1')
    else:
        canvas.create_polygon([532,257,576,283,576,327,532,300],fill='red', outline=None,tags='d1')
        canvas.create_text(200,200, text="ประตูฟาร์มกำลังปิด", fill='red', font=('Angsana New',30,'bold'),tags='d1')
        canvas.create_line(313,214,550,292,fill='gray', width=3,tags='d1')

#################### FAN ######################

fan = ImageTk.PhotoImage(Image.open('fan.png')) 
canvas.create_image(969,293,image=fan,tags='img3')

angle = 0

def run_fan(event=None):
	# fan = ImageTk.PhotoImage(resize_image('fan-icon.png',100))
	global angle
	while True:	
		if angle != 0:
			canvas.delete('img3')
			fan = ImageTk.PhotoImage(image = Image.open('fan.png').rotate(angle)) 
			canvas.create_image(969,293,image=fan,tags='img3')
		angle += 20
		if angle >= 360:
			angle = 0
		time.sleep(0.1)

task = Thread(target=run_fan)
task.start()

GUI.bind('<Return>',DoorOnOff)
GUI.mainloop()