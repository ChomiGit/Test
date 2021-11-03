from tkinter import *

def dump(*argp, **argn):
    print(argp, argn)

def dumpE(ev):
    print("//", E.get())
    print(ev)

F = LabelFrame(borderwidth=2, text="The labeled frame", relief=GROOVE)
F.pack()
B = Button(master=F, text="The button")
B.pack()
E = Entry(master=F, text="The entry")
E.pack()
B.bind('<Motion>', dump)
B.bind('<Button-1>', dumpE)
E.bind('<Any-KeyPress>', dumpE)
mainloop()
