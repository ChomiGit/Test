from tkinter import *

F = Frame(borderwidth=3, relief=GROOVE)
F.master.columnconfigure(0, weight=1)
F.master.rowconfigure(0, weight=1)
F.grid(sticky="EWNS")

F.columnconfigure(0, weight=1)
F.columnconfigure(1, weight=1)
F.rowconfigure(0, weight=0)
F.rowconfigure(1, weight=1)

B1 = Button(master=F, text="B1")
B1.grid(sticky="EW")
B2 = Button(master=F, text="B2")
B2.grid(row=0, column=1)
L = Label(master=F, text="The text")
L.grid()

mainloop()
