
import tkinter
import tkinter.messagebox

class TestGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.geometry('600x300')
        self.main_window.title('Averages')

        self.first_frame = tkinter.Frame(self.main_window)
        self.second_frame = tkinter.Frame(self.main_window)
        self.third_frame = tkinter.Frame(self.main_window)
        self.forth_frame = tkinter.Frame(self.main_window)
        self.fifth_frame = tkinter.Frame(self.main_window)
        
        self.test1 = tkinter.Label(self.first_frame, text = "Enter the score for test 1:")
        self.test1_entry = tkinter.Entry(self.first_frame, width=10)

        self.test2 = tkinter.Label(self.second_frame, text = "Enter the score for test 2:")
        self.test2_entry = tkinter.Entry(self.second_frame, width=10)

        self.test3 = tkinter.Label(self.third_frame, text = "Enter the score for test 3:")
        self.test3_entry = tkinter.Entry(self.third_frame, width=10)
        '''
        '''
        #pack
        self.first_frame.pack()
        self.second_frame.pack()
        self.third_frame.pack()
        self.forth_frame.pack()
        self.fifth_frame.pack()
        
        self.test1.pack()
        self.test1_entry.pack()
        self.test2.pack()
        self.test2_entry.pack()
        self.test3.pack()
        self.test3_entry.pack()
        

        self.avgbutton = tkinter.Button(self.main_window, text = 'Average', command = self.average)
        self.quitbutton = tkinter.Button(self.main_window, text = 'Quit', command = self.main_window.destroy)
        
        #pack buttons
        self.avgbutton.pack()
        self.quitbutton.pack()
        
        tkinter.mainloop()
        
    def average(self):
        test1 = float(self.test1_entry.get())
        test2 = float(self.test2_entry.get())
        test3 = float(self.test3_entry.get())

        avg = (test1 + test2 + test3) / 3
        result = round(avg,2)

        tkinter.messagebox.showinfo('Results', str(result))
        
test_gui = TestGUI()
