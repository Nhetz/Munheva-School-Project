# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 14:57:22 2019

@author: Ashley
"""
from tkinter import *
import tkinter.messagebox
from SignUp import SignUp
from SignIn import SignIn

class Authentication:
    
    
    def log(self):
        s = SignUp()
        i=SignIn()
        
        self.root = Tk()
        self.root.configure(bg ="lightgreen")
        self.root.title("SIGNUP")
        self.root.geometry("230x100")
        self.root.resizable(0,0)
        
        
        def signup():
            self.root.destroy()
            s.sig()
            
        def signin():
            self.root.destroy()
            i.ini()
            
        
        l1= Label(text ="Authentication", bg="lightgreen", font="Bold",fg ="red")
        l1.grid(row =0, column =4)
        b1 =Button(text ="SIGN IN", bg ="pink",font="Bold",fg="green",command =signin)
        b1.configure(width =10)
        b1.grid(row =3, column =5)
        b2 =Button(text ="SIGN UP", bg ="pink",font="Bold",fg="green",command =signup)
        b2.configure(width =10)
        b2.grid(row =4, column =5)
        
        
        self.root.mainloop()
        
    
        
c =Authentication()
c.log()