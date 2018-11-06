from bot2 import BotGui
# create a BotGui object
gui = BotGui() # creat class
gui.mainloop() # start up the GUI

# Import everything from tkinter

from tkinter import *
# class botgui with parenting class Tk
class BotGui(Tk):
       # pass # pass is doing nothing, but allow us to run program
       def __init__(self):
           #self means belong to the object
            super().__init__()
            # super init this object
           
            # set window attributes
            self.title("Bot Gui")
            self.geometry("300x300")
            self.configure(height = 300, width = 300)
            
    

            # add window components by
            # 1. create a component object
            self.heading_label = Label(text="Entrance Ticket")
            self.heading_label.configure(font = "Arial 24")
            self.heading_label. place(x=35, y=5)

            self.tickets_entry = Entry()
            #self.tickets_entry.configure(widht = 40)
            self.tickets_entry.place(x=10, y=50)




    # handle events
    #(callback functions
