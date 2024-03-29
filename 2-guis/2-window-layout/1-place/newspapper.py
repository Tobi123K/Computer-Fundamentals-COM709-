    #import everything from tkinter
from tkinter import*

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
                                     pady = 10)
    def add_email_frame(self):
        #1.object
        self.email_frame = Frame()
        self.email_frame.pack( fill=X)
        self.email_frame.configure(bg="#eee",pady = 20)

        self.email_label = Label(self.email_frame, text="Email")
        self.email_label.pack( side = LEFT, fill=X)
        self.email_label.configure(font="Arial 10",)

        self.email_entry = Entry(self.email_frame)
        self.email_entry.pack( fill=X)
        self.email_entry.configure(bg="white",
                                   width=30)
    def add_subscribe_button(self):
        #1. object
        self.subcribe_button = Button(text = "Subscribe")
        self.subcribe_button.pack(side = BOTTOM, fill=X)
        self.subcribe_button.configure(bg="#fee",font="Arial 8", width=30, height= 1, pady = 4)

# the object
if __name__ == "__main__":
    gui = NewsLetterGui()    
    gui.mainloop()
