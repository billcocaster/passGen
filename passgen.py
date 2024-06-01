from tkinter import*
import tkinter as tk
import os
import tkinter.messagebox
import ctypes
from tkinter import messagebox
import random

class passGen:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Welcome to password generator")
        self.main_window.geometry('500x200')

        self.frame1 = Frame(self.main_window)
        self.frame2 = Frame(self.main_window)
        self.frame3 = Frame(self.main_window)
        self.frame4 = Frame(self.main_window)

        self.brand = Label(self.frame1,text='Please select properties of your password',font=('MetalBlockTheta',18))
        self.brand.pack(side='top')

        self.space = Label(self.frame2,text='',font=('electrolize',15))
        self.space.pack()

        self.text = Label(self.frame2,text='Length:',font=('electrolize',15))
        self.text.pack(side='left')

        self.entry = Entry(self.frame2,width=5)
        self.entry.pack(side='left')

        self.space = Label(self.frame3,text='',font=('electrolize',10))
        self.space.pack()
        
        self.button = Button(self.frame3,text='Generate',font='electrolize',command=self.passZone)
        self.button.pack()
        
        self.passGenWord= tk.StringVar()
        self.entrypass = Entry(self.frame4,textvariable=self.passGenWord,state='readonly')
        self.entrypass.pack()
        


        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
        self.frame4.pack()
        

        mainloop()
        
    def passZone(self):
        try:
            passLength = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error","Please enter valid number")
        selections=[0,1,2,3]
        passy=""
        specialChars=[63,64,33,35,37,43,45,42]
        for i in range(passLength):
            selection=random.choice(selections)
            if selection == 0:
                o1 = chr(random.choice(specialChars))
                passy+=o1
            elif selection == 1:
                o2 = chr(random.randint(65,90))
                passy+=o2
            elif selection == 2:
                o3 = chr(random.randint(97,122))
                passy+=o3
            elif selection == 3:
                o4 = str(random.randint(0,9))
                passy+=o4
        self.passGenWord.set(passy)
                
                
            

passGen()