#modules
from tkinter import *
import tkinter as tk
import subprocess
import customtkinter
from PIL import ImageTk, Image  
import psutil 
import webbrowser
import time
import sys




#settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


root = tk.Tk()
root.geometry("500x900")
root.config(background="#c0c0c0")
root.title("Acer predator sense for PHN16-71")

#battery limit

title= customtkinter.CTkLabel(root , text='Choose setting', text_color="#000000", font=('Helvetic',37 , "bold"))
title.pack(padx=20,pady=20)


def func():
     print ("Battery limit set to 80%")
     subprocess.run('sudo echo 1 | sudo tee /sys/bus/wmi/drivers/acer-wmi-battery/health_mode', shell=True)

def func0():
     print ("Battery limit disabled")
     subprocess.run('sudo echo 0 | sudo tee /sys/bus/wmi/drivers/acer-wmi-battery/health_mode', shell=True)




btn = tk.Button(root , text="Set charging limit to 80%" , command = func,
                                  font=("",20 ))
btn.pack(side="top")

btn = tk.Button(root , text="Disable charging limit" , command = func0,
                                  font=("",20 ))
btn.pack(side="top")



#logo
predatorlogo = ImageTk.PhotoImage(Image.open("predator.png"))
labell= Label(image=predatorlogo)
labell.place(x=10 , y=10)





#fan control
'''
fancoltrol= customtkinter.CTkLabel(root , text='Fan control', text_color="#000000", font=('Helvetic',37 , "bold"))
fancoltrol.pack()

scale = Scale(root,from_=10, to=0)
scale.pack()

#power modes
'''

'''PopOs
system76-power profile battery  
system76-power profile balanced  
system76-power profile performance

Ubuntu
powerprofilesctl set power-saver
powerprofilesctl set balanced
powerprofilesctl set performance

'''


powermodes= customtkinter.CTkLabel(root , text='Power modes', text_color="#000000", font=('Helvetic',37 , "bold"))
powermodes.pack()

powermodes = ["Power saver","Balanced","Performance"]

def powermodessel():
    if(powermodx.get()==0):
        subprocess.run('system76-power profile battery', shell=True)
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 60.00', shell=True)
    elif (powermodx.get() ==1):
        subprocess.run('system76-power profile balanced ', shell=True)
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 165.00 ', shell=True)
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 80%', shell=True)
    elif (powermodx.get() ==2):
        subprocess.run('system76-power profile performance', shell=True)
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 165.00 ', shell=True)
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 80%', shell=True)




powermodx=IntVar()


for ib in range(len(powermodes)):
    buttonss = Radiobutton(root ,variable=powermodx, text=powermodes[ib] , value=ib , font=("" , 20 ), command=powermodessel)


    buttonss.pack()

#xrandr --output eDP-1 --mode 1920x1200 --rate 165.00

#screen brightness


screenbrigth= customtkinter.CTkLabel(root , text='Screen brightness '  , text_color="#000000", font=('Helvetic',34 , "bold"))
screenbrigth.pack()


def printselection(value):
    brightnesss = (int(s.get()))
    if brightnesss >= 0 and brightnesss <= 10:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 10%', shell=True)
    elif brightnesss >= 10 and brightnesss <= 20:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 20%', shell=True)    
    elif brightnesss >= 20 and brightnesss <= 30:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 30%', shell=True)
    elif brightnesss >= 30 and brightnesss <= 40:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 40%', shell=True)
    elif brightnesss >= 40 and brightnesss <= 50:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 50%', shell=True)
    elif brightnesss >= 50 and brightnesss <= 60:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 60%', shell=True)
    elif brightnesss >= 60 and brightnesss <= 70:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 70%', shell=True)
    elif brightnesss >= 70 and brightnesss <= 80:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 80%', shell=True)
    elif brightnesss >= 80 and brightnesss <= 90:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 90%', shell=True)
    elif brightnesss >= 90 and brightnesss <= 100:
        subprocess.run('sudo brightnessctl -d "nvidia_wmi_ec_backlight" set 100%', shell=True)
    
    



s = tk.Scale(root, 
from_=0, 
to=100, 
orient=tk.HORIZONTAL, 
length=400, showvalue=0,
tickinterval=10, 
resolution=0.03,
command = printselection ,
label='select brightness'
 )
 
s.pack()





brightnesslogo = PhotoImage(file='brightness.png')
brightlabel = Label(image=brightnesslogo)
brightlabel.place(x=4 , y=400)

#screen refresh rate

screen_refresh_rate= customtkinter.CTkLabel(root , text='Screen refresh rate '  , text_color="#000000", font=('Helvetic',34 , "bold"))
screen_refresh_rate.pack()


def func60hz():
     print ("screen refresh rate set to 60 hz")
     subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 60.00', shell=True)

def func165hz():
     print ("screen refresh rate set to 165 hz")
     subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 165.00', shell=True)



btnscreen60 = tk.Button(root , text="60 Hz" , command = func60hz,
                                  font=("",20 ))
btnscreen60.place(x=50 , y= 500)

btnscreen165 = tk.Button(root , text="165 Hz" , command = func165hz,
                                  font=("",20 ))
btnscreen165.place(x=314 , y = 500)





#battery


def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return "%d:%02d:%02d" % (hours, minutes, seconds) 
  

battery = psutil.sensors_battery() 
  

print("Battery percentage : ", battery.percent) 
print("Power plugged in : ", battery.power_plugged) 

battery_plugged = battery.power_plugged


print("Battery left : ", convertTime(battery.secsleft)) 



#set screen refresh rate if laptop is plug in or not
"""

def battery_plug_check():
    if battery_plugged==False:
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 60.00', shell=True)
    elif battery_plugged==True:
         subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 165.00', shell=True)

"""






###

battery_life = customtkinter.CTkLabel(root , text='Battery information '  , text_color="#000000", font=('Helvetic',34 , "bold"))
battery_life.place(x=60,y=550)


#battery sensor
battery1 = int(battery.percent)
battery1 = str(battery1)
battery_sensor = customtkinter.CTkLabel(root , text= battery1 + "%" , text_color="#000000", font=('Helvetic',25 , "bold"))
battery_sensor.place(x=420,y=25)

#Update battery information


def updatebatteryinfo():
     
    subprocess.run('cd /home/yusifvatan/projects', shell=True)
    battteryyyy0 = subprocess.run('python3 project2.py', shell=True)
    
    
    
    
    

btnrefreshbattery = tk.Button(root , text="Refresh battery informations", command=updatebatteryinfo ,
                                  font=("",13 ))
btnrefreshbattery.place(x=100 , y=600)




#battery informations

'''logo'''
battery_logo = ImageTk.PhotoImage(Image.open("battery_percente0.png"))
labell_battery= Label(image=battery_logo)

#battery percente at below

labell_battery.place(x=13 , y=645)

battery_sensor = customtkinter.CTkLabel(root , text= battery1 + "%" , text_color="#000000", font=('Helvetic',25 , "bold"))
battery_sensor.place(x=60,y=651)

#check laptop is plug in or not

if battery_plugged==True:
    battery_plugged_check="Laptop is plug in"
else:
    battery_plugged_check="Laptop is not plug in"
    
battery_sensor = customtkinter.CTkLabel(root , text= battery_plugged_check, text_color="#000000", font=('Helvetic',22 , "bold"))
battery_sensor.place(x=15,y=690)

#check how long will laptop battery last

battery_left_time=convertTime(battery.secsleft)

battery_left_time_indicator = customtkinter.CTkLabel(root , text=battery_left_time + " hours left", text_color="#000000", font=('Helvetic',22 , "bold"))
battery_left_time_indicator.place(x=15,y=725)



#menu
menubar = Menu(root)
root.config(menu=menubar)

#link of repository
#https://github.com/yusifvatan/Acer-predator-sofware-for-phn16-71

def repositorylink():
    webbrowser.open('https://github.com/yusifvatan/Acer-predator-sofware-for-phn16-71', new=2)



filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Info",menu=filemenu)
filemenu.add_command(label="Repository link",command=repositorylink)





root.mainloop()



























""" Features I want add but doesn't work at the moment

Feature 1:
If laptop is plug in change refresh rate to 165.00 Hz or to 60Hz if it is unplug
What is problem? - I dont know but it doesnt work

commmd=0


while commmd==0:
    if battery_plugged==False:
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 60.00', shell=True)
    elif battery_plugged==True:
        subprocess.run('xrandr --output eDP-1-1 --mode 1920x1200 --rate 165.00', shell=True)



    
        


"""

