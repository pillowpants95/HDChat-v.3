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
     tkvar1.set('Start, Middle, & End')
     
def rindex(*entry):
     dex = rname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(rscript[dex])
     r.update() 
     r.destroy()
     tkvar2.set('Remote')
     
def acindex(*entry):
     dex = acname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(acscript[dex])
     r.update() 
     r.destroy()
     tkvar3.set('Abandoned Chat?')
     
def tsindex(*entry):
     dex = tsname.index(*entry)
     r = Tk()
     r.withdraw()
     r.clipboard_clear()
     r.clipboard_append(tsscript[dex])
     r.update() 
     r.destroy()
     tkvar4.set('Troubleshooting Steps')
          
#####establishes ui infromation and features    
root = tk.Tk()
root.title('HD Tools')
root.attributes("-topmost", True)
frame = tk.Frame(root)
frame.pack(pady = 5, padx = 5)

####simple option box
tkvar1 = StringVar(root)
popupMenu = OptionMenu(frame, tkvar1, *smename, command=index)
popupMenu.configure(width=20)
popupMenu.grid(row = 1, column = 1)
tkvar1.set('Start, Middle, & End')

tkvar2 = StringVar(root)
popupMenu = OptionMenu(frame, tkvar2, *rname, command=rindex)
popupMenu.configure(width=20)
popupMenu.grid(row = 2, column = 1)
tkvar2.set('Remote')

tkvar3 = StringVar(root)
popupMenu = OptionMenu(frame, tkvar3, *acname, command=acindex)
popupMenu.configure(width=20)
popupMenu.grid(row = 3, column = 1)
tkvar3.set('Abandoned Chat?')

tkvar4 = StringVar(root)
popupMenu = OptionMenu(frame, tkvar4, *tsname, command=tsindex)
popupMenu.configure(width=20)
popupMenu.grid(row = 4, column = 1)
tkvar4.set('Troubleshooting Steps')

#####runs the mainloop to start the ui =
root.mainloop()
