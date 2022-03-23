import tkinter
import tkinter.messagebox


class MyGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #configure the main window
        self.main_window.geometry("500x200")
        self.main_window.title('label Demo')


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
    

        self.label1 = tkinter.Label(self.top_frame,text='John')

        self.label2 = tkinter.Label(self.top_frame,text='Jill')

        self.label3 = tkinter.Label(self.top_frame,text='James')


        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        self.label4 = tkinter.Label(self.top_frame,text='Jack')

        self.label5 = tkinter.Label(self.top_frame,text='Jim')

        self.label6 = tkinter.Label(self.top_frame,text='Jerry')

        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #Yes, we have to pack the frames too!
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.mybutton = tkinter.Button(self.main_window, text= 'Click Me!', command= self.do_something)

        self.quik_button = tkinter.Button(self.main_window,text='Quit', command= self.main_window.destroy)#always destroy the whole window


        self.mybutton.pack(side= "left")
        self.quik_button.pack(side="right")

       
        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the bottom')

        tkinter.mainloop()

my_gui = MyGUI() 

print("moving on....")

