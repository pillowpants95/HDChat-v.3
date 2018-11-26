######imports python tools need for ui and csv reading 
from tkinter import *
import tkinter as tk
import csv

#####establishes arrays that the lables and scripst are saved in 
smename = []
smescript = []
rname = []
rscript = []
acname = []
acscript = []
tsname = []
tsscript = []

#####pulls infor from csv and imports to arrays
for d in csv.DictReader(open('script.csv')):
          smename.append((d['smename']))
          smescript.append((d['smescript']))
          rname.append((d['rname']))
          rscript.append((d['rscript']))
          acname.append((d['acname']))
          acscript.append((d['acscript']))
          tsname.append((d['tsname']))
          tsscript.append((d['tsscript']))
          
smename = list(filter(None, smename))
smescript = list(filter(None, smescript))
rname = list(filter(None, rname))
rscript = list(filter(None, rscript))
acname = list(filter(None, acname))
acscript = list(filter(None, acscript))
tsname = list(filter(None, tsname))
tsscript = list(filter(None, tsscript))

#####functions for all the option boxes to pull the needed scripts based on the button lable
def index(*entry):
     dex = smename.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(smescript[dex])
     r.update() 
     r.destroy()
     create()
     
def rindex(*entry):
     dex = rname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(rscript[dex])
     r.update() 
     r.destroy()
     create()
     
def acindex(*entry):
     dex = acname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(acscript[dex])
     r.update() 
     r.destroy()
     create()
     
def tsindex(*entry):
     dex = tsname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(tsscript[dex])
     r.update() 
     r.destroy()
     create()
          
#####establishes ui infromation and features    
root = tk.Tk()
root.title('HD Tools')
root.attributes("-topmost", True)
frame = tk.Frame(root)
frame.pack(pady = 5, padx = 5)

####simple option box
def add_grid(data, command, title, row):
     var = StringVar(root)
     popupMenu = OptionMenu(frame, var, *data, command=command)
     popupMenu.configure(width=20)
     popupMenu.grid(row = row, column = 1)
     var.set(title)

def create():
     add_grid(smename, index, 'Start, Middle, & End', 1)
     add_grid(rname, rindex, 'Remote', 2)
     add_grid(acname, acindex, 'Abandoned Chat?', 3)
     add_grid(tsname, tsindex, 'Troubleshooting Steps', 4)

#####runs the mainloop to start the ui =
root.mainloop()
