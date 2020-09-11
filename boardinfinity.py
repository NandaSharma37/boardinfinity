from tkinter import *
from tkcalendar import DateEntry
from datetime import date
import datetime

def cert():
    rut=Toplevel()
    rut.geometry('550x650')
    label=Label(rut,text="Tweet expired")
    label.place(x=230,y=295)

def certificate():
    
    global canvas
    global canvas1
    
    root=Toplevel()
    root.geometry('550x650')
   
   
    
    """label_5=Label(root,text=Username.get(),font=("bold",10))
    label_5.place(x=100,y=300)"""
    label_22=Label(root,text="Entered Tweet is",font=("bold",10))
    label_22.place(x=230,y=270)
    label=Label(root,text=Username.get())
    label.place(x=230,y=295)
    label=Label(root,text=c.get())
    label.place(x=235,y=390)
    current_day = datetime.date.today()
    """print("\n Default Date Object:", current_day, "\n")"""
 
    formatted_date = datetime.date.strftime(current_day, "%m/%d/%Y")
    """print("\n Formatted Date String:", formatted_date, "\n")"""
    if call==formatted_date:
        cert()
        
        
    

    













top=Tk()
top.geometry('500x500')
top.title("Board Infinity")
"""canvas1=Canvas(root,width=800,height=600)
canvas1.place(x=0,y=0)
myimage1=PhotoImage(file='b.gif')
canvas1.create_image(0,0,anchor=NW,image=myimage1)"""

var=IntVar()
c=StringVar()
var1=StringVar()
    
label_0=Label(top,text="BOARD INFINITY",font=("bold",20))
label_0.place(x=90,y=53)


label_1=Label(top,text="Enter Tweet",font=("bold",10))
label_1.place(x=80,y=130)
Username=Entry(top)
Username.place(x=240,y=130,width=100)
"""label_2=Label(top,text="Select Course",font=("bold",10))
label_2.place(x=80,y=200)
list1=['PYTHON','JAVA','C','C++','HTML','C#']
droplist=OptionMenu(top,c,*list1)
droplist.config(width=15)
c.set('Select Course')
droplist.place(x=240,y=195)"""
secvar=StringVar()
label_2=Label(top,text="Select expiry date",font=("bold",10))
label_2.place(x=80,y=200)
Button(top,text='SUBMIT',width=20,bg='brown',fg='white',command=certificate).place(x=180,y=280)
cal = DateEntry(top, width=12, year=2019, month=6, day=22, 
background='darkblue', foreground='white', borderwidth=2)
cal.place(x=250,y=195)




call=cal.get()

usr=Username.get()
Course=c.get()
seq=secvar.get()
plat=secvar1.get()








