
import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Names')
        
        #top_frame is user defined - tkinter.Frame is in module
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.label1 = tkinter.Label(self.top_frame, text = 'John')

        self.label2 = tkinter.Label(self.top_frame, text = 'Jill')

        self.label3 = tkinter.Label(self.top_frame, text = 'James')

        #default is top
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.bottom_frame, text = 'Jack')

        self.label5 = tkinter.Label(self.bottom_frame, text = 'Jim')

        self.label6 = tkinter.Label(self.bottom_frame, text = 'Jerry')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #pack frames
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        #command function makes it so that the button reacts to being clicked
        self.mybutton = tkinter.Button(self.main_window, text = 'Click Me!', command = self.do_something)

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.mybutton.pack(side='left')
        self.quit_button.pack(side='right')


        

        tkinter.mainloop()


    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')

        
        

#instance of class
my_gui = MyGUI()

#not printed until mainloop is quit
print('moving on.....')
