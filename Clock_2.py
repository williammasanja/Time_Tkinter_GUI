

from calendar import week
from tkinter import *
from PIL import ImageTk, Image
import time


root = Tk()
root.title('Time')
root.geometry('490x230')
root.resizable(width=False, height=False)

def clock():
    global Time
    global hour
    global minute
    global militarytime
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    militarytime = int(hour+minute)
    #print(minute)
    Time = hour + ':' + minute + ':' + second
    lbl5.config(text=Time)
    lbl5.after(1000, clock)
def date():
    weekday = time.strftime("%A")
    day = time.strftime("%d")
    month = time.strftime("%B")
    year = time.strftime("%Y")
    weekday = weekday[:3]

    lbl6.config(text= weekday+ ' '+day+ ' '+month+ ' ' + year)
    lbl6.after(86400000, date)

def am_pm():
    global a_p
    a_p = time.strftime("%p")
    lbl7.config(text=a_p)
    lbl7.after(1000, am_pm)
def Refresh():
    global Time
    global militarytime
    global minute
    global a_p
    global lbl3
    global img
    global resizedimg
    global newimg 
    hour = time.strftime("%H")
    #print(Time)
    #print(a_p)
    #print(int(hour))
    minute = time.strftime("%M")
    militarytime = int(hour+minute)
    a_p = time.strftime("%p")
    # Code is finicky. Add restraints so that it will show the correct image between the section of corresponding hours (and/or minutes) of each day. example: 11:00 pm - 1:00am is Midnight
    if int(hour) >=  23 and a_p == "PM" or int(hour) >= 0 and int(hour) < 1 and a_p == "AM":
        img = Image.open("C_Images/Midnight.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)
        lbl3.after(1000, Refresh)
    elif int(hour) >= 1 and militarytime < 430 and a_p == "AM":
        img = Image.open("C_Images/Night.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg) 
        lbl3.after(1000, Refresh)

    elif militarytime >= 430 and int(hour) < 8 and a_p == "AM":
        img = Image.open("C_Images/EarlyMorning.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)    
        lbl3.after(1000, Refresh)

    elif int(hour) >=  8 and int(hour) < 11 and a_p == "AM":
        img = Image.open("C_Images/LateMorning.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)
        lbl3.after(1000, Refresh)

    elif int(hour) >= 11 and a_p == "AM" or militarytime < 1330 and a_p == "PM":        
        img = Image.open("C_Images/EarlyAfternoon.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)
        lbl3.after(1000, Refresh)

    elif militarytime >= 1330 and militarytime < 1630 and a_p == "PM":        
        img = Image.open("C_Images/LateAfternoon.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)
        lbl3.after(1000, Refresh)

    elif militarytime >= 1630 and int(hour) < 18 and a_p == "PM":
        img = Image.open("C_Images/EarlyEvening.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)  
        lbl3.after(1000, Refresh)

    elif int(hour) >= 18 and militarytime < 2030 and a_p == "PM":        
        img = Image.open("C_Images/LateEvening.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)
        lbl3.after(1000, Refresh)

    elif militarytime >= 2030 and int(hour) < 23 and a_p == "PM":
        img = Image.open("C_Images/Night.png")
        resizedimg = img.resize((170, 170))
        newimg = ImageTk.PhotoImage(resizedimg) 
        lbl3.config(image=newimg)     
        lbl3.after(1000, Refresh)
   
    
    
        
        
  
       
   

    
#Time Label
frame1 = Frame(root)
lbl = Label(frame1, text="")
lbl.config(font=("Arial Black", 15,))


#MainFrame or frame2
frame2 = Frame(root, width=400, height=300)

#Time/Date or Frame3  
frame3 = Frame(frame2,)
#frame3.config(width=100)

#Image Frame or frame4
frame4 = Frame(frame2)
img = Image.open("C_Images/sun.png")
resizedimg = img.resize((170, 170))
newimg = ImageTk.PhotoImage(resizedimg)
lbl3 = Label(frame4, image=newimg)
Refresh()

#Time or Frame5
frame5=Frame(frame3)
lbl5 = Label(frame5, text='' )
lbl5.config(font=("Arial Black", 30,))
clock()

#Date or Frame6
frame6=Frame(frame3)
lbl6 = Label(frame6, text= '')
date()

#Am/Pm or Frame7
frame7=Frame(frame3)
lbl7 = Label(frame7, text= '')
lbl7.config(font=("Arial Black", 14,))
am_pm()

#Time Grid
frame1.grid(row=0, column=0, sticky = 'w')
lbl.grid(row=0, column=0)
#Frame2 Grid
frame2.grid(row=1,column=0)

#Frame3 Grid
frame3.grid(row=0, column=0, sticky='n', padx=(30,40),)

#Frame4 Grid
frame4.grid(row=0, column=1, sticky='e', pady=(0,0))
lbl3.grid(row=0, column=0 )

#Frame5 Grid
frame5.grid(row=0,column=0, pady=(40, 0))
lbl5.grid(row=0, column=0)

#Frame6 Grid
frame6.grid(row=1, column=0, padx=(50, 0 ), )
lbl6.grid(row=0, column=0)

#Frame7 grid
frame7.grid(row=0, column=1, pady= (20, 0))
lbl7.grid(row=0, column=0)
root.mainloop()