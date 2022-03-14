
import tkinter
import tkinter.messagebox

class KiloConverterGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('500x200')
        self.main_window.title('Names')
        
        #top_frame is user defined - tkinter.Frame is in module
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.top_frame, text = 'Enter a distance in Kilometers:')
        self.kilo_entry = tkinter.Entry(self.top_frame, width = 10)

        

        #default is top
        self.prompt_label.pack(side='left')
        self.kilo_entry.pack(side='left')
       

        #pack frames
        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        #command function makes it so that the button reacts to being clicked
        self.calcbutton = tkinter.Button(self.main_window, text = 'Convert', command = self.convert)

        self.quit_button = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)

        self.calcbutton.pack(side='left')
        self.quit_button.pack(side='right')


        

        tkinter.mainloop()


    def convert(self):
        #get method built into tkinter module
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214, 2)
        #
        tkinter.messagebox.showinfo('Results', str(kilo) + ' kilometers is equal to ' + str(miles) + ' miles.')

        
        

#instance of class
Kilo_conv = KiloConverterGUI()


