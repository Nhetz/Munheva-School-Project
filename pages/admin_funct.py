# -*- coding: utf-8 -*-
"""
Created on Sun Jul  7 18:56:51 2019

@author: Ashley
"""
from tkinter import *

import sqlite3
import tkinter.messagebox
import tkinter as tk
from db_connection import *
from Authentication_time import *
import time

class Functions:
    ti =""
    def delete(self):
        self.root =Tk()
        self.root.geometry("268x93")
        self.root.configure(bg ="lightgreen")
        self.root.title("Delete Staff")
        self.root.resizable(0,0)
        
        def ex():
            
            a =tkinter.messagebox.askyesno("Exit","Do you want to exit")
            if a ==1:
                self.root.destroy()
                from Admin import Admin
                c =Admin()
                c.admin()
        
        
        def back():
            
            self.root.destroy()
            from Admin import Admin
            a =Admin()
            a.admin()
        
        
        def delete():
            y =[]
            i =ectxt.get()
            cur.execute("select * from staff where ECNO=?",(i,))
            for e in cur:
                y.append(e)
            if len(y)==1:
                cur.execute("Delete from staff where ECNO =?",(i,))
                con.commit()
                cur.execute("Update Courses set ECNO =NULL where ECNO =?",(i,))
                con.commit()
                y.clear()
                tkinter.messagebox.showinfo("Alert",i+"was successfully deleted")
            else:
                tkinter.messagebox.showinfo("Alert","No such teacher exists in the database")
        
        ectxt = StringVar()
        
        
        l =Label(text = "ECNO:", bg ="lightgreen", font ="Bold",fg ="Black")
        l.grid(row =2,column=2)
        
        l =Label(text = "", bg ="lightgreen")
        l.grid(row =2,column=3)
        
        l =Label(text = "", bg ="lightgreen")
        l.grid(row =3,column=2)
        
        e1 =Entry(self.root, textvar =ectxt,font ="Bold")
        e1.configure(width =16)
        e1.grid(row =2, column =4)
        
        b1 =Button(text ="Delete", bg ="purple",fg ="white",font ="Bold",command =delete)
        b1.configure(width =10)
        b1.grid(row =4,column =2)
        
        menu  =Menu(self.root)
        self.root.config(menu =menu)
        
        submen =Menu(menu)
        menu.add_cascade(label ="File",menu =submen)
        submen.add_command(label ="Exit", command= ex)
        
        sub = Menu(menu)
        sub.add_command(label ="Format")
        menu .add_cascade(label = "Delete", menu =sub)
        
        b2 =Button(text ="Back", bg ="purple",fg ="white",font ="Bold",command =back)
        b2.configure(width =10)
        b2.grid(row =4,column =4)
        self.root.mainloop()
        
        
    def addstaff(self):
        
        self .root =Tk()
        self.root.title("Teacher Registration")
        self.root.geometry("280x320")
        self.root.configure(bg ="lightgreen")
        self.root.resizable(0,0)
        
        ectxt = StringVar()
        nametxt = StringVar()
        v = tk.IntVar()
        x = tk.StringVar()
        tkvar =StringVar()
        
        Departments ={'Maths','Geography','Computers','History'}# Dictionary for Department Selection
        tkvar.set('Dept')
        
        Jobs ={'HOD','SNRT','GNT'}# Dictionary for Job_Status Selection
        x.set(' Title')
        
        dept =[]
        job =[]
        
        for e in Departments:
            dept.append(e)
            
        for e in Jobs:
            job.append(e)
            
        
        def ex():
            
            a =tkinter.messagebox.askyesno("Exit","Do you want to exit")
            if a ==1:
                self.root.destroy()
                from Admin import Admin
                c =Admin()
                c.admin()
                
                
        def save():
            e =ectxt.get()
            n =nametxt.get()
            t =v.get()
            y =x.get()
            k = tkvar.get()
            ECNO =[]
            Js =[]
            if (len(e)==0 or len(n)==0 or t==0 or dept.count(k)==0 or job.count(y)==0):
                tkinter.messagebox.showwarning("Alert","Please fill all fields")
            else:
                if e[0]=="T" and e[1]=="R":# teacher code is in the form TR**
                    cur.execute("select ECNO from staff where ECNO =?",(e,))
                    for i in cur:
                       ECNO.append(i)
                    if len(ECNO)==1:#checking if Teacher with the same ECNO has not been added already in the system
                       tkinter.messagebox.showerror("Alert","This teacher is already added to the system")
                       ECNO.clear()
                    else:
                      if y =="HOD":
                        cur.execute("select * from staff where Job_Status =? and Department =?",(y,k,))# making sure that there is one HOD / dept
                        for e in cur:
                           Js.append(e)
                        if len(Js)==1:
                          tkinter.messagebox.showwarning("Alert","There can be only one HOD per department")
                          Js.clear()
                        else:
                            if t ==1:# Gender
                             r ="M"
                            else:
                              r ="F" 
                            cur.execute("insert into staff(ECNO,Name,Sex,Job_Status,Department)values(?,?,?,?,?)",(e,n,r,y,k,))
                            con.commit()
                            tkinter.messagebox.showinfo("Confirmation",n + "belonging to" + "" +k + " added successfully")
                            
                      else:
                       if t ==1:# Gender
                          r ="M"
                       else:
                         r ="F" 
                       cur.execute("insert into staff(ECNO,Name,Sex,Job_Status,Department)values(?,?,?,?,?)",(e,n,r,y,k,))
                       con.commit()
                       tkinter.messagebox.showinfo("Confirmation",n + "" + "of" +""+k + "" + " added successfully")
                else:
                    tkinter.messagebox.showwarning("Alert","ECNO code is TR")
                    
                     
            
              
              
    
             
                
            
            
        l1 =Label(text ="ECNO",bg ="lightgreen", font ="Bold")
        l1.grid(row =2, column =2)
        
        l2 = Label(text  = "Name",bg ="lightgreen", font ="Bold")
        l2.grid(row =4, column =2)
        
        l3 = Label(text  = '',bg ="lightgreen")
        l3.grid(row =3, column =2)
        
        l4 = Label(text  = "Job Title",bg ="lightgreen", font ="Bold")
        l4.grid(row =6, column =2)
        
        l5 = Label(text  = '',bg ="lightgreen")
        l5.grid(row =5, column =2)
        
        l6 = Label(text  = '',bg ="lightgreen")
        l6.grid(row =5, column =3)
        
        l6 = Label(text  = '',bg ="lightgreen")
        l6.grid(row =9, column =2)
        
        popup = OptionMenu(self.root, tkvar, *Departments)
        popup.configure(width = 10, bg ="purple", fg ="white" , font ="Bold")
        popup.grid(row =14, column =4)
        
        l4 = Label(text  = "Gender",bg ="lightgreen", font ="Bold")
        l4.grid(row =11, column =2)
        
        menu  =Menu(self.root)
        self.root.config(menu =menu)
        
        submen =Menu(menu)
        menu.add_cascade(label ="File",menu =submen)
        submen.add_command(label ="Exit", command= ex)
        
        sub = Menu(menu)
        sub.add_command(label ="Format")
        menu .add_cascade(label = "Delete", menu =sub)
        
        
        r1 =Radiobutton(self.root,text ="M",value =1,bg="lightgreen", variable =v, font ="Bold")
        r1.grid(row =11, column =4)
        
        r2 = Radiobutton(self.root, text ="F", value =2, bg ="lightgreen", variable =v, font ="Bold")
        r2.grid(row=12, column =4)
        
        pop = OptionMenu(self.root,x ,*Jobs)
        pop.configure(width = 10, bg ="purple", fg ="white" , font ="Bold")
        pop.grid(row =6, column =4)
       
        
        l5 =Label(text = "Dept", font ="Bold", bg ="lightgreen")
        l5.grid(row = 14, column =2)
        
        l6 =Label(text = "", font ="Bold", bg ="lightgreen")
        l6.grid(row = 13, column =2)
        
        l6 =Label(text = "", font ="Bold", bg ="lightgreen")
        l6.grid(row = 16, column =2)
        
        e1 =Entry(self.root, textvar =ectxt, font ="Bold",bg ="white")
        e1.configure(width =14)
        e1.grid(row =2, column =4)
        
        e2 =Entry(self.root, textvar =nametxt, font ="Bold",bg ="white")
        e2.configure(width =14)
        e2.grid(row =4, column =4)
        
        b1 =Button(text ="Add", bg ="White", font ="Bold",command =save,fg ="Black")
        b1.grid(row =18, column =2)
        b1.configure(width =10)
        self.root.mainloop()
        
    def forget(self): # functionality to call when user forgets password
        self.root =Tk()
        self.root.geometry("320x170")
        self.root.configure(bg="lightgreen")
        self.root.title("Password Change")
        self.root.resizable(0,0)
        emails=[] #list to append emails from database
        
        def back():
            self.root.destroy()
            from SignIn import SignIn
            i =SignIn()
            i.ini()
        
        def change():
            e = emailtxt.get()
            p1 =pass1txt.get()
            p2 =pass2txt.get()
            cur.execute("select email from staff where email =?",(e,))
            for i in cur:
                emails.append(i)
            if len(emails)==1:
                if p1!=p2:
                    tkinter.messagebox.showwarning("Alert","Password Mismatch!")
                else:
                    cur.execute("update staff set Password =? where email =?",(p1,e,))
                    con.commit()
                    tkinter.messagebox.showinfo("Confirmation","Password Change Successfull!")
                emails.clear()
            else:
                tkinter.messagebox.showwarning("Alert","Email does not belong to any account ")
        
        emailtxt =StringVar()
        pass1txt =StringVar()
        pass2txt =StringVar()
        
        l1 =Label(text ="Email",font ="Bold",bg ="lightgreen")
        l1.grid(row =2,column=2)
        
        l =Label(text ="",bg ="lightgreen",fg ="lightgreen")
        l.grid(row =3,column=2)
        
        l =Label(text ="",bg ="lightgreen",fg ="lightgreen")
        l.grid(row =5,column=3)
        
        l =Label(text ="",bg ="lightgreen",fg ="lightgreen")
        l.grid(row =7,column=2)
        
        l =Label(text ="gjhk",bg ="lightgreen",fg ="lightgreen")
        l.grid(row =2,column=3)
        
        e1 =Entry(self.root,textvar =emailtxt,font ="Bold")
        e1.configure(width =16)
        e1.grid(row =2,column =4)
        
        l2=Label(text ="New Password",font ="Bold",bg ="lightgreen")
        l2.grid(row =4,column=2)
        
        l3 =Label(text ="Reapet Password",font ="Bold",bg ="lightgreen")
        l3.grid(row =6,column=2)
        
        e2 =Entry(self.root,textvar =pass1txt,font ="Bold",show ="*")
        e2.configure(width =16)
        e2.grid(row =4,column =4)
        
        e3 =Entry(self.root,textvar =pass2txt,font ="Bold",show="*")
        e3.configure(width =16)
        e3.grid(row =6,column =4)
        
        b1 =Button(text ="Submit" ,font ="Bold",fg ="white",bg ="purple",command =change)
        b1.configure(width=10)
        b1.grid(row =8,column=2)
        
        b2 =Button(text ="Login" ,font ="Bold",fg ="white",bg ="purple",command =back)
        b2.configure(width=10)
        b2.grid(row =8,column=4)
        
        self.root.mainloop()
        
    def add_course(self):# functionality for adminstrator to add courses done at the xul
        
        self.root =Tk()
        self.root.geometry("310x184")
        self.root.title("Course Registration")
        self.root.configure(bg ="lightgreen")
        self.root.resizable(0,0)
        
        def ex():
            
            a =tkinter.messagebox.askyesno("Exit","Do you want to exit")
            if a ==1:
                self.root.destroy()
                from Admin import Admin
                c =Admin()
                c.admin()
        
        def add():
            name =crsnm.get()
            idtx =crsid.get()
            d =dept.get()
            Depts =[]
            for e in dpt:
                Depts.append(e)
            if len(name)==0 or len(idtx)==0 or Depts.count(d)==0:
                tkinter.messagebox.showwarning("Alert","Fill all Fields!")
                
            else: 
                
                courses =[]
               
                
                if d =="Maths":
                  if idtx[0]=="M" and idtx[1]=="T":
                      cur.execute("select * from courses where CourseID =?",(idtx,))
                      for i in cur:
                          courses.append(i)
                      if len(courses)==0:
                          cur.execute("Insert into  Courses(CourseID,CourseName,Department) values(?,?,?)",(idtx,name,d,))
                          con.commit()
                          tkinter.messagebox.showinfo("Confirmation","Course successfully added")
                          courses.clear()
                      else:
                           tkinter.messagebox.showinfo("Info","Course code already in use try another one")
                  else:
                       tkinter.messagebox.showwarning("Alert","Maths Department code is MT")
                elif d =="Computers":
                    if idtx[0]=="C" and idtx[1]=="M":
                        cur.execute("select * from courses where CourseID =?",(idtx,))
                        for i in cur:
                          courses.append(i)
                        if len(courses)==0:
                          cur.execute("Insert into  Courses(CourseID,CourseName,Department) values(?,?,?)",(idtx,name,d,))
                          con.commit()
                          tkinter.messagebox.showinfo("Confirmation","Course successfully added")
                          courses.clear()
                        else:
                           tkinter.messagebox.showinfo("Info","Course code already in use try another one")
                    else:
                         tkinter.messagebox.showwarning("Alert","Computers Department code is CM")
                elif d =="Geography":
                    if idtx[0]=="G" and idtx[1]=="E" and idtx[2] =="O":
                        cur.execute("select * from courses where CourseID =?",(idtx,))
                        for i in cur:
                          courses.append(i)
                        if len(courses)==0:
                          cur.execute("Insert into  Courses(CourseID,CourseName,Department) values(?,?,?)",(idtx,name,d,))
                          con.commit()
                          tkinter.messagebox.showinfo("Confirmation","Course successfully added")
                          courses.clear()
                        else:
                           tkinter.messagebox.showinfo("Info","Course code already in use try another one")
                    else:
                      tkinter.messagebox.showwarning("Alert","Geography Department code is GEO")
                elif d:
                    if idtx[0]=="H" and idtx[1] =="I" and idtx[2]=="S":
                        cur.execute("select * from courses where CourseID =?",(idtx,))
                        for i in cur:
                          courses.append(i)
                        if len(courses)==0:
                          cur.execute("Insert into  Courses(CourseID,CourseName,Department) values(?,?,?)",(idtx,name,d,))
                          con.commit()
                          tkinter.messagebox.showinfo("Confirmation","Course successfully added")
                          courses.clear()
                        else:
                           tkinter.messagebox.showinfo("Info","Course code already in use try another one")
                    else:
                      tkinter.messagebox.showwarning("Alert","History Department code is HIS")
           
        
        crsnm =StringVar()
        crsid =StringVar()
        dept =StringVar()
        dpt ={'Maths','History','Computers','Geography'}
        dept.set("Select Department")
        
        l1 =Label(text ="CourseID",font ="Bold",bg ="lightgreen")
        l1.grid(row=2,column=2)
        
        l =Label(text ="",font ="Bold",bg ="lightgreen")
        l.grid(row=3,column=2)
        
        l2 =Label(text ="CourseName",font ="Bold",bg ="lightgreen")
        l2.grid(row=4,column=2)
        
        l =Label(text ="dfgc",font ="Bold",bg ="lightgreen",fg ="lightgreen")
        l.grid(row=3,column=3)
       
        e1 =Entry(self.root,textvar =crsid,font ="Bold")
        e1.configure(width=16)
        e1.grid(row =2, column=4)
        
        e2 =Entry(self.root,textvar =crsnm,font ="Bold")
        e2.configure(width =16)
        e2.grid(row =4, column=4)
        
        l =Label(text ="",font ="Bold",bg ="lightgreen")
        l.grid(row=5,column=2)
        
        l =Label(text ="Department",font ="Bold",bg ="lightgreen")
        l.grid(row=6,column=2)
        
        l =Label(text ="",font ="Bold",bg ="lightgreen")
        l.grid(row=7,column=2)
        
        opt =OptionMenu(self.root,dept,*dpt)
        opt.configure(bg ="purple",fg ="white",font ="Bold")
        opt.grid(row=6,column=4)
        
        menu  =Menu(self.root)
        self.root.config(menu =menu)
        
        submen =Menu(menu)
        menu.add_cascade(label ="File",menu =submen)
        submen.add_command(label ="Exit", command= ex)
        
        sub = Menu(menu)
        sub.add_command(label ="Format")
        menu .add_cascade(label = "Delete", menu =sub)
        
        
        b1 =Button(text ="Add", font ="Bold", command =add)
        b1.configure(width =10,bg ="Orange")
        b1.grid(row =8,column=2)
        self.root.mainloop()
        
        
                           