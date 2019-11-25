# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 15:17:06 2019

@author: Ashley
"""

from db_connection import *
from tkinter import *
import tkinter.messagebox
import tkinter as tk

class SignUp:
    passe =""
    passd =""
    
    def sig(self):
        self.root = Tk()
        self.root.geometry("360x240")
        self.root.title("Registration")
        self.root.configure(bg="lightgreen")
        self.root.resizable(0,0)
        
        passe =""
        passd =""
        
        def ex():
            self.root.destroy()
            from Authenticate import Authentication
            c = Authentication()
            c.log()
        
        def reg():
            u =usertxt.get()
            p1 =pass1txt.get()
            p2 =pass2txt.get()
            e =[]
            y =[]
            em = emailtxt.get()
            if p1 !=p2:
                t1.insert(0.0,"Password Mismatch")
            elif p1==p2:
                if len(u)==0 or len(p1)==0 or len(em)==0:
                    tkinter.messagebox.showwarning("Alert","Please fill up all fields!")
                else:
                   cur.execute("select * from staff where ECNO =?",(u,))
                   for r in cur:
                       y.append(r)
                   if len(y) ==1:
                      cur.execute("select Password from staff where ECNO =?",(u,))
                      for i in cur:
                       e.append(i)
                      if e[0] ==(None,):
                         if len(p1)>6:
                             tkinter.messagebox.showwarning("Alert","Password must be at most 6")
                         if not any(char.isdigit() for char in p1):
                             tkinter.messagebox.showwarning("Alert","At least one character in the password must be a number")
                         else:
                           cur.execute("update staff set Password = ?,email=? where ECNO =?",(p1,em,u,))
                           con.commit()
                           tkinter.messagebox.showinfo("Confirmation","Congratulations, You have successfully registered")
                           y.clear()
                           e.clear()

                      else:
                         tkinter.messagebox.showinfo("Confirmation","You are already a registered teacher of this school")
                   else:
                       tkinter.messagebox.showinfo("Confirmation"," You are not a recognised Teacher of this school")
                       
            
                
                   
        
        usertxt =StringVar()
        pass1txt =StringVar()
        pass2txt= StringVar()
        emailtxt = StringVar()
        
        l1 =Label(text ="Username",font ="Bold", bg= "lightgreen")
        l1.grid(row =2,column =2)
        l1 =Label(text ="", bg= "lightgreen")
        l1.grid(row =3,column =2)
        l1 =Label(text ="",font ="Bold", bg= "lightgreen")
        l1.grid(row =5,column =2)
        l1 =Label(text ="",font ="Bold", bg= "lightgreen")
        l1.grid(row =7,column =2)
        l1 =Label(text ="",font ="Bold", bg= "lightgreen")
        l1.grid(row =9,column =2)
        
        #spaces
        
        e1 =Entry(self.root, textvar=usertxt, font ="Bold")
        e1.grid(row =2, column =4)
        l2 =Label(text ="Password", font ="Bold", bg ="lightgreen")
        l2.grid(row =4, column =2)
        e2 =Entry(self.root, textvar =pass1txt,font ="Bold",show="*")
        e2.grid(row =4, column =4)
        l3 =Label(text ="Reapeat Password", font ="Bold", bg ="lightgreen")
        l3.grid(row =6, column =2)
        e3 =Entry(self.root, textvar =pass2txt,font ="Bold",show="*")
        e3.grid(row =6, column =4)
        b1 =Button(text ="SIGNUP",bg ="black",fg ="white",command =reg)
        b1.configure(width =10)
        b1.grid(row=10,column =2)
        t1 =Text(self.root, width ="27", height =2, bg ="skyblue",fg ="black")
        t1.grid(row =10,column =4)
        l4 =Label(text ="Email", font ="Bold", bg ="lightgreen")
        l4.grid(row =8, column =2)
        e4 =Entry(self.root, textvar =emailtxt,font ="Bold")
        e4.grid(row =8, column =4)
        
        menu  =Menu(self.root)
        self.root.config(menu =menu)
        
        submen =Menu(menu)
        menu.add_cascade(label ="File",menu =submen)
        submen.add_command(label ="Exit", command= ex)
        self.root.mainloop()
      
