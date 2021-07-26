from tkinter import *

window=Tk()

def kg_to_wt():
    print(e1_val.get())
    grams = float(e1_val.get())*1000
    pounds = float(e1_val.get())*2.20462
    ounces = float(e1_val.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)

def clear():
    e1.delete(0, END)
    t1.delete(1.0, END)
    t2.delete(1.0, END)
    t3.delete(1.0, END)

l1 = Label(window, text='Enter Kg')
l1.grid(row=0,column=0)

e1_val = StringVar()
e1=Entry(window, textvariable=e1_val)
e1.grid(row=0,column=1)

b1=Button(window, text='Convert', command=kg_to_wt)
b1.grid(row=0,column=2)

b2=Button(window, text='Clear', command=clear)
b2.grid(row=4,column=0)

l2 = Label(window, text='Grams')
l2.grid(row=1,column=0)

l3 = Label(window, text='Pounds')
l3.grid(row=1,column=1)

l4 = Label(window, text='Ounces')
l4.grid(row=1,column=2)

t1=Text(window, height=1, width=6)
t1.grid(row=2,column=0)

t2=Text(window, height=1, width=6)
t2.grid(row=2,column=1)

t3=Text(window, height=1, width=6)
t3.grid(row=2,column=2)

window.mainloop()
