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
    
        self.radio_var = tkinter.IntVar()

        #set the default button
        self.radio_var.set(20)

        self.rb1 = tkinter.Radiobutton(self.top_frame, text = 'Optiona1', variable = self.radio_var,
        value=10)

        self.rb2 = tkinter.Radiobutton(self.top_frame, text = 'Optiona2', variable = self.radio_var,
        value=20)
        
        self.rb3 = tkinter.Radiobutton(self.top_frame, text = 'Optiona3', variable = self.radio_var,
        value=30)

        #pack the radiobuttons.
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        


        self.ok_button = tkinter.Button(self.bottom_frame, text= 'OK', command= self.show_choice)
        self.reset_button = tkinter.Button(self.bottom_frame,text='Reset', command= self.rb1.select)#always destroy the whole window
        self.quit_button = tkinter.Button(self.main_window,text='Quit', command= self.main_window.destroy)

        #pack the Buttons.
        self.ok_button.pack(side='left')
        self.reset_button.pack(side= "left")
        self.quit_button.pack(side="right")


        #Yes, we have to pack the frames too!
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")
       
        tkinter.mainloop()

    def show_choice(self):
        tkinter.messagebox.showinfo("Selection", 'You have selected option' + str(self.radio_var.get()))


my_gui = MyGUI() 

        




