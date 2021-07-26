from tkinter import *

window=Tk()

def km_to_miles():
    print(e1_val.get())
    miles = float(e1_val.get())/1.6
    t1.insert(END,miles)

def clear():
    e1.delete(0, END)
    t1.delete(1.0, END)

b1=Button(window, text='Execute', command=km_to_miles)
b1.grid(row=0,column=0)

b2=Button(window, text='Clear', command=clear)
b2.grid(row=1,column=0)

e1_val = StringVar()
e1=Entry(window, textvariable=e1_val)
e1.grid(row=0,column=1)

t1=Text(window, height=1, width=10)
t1.grid(row=0,column=3)

window.mainloop()
