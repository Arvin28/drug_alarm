import tkinter as tk
from tkinter.constants import X, Y
import tkinter.ttk as ttk
from time import *
from typing import Counter
from threading import Thread



root= tk.Tk()
note= ttk.Notebook(root)
note.grid (row=0,column=0)


def start(number):
    if number == 1:
        seconds1 = int(sp1.get())*3600 + int(sp2.get())*60 + int(sp3.get())
        th1 = Thread(target=start, args= (seconds1, t_1,b1))
        th1.start()

def time_format (seconds):
    h = int (seconds/3600)
    tem = seconds%3600
    m = tem/60
    s = tem%60
    return '%02d:%02d:%02d:'% (h,m,s)


def time_format(seconds):
    h = int(seconds/3600)
    tem = seconds%3600
    m = tem/60
    s = tem%60
    return '%02d:%02d:%02d'%(h, m, s)

def cunter (second,var,button):
    while second:
        sleep (1)
        second = -1
        var.set(time_format(second))
    


        
    

def callback1 (a,b,c):
    n_1.set(name1.get())

def callback2 (a,b,c):
    n_2.set(name2.get())

def callback3 (a,b,c):
    n_3.set(name3.get())


def callback_time1 (a,b,c):
    timer1 = int (time1.get())
    timer2 = int (time2.get())
    timer3 = int (time3.get())
    t_1.set('%02d:%02d:%02d' % (timer1,timer2,timer3))


def callback_time2 (a,b,c):
    timer4 = int (time4.get())
    timer5 = int (time5.get())
    timer6 = int (time6.get())
    t_2.set('%02d:%02d:%02d' % (timer4,timer5,timer6))



def callback_time3 (a,b,c):
    timer7 = int (time7.get())
    timer8 = int (time8.get())
    timer9 = int (time9.get())
    t_3.set('%02d:%02d:%02d' % (timer7,timer8,timer9))




Patiens = ttk.Frame(note)
note.add(Patiens, text="Patients")




Timers = tk.Frame(note)
note.add(Timers,text="Timers",)



n_1= tk.StringVar()
n_1.set("Timer1")
tk.Label(Timers, textvariable=n_1).grid(row=0,column=0)
n_2= tk.StringVar()
n_2.set("Timer1")
tk.Label(Timers, textvariable=n_2).grid(row=0,column=1,padx=10)
n_3= tk.StringVar()
n_3.set("Timer1")
tk.Label(Timers, textvariable=n_3).grid(row=0,column=2,padx=10)

t_1=tk.StringVar()
t_1.set("00:00:00")
tk.Label (Timers,textvariable=t_1).place (x=0,y=25)

t_2=tk.StringVar()
t_2.set("00:00:00")
tk.Label (Timers,textvariable=t_2).place (x=50,y=25)

t_3=tk.StringVar()
t_3.set("00:00:00")
tk.Label (Timers,textvariable=t_3).place (x=110,y=25)


b1=tk.Button(Timers, text="Start",bg="light green",command= lambda: start(1)).place(x=1,y=60)
b2=tk.Button(Timers, text="Start",bg="light green",command=  lambda: start(2)).place(x=52,y=60)
b3=tk.Button(Timers, text="Start",bg="light green",command=  lambda: start(3)).place(x=115,y=60)

lf1= tk.LabelFrame(Patiens,text="patient1")
lf1.grid(row=0,column=0)
tk.Label(lf1, text="name").grid(row=0,column=0)
tk.Label(lf1, text="Time").grid(row=1,column=0)
name1=tk.StringVar()
name1.trace("w",callback1)
tk.Entry(lf1,textvariable=name1).grid (row=0,column=1)

lf2= tk.LabelFrame(Patiens,text="patient2")
lf2.grid(row=1,column=0)
tk.Label(lf2, text="name").grid(row=0,column=0)
tk.Label(lf2, text="Time").grid(row=1,column=0)
name2=tk.StringVar()
name2.trace("w",callback2)
tk.Entry(lf2,textvariable=name2).grid (row=0,column=1)
lf3= tk.LabelFrame(Patiens,text="patient3")
lf3.grid(row=2,column=0)
tk.Label(lf3, text="name").grid(row=0,column=0)
tk.Label(lf3, text="Time").grid(row=1,column=0)
name3=tk.StringVar()
name3.trace("w",callback3)
tk.Entry(lf3,textvariable=name3).grid (row=0,column=1)

#########################timer sters1####################################
t1 = tk.Frame(lf1)
t1.grid(row=1, column=1)
time1=tk.IntVar()
time1.trace("w",callback_time1)
sp1=tk.Spinbox(t1, from_=0, to=23, state='readonly', wrap=True, width=2,textvariable=time1).grid(row=1, column=1)
time2=tk.IntVar()
time2.trace("w",callback_time1)
sp2=tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time2).grid(row=1, column=2)
time3=tk.IntVar()
time3.trace("w",callback_time1)
tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time3).grid(row=1, column=3)
######################timer sters2########################
t1 = tk.Frame(lf2)
t1.grid(row=1, column=1)
time4=tk.IntVar()
time4.trace("w",callback_time2)
sp3=tk.Spinbox(t1, from_=0, to=23, state='readonly', wrap=True, width=2,textvariable=time4).grid(row=1, column=1)
time5=tk.IntVar()
time5.trace("w",callback_time2)
sp4=tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time5).grid(row=1, column=2)
time6=tk.IntVar()
time6.trace("w",callback_time2)
sp5=tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time6).grid(row=1, column=3)

##################timer sters3######################

t1 = tk.Frame(lf3)
t1.grid(row=1, column=1)
time7=tk.IntVar()
time7.trace("w",callback_time3)
tk.Spinbox(t1, from_=0, to=23, state='readonly', wrap=True, width=2,textvariable=time7).grid(row=1, column=1)
time8=tk.IntVar()
time8.trace("w",callback_time3)
tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time8).grid(row=1, column=2)
time9=tk.IntVar()
time9.trace("w",callback_time3)
tk.Spinbox(t1, from_=0, to=59, state='readonly', wrap=True, width=2,textvariable=time9).grid(row=1, column=3)




root.mainloop()