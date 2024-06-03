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
        self.main_window.geometry('650x500')

        frame1 = Frame(self.main_window)
        frame2 = Frame(self.main_window)
        checkFrame = Frame(self.main_window)
        frame3 = Frame(self.main_window)
        frame4 = Frame(self.main_window)
        self.frame5 = Frame(self.main_window)

        brandFont = font.Font(family="helvetica",size=18,slant="roman")
        labelFont = font.Font(family="helvetica",size=18,slant="italic")
        self.reminderFontLessEq2 = font.Font(family="helvetica",size=10,slant="italic")
        self.reminderFont3 = font.Font(family="helvetica",size=10,slant="italic") 
        
        brand = Label(frame1,text='Please select properties of your password',font=brandFont)
        brand.pack(side='top')

        space = Label(frame2,text='',font=('electrolize',15))
        space.pack()

        text = Label(frame2,text='Length:',font=labelFont)
        text.pack(side='left')

        self.entry = Entry(frame2,width=5)
        self.entry.pack(side='right')
        
        stil = ttk.Style()
        stil.configure("TCheckbutton", font=('Helvetica', 18, 'italic'))
        
        self.checkSpecVar = tk.IntVar()
        checkSpec = ttk.Checkbutton(checkFrame,text='Special chars',style="TCheckbutton",variable=self.checkSpecVar,onvalue=1,offvalue=0,command=self.reminders)
        checkSpec.pack()        
        
        self.checkNumVar = tk.IntVar()
        checkNum = ttk.Checkbutton(checkFrame,text='Numbers',style="TCheckbutton",variable=self.checkNumVar,onvalue=4,offvalue=0,command=self.reminders)
        checkNum.pack()        
        
        self.checkDownVar = tk.IntVar()
        checkDown = ttk.Checkbutton(checkFrame,text='Downletters',style="TCheckbutton",variable=self.checkDownVar,onvalue=3,offvalue=0,command=self.reminders)
        checkDown.pack()        

        self.checkUpVar = tk.IntVar()
        checkUp = ttk.Checkbutton(checkFrame,text='Upletters',style="TCheckbutton",variable=self.checkUpVar,onvalue=2,offvalue=0,command=self.reminders)
        checkUp.pack()        



        space = Label(frame3,text='',font=('electrolize',10))
        space.pack()
        
        button = Button(frame3,text='Generate',font='electrolize',command=self.passZone)
        button.pack()
        
        self.passGenWord= tk.StringVar()
        entrypass = Entry(frame4,textvariable=self.passGenWord,state='readonly')
        entrypass.config(readonlybackground=entrypass.cget('background'), fg='black', highlightthickness=0, borderwidth=0)
        entrypass.pack(padx=10,pady=10)
        
        self.reminder = None
        

        


        frame1.pack()
        frame2.pack()
        checkFrame.pack()
        frame3.pack()
        frame4.pack()
        self.frame5.pack()
        

        mainloop()
        
    def passZone(self):
        try:
            passLength = int(self.entry.get())
            if passLength<=0:
                raise ValueError("Length must be a positive number.")
        except ValueError:
            messagebox.showerror("Error","Please enter valid length")
            return
            
        selections = self.filters()
        
        if not selections:
            messagebox.showerror("Error", "Please select at least one property")
            return
        
        passy=""
        specialChars = [33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 
                       58, 59, 60, 61, 62, 63, 64, 91, 92, 93, 94, 95, 96, 123, 124, 125, 126]
        
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
        
    def filters(self):
        selections=[]
        if self.checkSpecVar.get() !=0:
            selections.append(self.checkSpecVar.get())
        if self.checkNumVar.get() !=0:
            selections.append(self.checkNumVar.get())
        if self.checkDownVar.get() !=0:
            selections.append(self.checkDownVar.get())
        if self.checkUpVar.get() !=0:
            selections.append(self.checkUpVar.get())
        return selections
    
    def reminders(self):
        selections = self.filters()
        if self.reminder:
            self.reminder.destroy()
        if len(selections) <= 2:
            self.reminder = Label(self.frame5, text='Not recommended',foreground='red',font=("helvetica",10,"bold"))
            self.reminder.pack()
        elif len(selections) == 3:
            self.reminder = Label(self.frame5, text="These types of passwords are good but it's recommended to use passwords that contain all these 4 options",foreground='orange',
                                  font=self.reminderFont3)
            self.reminder.pack()
        

            
        
        
        
                
                
            

passGen()