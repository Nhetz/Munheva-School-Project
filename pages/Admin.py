# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 20:19:39 2019

@author: Ashley
"""

from tkinter import *
import tkinter.messagebox
import tkinter as tk
from admin_funct import Functions
from SignIn import *


class Admin:
    
    def admin(self):
        
        f =Functions()
        s =SignIn()
        
        self.root =Tk()
        self.root.geometry("259x163")
        self.root.title("Adminstrator Page")
        self.root.configure(bg ="lightgreen")
        self.root.resizable(0,0)
        
        def ad():
            self.root.destroy()
            f.addstaff()
            
        def logout():
            self.root.destroy()
            s.ini()
            
            
            
        def delete():
             self.root.destroy()
             f.delete()
             
        def add_course():
            self.root.destroy()
            f.add_course()
            
        l1 =Label(text ="Welcome Admistrator", font ="Bold", fg ="Orange",bg ="lightgreen")
        l1.grid(row =0, column =3)
        b1 =Button(text ="Add Staff",font ="Bold",fg ="white",bg ="black", command =ad)
        b1.configure(width =10)
        b1.grid(row =2,column =3)
         
        b2 =Button(text ="Delete Staff",font ="Bold", fg ="white", bg ="blue", command =delete)
        b2.configure(width =10)
        b2.grid(row =2,column =4)
        
        b3 =Button(text ="Update Staff", font ="Bold", fg ="Black",bg ="white")
        b3.configure(width =10)
        b3.grid(row =4, column =3)
        
        l2 =Label(text = '', bg ="lightgreen")
        l2.grid(row =3, column =3)
        
        l3 =Label(text = '',  bg ="lightgreen")
        l3.grid(row =3, column =4)
        
        l=Label(text = '',  bg ="lightgreen")
        l.grid(row =5, column =3)
        
        b4 =Button(text ="Log out", font ="Bold", fg ="Black",bg ="yellow", command =logout)
        b4.configure(width =10)
        b4.grid(row =6, column =3)
        
        b5 = Button(text ="Add Course", font ="Bold",fg ="white",bg ="purple",command=add_course)
        b5.grid(row =4, column =4)
        self.root.mainloop()
        


    