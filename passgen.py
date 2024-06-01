from tkinter import*
import tkinter as tk
import os
import tkinter.messagebox
import ctypes
from tkinter import messagebox
import random
from tkinter import font
from tkinter import ttk

class passGen:
    def __init__(self):
        self.main_window = Tk()
        self.main_window.title("Welcome to password generator")
        self.main_window.geometry('500x500')

        self.frame1 = Frame(self.main_window)
        self.frame2 = Frame(self.main_window)
        self.checkFrame = Frame(self.main_window)
        self.frame3 = Frame(self.main_window)
        self.frame4 = Frame(self.main_window)

        self.brandFont = font.Font(family="helvetica",size=18,slant="roman")
        self.labelFont = font.Font(family="helvetica",size=18,slant="italic")
        
        self.brand = Label(self.frame1,text='Please select properties of your password',font=self.brandFont)
        self.brand.pack(side='top')

        self.space = Label(self.frame2,text='',font=('electrolize',15))
        self.space.pack()

        self.text = Label(self.frame2,text='Length:',font=self.labelFont)
        self.text.pack(side='left')

        self.entry = Entry(self.frame2,width=5)
        self.entry.pack(side='right')
        
        stil = ttk.Style()
        stil.configure("TCheckbutton", font=('Helvetica', 18, 'italic'))
        
        self.checkSpecVar = tk.IntVar()
        self.checkSpec = ttk.Checkbutton(self.checkFrame,text='Special chars',style="TCheckbutton",variable=self.checkSpecVar,onvalue=1,offvalue=0)
        self.checkSpec.pack()        
        
        self.checkNumVar = tk.IntVar()
        self.checkNum = ttk.Checkbutton(self.checkFrame,text='Numbers',style="TCheckbutton",variable=self.checkNumVar,onvalue=4,offvalue=0)
        self.checkNum.pack()        
        
        self.checkDownVar = tk.IntVar()
        self.checkDown = ttk.Checkbutton(self.checkFrame,text='Downletters',style="TCheckbutton",variable=self.checkDownVar,onvalue=3,offvalue=0)
        self.checkDown.pack()        

        self.checkUpVar = tk.IntVar()
        self.checkUp = ttk.Checkbutton(self.checkFrame,text='Upletters',style="TCheckbutton",variable=self.checkUpVar,onvalue=2,offvalue=0)
        self.checkUp.pack()        



        self.space = Label(self.frame3,text='',font=('electrolize',10))
        self.space.pack()
        
        self.button = Button(self.frame3,text='Generate',font='electrolize',command=self.passZone)
        self.button.pack()
        
        self.passGenWord= tk.StringVar()
        self.entrypass = Entry(self.frame4,textvariable=self.passGenWord,state='readonly')
        self.entrypass.config(readonlybackground=self.entrypass.cget('background'), fg='black', highlightthickness=0, borderwidth=0)
        self.entrypass.pack(padx=10,pady=10)
        


        self.frame1.pack()
        self.frame2.pack()
        self.checkFrame.pack()
        self.frame3.pack()
        self.frame4.pack()
        

        mainloop()
        
    def passZone(self):
        try:
            passLength = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Error","Please enter valid length")
        selections=[]
        if self.checkSpecVar.get() !=0:
            selections.append(self.checkSpecVar.get())
        if self.checkNumVar.get() !=0:
            selections.append(self.checkNumVar.get())
        if self.checkDownVar.get() !=0:
            selections.append(self.checkDownVar.get())
        if self.checkUpVar.get() !=0:
            selections.append(self.checkUpVar.get())

        passy=""
        specialChars=[63,64,33,35,37,43,45,42]
        
        for i in range(passLength):
            selection=random.choice(selections)
            if selection == 1:
                o1 = chr(random.choice(specialChars))
                passy+=o1
            elif selection == 2:
                o2 = chr(random.randint(65,90))
                passy+=o2
            elif selection == 3:
                o3 = chr(random.randint(97,122))
                passy+=o3
            elif selection == 4:
                o4 = str(random.randint(0,9))
                passy+=o4
        self.passGenWord.set(passy)
                
                
            

passGen()