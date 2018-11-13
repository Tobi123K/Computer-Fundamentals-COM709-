# In main folder
from NewsLetter import NewsLetterGui
# create a BotGui object
gui = NewsLetterGui() # creat class
gui.mainloop() # start up the GUI
# In newsletter.py
from tkinter import *
from tkinter import messagebox

class NewsLetterGui (Tk):

    # initialise the window
    def __init__(self):
        super().__init__()

        # set window attributes
        self.title("Newsletter")
        self.configure(bg="#eee",
                        padx= 10,
                       pady= 10,
                       width=300)
        # adding components
        self.add_heading_label()
        self.add_enter_smth()
        self.add_email_frame()
        self.add_subscribe_button()
        
    def add_heading_label(self):
        #1. creat object
        self.heading_label = Label(text="RECEIVE OUR NEWSLETTER")
        self.heading_label.pack(fill=X)
        #2. configure
        self.heading_label.configure(font="Arial 14",
                                     pady = 10)
        #3. events
    def add_enter_smth(self):
        #1. creat object
        self.enter_smth = Label(text="Please enter your email below to receive our newsletter")
        self.enter_smth.pack(fill=X)
        #2. configure
        self.enter_smth.configure(font="Arial 10",
                                     pady = 4)
    def add_email_frame(self):
        #1.object
        self.email_frame = Frame()
        self.email_frame.pack( fill=X)
        self.email_frame.configure(bg="#eee")

        self.email_label = Label(self.email_frame, text="Email")
        self.email_label.pack( side = LEFT, fill=X)
        self.email_label.configure(font="Arial 10",
                                     pady = 3)

        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack( fill=X)
        self.email_entry.configure(bg="white",
                       width=50)
    def add_subscribe_button(self):
        #1. object
        self.subcribe_button = Button(text = "Subscribe")
        self.subcribe_button.pack(side = BOTTOM)
        self.subcribe_button.configure(bg="#eee",font="Arial 8", width=8, height= 1, pady = 1 )

    # bind events 
        self.subcribe_button.bind("<ButtonRelease-1>", self.submit_button_clicked)
    def submit_button_clicked(self, event):
        num_emails = self.email_entry.get()
        messagebox.showinfo("NewsLetterGui", "Your email " + num_emails + " has been added, you nought boy!")
