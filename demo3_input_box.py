import tkinter
import tkinter.messagebox


class KiloConvertGUI:
    def __init__(self):
        self.main_window= tkinter.Tk()

        #configure the main window
        self.main_window.geometry("500x200")
        self.main_window.title('label Demo')


        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
    
        #calculation
        self.prompt_label1 = tkinter.Label(self.top_frame,text='Enter a distance in Kilometers:')

        self.kilo_entry = tkinter.Entry(self.top_frame, width=10)

        self.prompt_label1.pack(side="left")
        self.kilo_entry.pack(side="left")


        #Yes, we have to pack the frames too!
        self.top_frame.pack(side="top")
        self.bottom_frame.pack(side="top")

        self.calbutton = tkinter.Button(self.main_window, text= 'Convert', command= self.convert)

        self.quik_button = tkinter.Button(self.main_window,text='Quit', command= self.main_window.destroy)#always destroy the whole window


        self.calbutton.pack(side= "left")
        self.quik_button.pack(side="right")

       
        tkinter.mainloop()

    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round((kilo*0.6214), 2)



        tkinter.messagebox.showinfo('Results', str(kilo) + 'kilometers is equal to' + str(miles)+ 'miles.' )

        

my_gui = KiloConvertGUI() 



