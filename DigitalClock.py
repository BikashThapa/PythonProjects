import sys
from tkinter import Tk,Label
import time
from datetime import date

#defining the function for the time and refreshes each after 200 ms
def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)

#root is the variable made for the container of tkinter
root = Tk()
root.geometry("600x300")
clock = Label(root,font=("times", 80,"bold" ),bg="white")
clock.grid(row=1, column=2,pady=30,padx=80)
times()

digi =Label(root,text="Digital Clock",font=("times 30 bold"))
digi.grid(row=0,column=2)

nota = Label(root,text="   hours      minutes     seconds    ",font="times 25 bold")
nota.grid(row=3,column=2)

root.mainloop()