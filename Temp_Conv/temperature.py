from tkinter import *

root=Tk()
root.title("CELSIUS--->FARENHEIT")

e1=Entry(root,width=30,borderwidth=5)
e1.grid(row=3,column=2)
e2=Entry(root,width=35,borderwidth=5)
e2.grid(row=3,column=3)


#Button onClicks

def click(number):
    current=e1.get()
    e1.delete(0,END)
    e1.insert(0,str(current)+str(number))


def clear():
    e1.delete(0,END)


def convert():
    num = e1.get()
    num1 = int(num)
    e2.insert(0,(num1*1.8)+32)


#Buttons
Button_1=Button(root,text="1",padx=20,pady=20,command=lambda:click(1)).grid(row=4,column=0)
Button_2=Button(root,text="2",padx=20,pady=20,command=lambda:click(2)).grid(row=4,column=1)
Button_3=Button(root,text="3",padx=20,pady=20,command=lambda:click(3)).grid(row=5,column=0)
Button_4=Button(root,text="4",padx=20,pady=20,command=lambda:click(4)).grid(row=5,column=1)
Button_5=Button(root,text="5",padx=20,pady=20,command=lambda:click(5)).grid(row=6,column=0)
Button_6=Button(root,text="6",padx=20,pady=20,command=lambda:click(6)).grid(row=6,column=1)
Button_7=Button(root,text="7",padx=20,pady=20,command=lambda:click(7)).grid(row=7,column=0)
Button_8=Button(root,text="8",padx=20,pady=20,command=lambda:click(8)).grid(row=7,column=1)
Button_9=Button(root,text="9",padx=20,pady=20,command=lambda:click(9)).grid(row=8,column=0)
Button_0=Button(root,text="0",padx=20,pady=20,command=lambda:click(0)).grid(row=8,column=1)
Button_convert=Button(root,text="--->°F",padx=30,pady=30,command=convert).grid(row=4,column=2)
Button_clear=Button(root,text="CLEAR",padx=30,pady=30,command=clear).grid(row=5,column=2)

root.mainloop()