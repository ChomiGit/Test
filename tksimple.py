'''
Simple example Tkinter
'''

import time
import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = tk.Button(self, text='Quit', command=self.quit)
        self.timeButton = tk.Button(self, text='Time', command=self.settime)
        self.timeLabel = tk.Label(self, text='<time>')
        self.timeButton.grid()
        self.timeLabel.grid()
        self.quitButton.grid()

    def settime(self):
        self.timeLabel['text'] = time.strftime('%c')

app = Application()
app.master.title('Sample application')
app.mainloop()
