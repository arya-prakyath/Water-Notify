# Imports
from tkinter import *
import os

# Change Dir to Project
os.chdir(r'C:\Users\aryap\Documents\Python Scripts\Water_Notify')


# Function to open Notifier | water DB
def get_file(file):
    os.startfile(file)
    return None


# Define GUI colors
bg = '#FBEAEB'
fg = '#2F3C7E'

# Create GUI
root = Tk()
root.title('Water Notification System')
root.geometry('500x300+500+150')
root.resizable(False, False)
root.iconbitmap(r'C:\Users\aryap\Documents\Python Scripts\Water_Notify\water-icon.ico')
root['bg'] = bg

# Create Title
title = Label(root,
              text="Click the button to start the notification system to \nremind every 60 Mins to drink water.",
              font="candara 16 bold",
              bg=bg, fg=fg)
title.pack(pady=25)

# Create Start Button
startBtn = Button(root,
                  text="Start Now",
                  font='candara 15 bold',
                  bg=fg, fg=bg,
                  cursor='hand2', relief='solid',
                  command=lambda: get_file(r'C:\Users\aryap\Documents\Python Scripts\Water_Notify\waterNotify.py'))
startBtn.pack(pady=(0, 2), padx=50, fill=X)

# Create Get DB Button
dbBtn = Button(root,
               text="Open DB",
               font='candara 15 bold',
               bg=fg, fg=bg,
               cursor='hand2', relief='solid',
               command=lambda: get_file(r'C:\Users\aryap\Documents\Python Scripts\Water_Notify\waterDB.txt'))
dbBtn.pack(pady=2, padx=50, fill=X)

# Create End Button
closeBtn = Button(root,
                  text="Close",
                  font='candara 15 bold',
                  bg=fg, fg=bg,
                  cursor='hand2', relief='solid',
                  command=root.quit)
closeBtn.pack(pady=2, padx=50, fill=X)

# Copyrights Section
copyrights = Label(root, text="Copyrights - THE_ARYA", font="candara 12 bold", bg=fg, fg=bg)
copyrights.pack(pady=(20, 0), fill=X, side=BOTTOM, ipady=155)

# GUI loop
root.mainloop()
