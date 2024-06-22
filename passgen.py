from tkinter import*
import tkinter as tk
import os
import tkinter.messagebox
import ctypes
from tkinter import messagebox
import random
from tkinter import font
from tkinter import ttk
import customtkinter

class passGen:
    def __init__(self):
        self.main_window = customtkinter.CTk()
        self.main_window.title("Welcome to password generator")
        self.main_window.geometry('385x550')
        self.main_window.grid_columnconfigure(0, weight=1)
        self.main_window.grid_rowconfigure((0, 1), weight=1)
        self.main_window.resizable(width=False,height=False)
        self.main_window.grab_set()


        brandFrame = customtkinter.CTkFrame(self.main_window,fg_color='#F28705',corner_radius=5)
        brandFrame.grid(row=0,column=0,sticky='w',padx=10,pady=10)
        

        
        self.checkFrame = customtkinter.CTkFrame(self.main_window,fg_color='#243748')
        self.checkFrame.grid(row=1,column=0,sticky='nsw',padx=(10,0),pady=(0,10))


        brandFont = customtkinter.CTkFont(family="cascadia code",size=25,slant='roman',weight='bold')
        checkTitleFont = customtkinter.CTkFont(family="helvetica neue",size=18,slant='italic')
        self.reminderFontLessEq2 = customtkinter.CTkFont(family="helvetica neue",size=10,slant="italic",weight='bold')
        self.reminderFont3 = customtkinter.CTkFont(family="helvetica neue",size=10,slant="italic",weight='normal') 
    
    
        brand = customtkinter.CTkLabel(brandFrame,text=' passGen ',font=brandFont,text_color='#F20530')
        brand.grid(row=0,column=0,padx=0,pady=2,sticky='w')



        self.entry = customtkinter.CTkEntry(self.checkFrame,width=55,placeholder_text='Length',placeholder_text_color='#F2F2F2',fg_color='#2C2C2C',
                                            border_color='#F28705')
        self.entry.grid(row=5,column=0,sticky='w',padx=5,pady=5)
        
        
        
        checkTitle = customtkinter.CTkLabel(self.checkFrame,text='Please select properties of your password',font=checkTitleFont,fg_color='#F28705',
                                            corner_radius=5,text_color='#F2F2F2')
        checkTitle.grid(row=0,column=0,padx=10,pady=10)


        self.checkSpecVar = tk.IntVar()
        checkSpec = customtkinter.CTkCheckBox(self.checkFrame,text='Special chars',variable=self.checkSpecVar,onvalue=1,offvalue=0,command=self.reminders,fg_color='#F28705'
                                              ,hover_color='#2C2C2C',corner_radius=50,border_color='#F28705')
        checkSpec.grid(row=1,column=0,sticky='w',padx=5,pady=5)
        
        self.checkNumVar = tk.IntVar()
        checkNum = customtkinter.CTkCheckBox(self.checkFrame,text='Numbers',variable=self.checkNumVar,onvalue=4,offvalue=0,command=self.reminders,fg_color='#F28705'
                                             ,hover_color='#2C2C2C',corner_radius=50,border_color='#F28705')
        checkNum.grid(row=2,column=0,sticky='w',padx=5,pady=5)
        
        self.checkDownVar = tk.IntVar()
        checkDown = customtkinter.CTkCheckBox(self.checkFrame,text='Downletters',variable=self.checkDownVar,onvalue=3,offvalue=0,command=self.reminders,fg_color='#F28705'
                                              ,hover_color='#2C2C2C',corner_radius=50,border_color='#F28705')
        checkDown.grid(row=3,column=0,sticky='w',padx=5,pady=5)

        self.checkUpVar = tk.IntVar()
        checkUp = customtkinter.CTkCheckBox(self.checkFrame,text='Upletters',variable=self.checkUpVar,onvalue=2,offvalue=0,command=self.reminders,fg_color='#F28705'
                                            ,hover_color='#2C2C2C',corner_radius=50,border_color='#F28705')
        checkUp.grid(row=4,column=0,sticky='w',padx=5,pady=5)

        button = customtkinter.CTkButton(self.checkFrame,text='Generate',command=self.passZone,fg_color='#F20530',text_color='#F2F2F2')
        button.grid(row=6,column=0,pady=(20,0),sticky='w',padx=5)
        
        self.passGenWord= tk.StringVar()
        entrypass = customtkinter.CTkEntry(self.checkFrame,textvariable=self.passGenWord,state='readonly',text_color='#F2F2F2',width=280)
        entrypass.grid(row=7,column=0,pady=50)
        
        historyButton = customtkinter.CTkButton(self.checkFrame,text='Password History',command=self.historyAdder,fg_color='#F20530',text_color='#F2F2F2')
        historyButton.grid(row=6,column=0,sticky='e',pady=(20,0),padx=5)
        
        self.reminder = None
        self.passwordHistory = []



        self.main_window.mainloop()
        
    def passZone(self):
        try:
            passLength = int(self.entry.get())
            if passLength<=0:
                raise ValueError("Length must be a positive number.")
        except ValueError:
            self.errorMessages("Length Error","Please enter valid length")
            return
            
        selections = self.filters()
        
        if not selections:
            self.errorMessages("Property Error", "Please select at least one property")
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
        self.passwordHistory.append(passy)

        
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
            self.reminder = customtkinter.CTkLabel(self.checkFrame, text='Not recommended',font=self.reminderFontLessEq2,text_color='#F20530')
            self.reminder.grid(row=8,column=0,sticky='s',padx=5)
        elif len(selections) == 3:
            self.reminder = customtkinter.CTkLabel(self.checkFrame, text="These types of passwords are good but \nit's recommended to use passwords that contain all these 4 options",
                                  font=self.reminderFont3,text_color='#F28705')
            self.reminder.grid(row=8,column=0)
        
    def errorMessages(self, title, message):
        errorWindow = customtkinter.CTkToplevel(self.main_window)
        errorWindow.title(title)
        errorWindow.geometry("250x120")
        
        errorWindow.transient(self.main_window)
        errorWindow.grab_set()
        
        errorLabel = customtkinter.CTkLabel(errorWindow,text=message,wraplength=250)
        errorLabel.grid(row=0,column=0,padx=20,pady=20)
        
        okButton = customtkinter.CTkButton(errorWindow,text="OK",command=errorWindow.destroy)
        okButton.grid(pady=5,row=1,column=0,sticky='ns')
        
    def historyAdder(self):
        historyWindow = customtkinter.CTkToplevel(self.main_window)
        historyWindow.title("Password History")
        historyWindow.geometry("500x500")
        
        historyWindow.transient(self.main_window)
        historyWindow.grab_set()

        historyFrame = customtkinter.CTkScrollableFrame(historyWindow,width=450,height=450)
        historyFrame.grid(row=0,column=0,padx=10,pady=10)
        
        for i, password in enumerate(self.passwordHistory):
            tempStr = tk.StringVar(value=password)
            temp = customtkinter.CTkEntry(historyFrame,textvariable=tempStr,state='readonly',width=300)
            temp.grid(row=i,column=0,padx=5,pady=5)

       
passGen()