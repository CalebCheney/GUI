
import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        #configure main window
        self.main_window.geometry('500x200')
        self.main_window.title('Label Demo')

        #labels
        self.label1 = tkinter.Label(self.main_window,text = 'Hello World!')

        self.label2 = tkinter.Label(self.main_window,text = 'This is my GUI program.')

        #default is top
        self.label1.pack(side='top')
        self.label2.pack(side='bottom')

        
        tkinter.mainloop()

#instance of class
my_gui = MyGUI()

#not printed until mainloop is quit
print('moving on.....')
