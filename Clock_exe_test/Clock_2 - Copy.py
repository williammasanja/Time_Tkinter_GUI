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
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
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
    a_p = time.strftime("%p")
    lbl7.config(text=a_p)
    lbl7.after(1000, am_pm)




#Time Label
frame1 = Frame(root)
lbl = Label(frame1, text="")
lbl.config(font=("Arial Black", 15,))

#MainFrame or frame2
frame2 = Frame(root, width=400, height=300)
#frame2.config(width=400, height=300)


#moon_img = ImageTk.PhotoImage(Image.open("C_Images/moon.jpeg"))
#ImageList = [sun_img, moon_img]

#Time/Date or Frame3  
frame3 = Frame(frame2,)
#frame3.config(width=100)

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

#Image Frame or frame4
frame4 = Frame(frame2)
img = Image.open("C_Images/sun.png")
resizedimg1 = img.resize((170, 170))
newimg1 = ImageTk.PhotoImage(resizedimg1)
lbl3 = Label(frame4, image=newimg1)








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