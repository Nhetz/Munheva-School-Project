# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:36:50 2019

@author: Ashley
"""
from array import *
from db_connection import *
from tkinter import *
import tkinter.messagebox
import tkinter as tk
from SignUp import *
from Authentication_time import *
import time


class SignIn:
    def ini(self): 
        ti =time.asctime(time.localtime(time.time()))
        self.root =Tk()
        self.root.geometry("300x100")
        self.root.title("SIGN IN")
        self.root.configure(bg ="lightgreen")
        self.root.resizable(0,0)
        
        def forget():
            self.root.destroy()
            from admin_funct import Functions
            a= Functions()
            a.forget()
            
        def ex():
            self.root.destroy()
            from Authenticate import Authentication
            c = Authentication
            c.log()

        
        def sig():
            u=usertxt.get()
            p =passtxt.get()
            t =[]
            y =[]
            dep=[]
            cur.execute("select * from staff where ECNO =? and Password =?",(u,p))
            for e in cur:
                t.append(e)
            if len(t)==1:
               cur.execute("select Job_Status from staff where ECNO =? and Password =?",(u,p))
               for e in cur:
                   y.append(e)
               if y[0] ==('Admin',):
                   self.root.destroy()
                   from Admin import Admin
                   d = Admin()
                   d.admin()
               elif y[0]==('HOD',):
                    arr = array('i',[])
                    cur.execute("insert into login_details(ECNO,Login) values(?,?)",(u,tm,))
                    con.commit()
                    cur .execute("select Number from login_details where Login =?",(tm,))
                    for e in cur:
                        for i in e:
                          arr.append(i)
                    for e in arr:
                        no =e
                    cur.execute("select department from staff where ECNO =?",(u,))
                    for i in cur:
                       dep.append(i)
                    for i in dep:
                        for e in i:
                           dept =e
                    dep.clear()
                    cur.execute("select Name from staff where ECNO =?",(u,))
                    for e in cur:
                        dep.append(e)
                    for e in dep:
                        for i in e:
                            Name =i
                    self.root.destroy()       
                    root =Tk()
                    root.geometry("250x200")
                    root.configure(bg ="lightgreen")
                    root.title("HOD")
                    root.resizable(0,0)

                    s =tk.StringVar()
                    Stat ={'SNRT','GNT'}
                    s.set("Status")
                    name =[]
                    
                    def view():
                        r =s.get()
                        cur.execute("select Name from staff where Job_Status=? and Department =?",(r,dept,))
                        for e in cur:
                            name.append(e)
                        for e in name:
                              for i in e:
                                 stm = i,"\n"
                                 for e in stm:
                                    text.insert(0.0,e)
                    def back():
                        cur.execute("Update login_details set logout =? where Number =?",(ti,no,))
                        con.commit()
                        root.destroy()
                        c =SignIn()
                        c.ini()
                           
                        
                        
                            
                                  
                        
                    def assign(): 
                       root.destroy()
                       window =Tk()
                       window.configure(bg ="lightgreen")
                       window.title("Teacher Assignment")
                       window.geometry("330x200")
                       window.resizable(0,0)
                       
                       
                       cur.execute("select CourseName from Courses where Department =?" ,(dept,))
                       courses={}
                       course =StringVar()
                       course.set("Select Course")
                       teachers ={}
                       trs =StringVar()
                       trs.set("Select Teacher")
                       for e in cur:
                           for i in e:
                               courses.setdefault(i)
                                   
                       cur.execute("select Name from staff where Department =?",(dept,))
                       for e in cur:
                           for i in e:
                                teachers.setdefault(i)
                      
                         
                       def assign():
                           ECNO=[]
                           c =course.get()
                           t =trs.get()
                           cur.execute("select ECNO from staff where Name=?",(t,))
                           for e in cur:
                               for i in e:
                                   ecno =i
                           cur.execute("select ECNO from courses where CourseName =?",(c,))
                           for e in cur:
                               ECNO.append(e)
                           if ECNO[0]==(None,):
                               cur.execute("update courses set ECNO =? where CourseName =?" ,(ecno,c,))
                               con.commit()
                               tkinter.messagebox.showinfo("Confirmation","Course Assignment to the teacher successfull")
                           else:
                               tkinter.messagebox.showwarning("Alert","This course was already assigned a teacher")
                       
                       def back():
                            cur.execute("update login_details set Logout =? where Number =?",(ti,no,))
                            window.destroy()
                            c =SignIn()
                            c.ini()
                           
                               
                           
                           
                           
                           
                       l1 =Label(text ="HOD", font ="Bold", fg ="Blue", bg ="lightgreen")
                       l1.grid(row=1,column =2)
                       
                       l2 =Label(text =Name, font ="Bold",bg ="lightgreen", fg ="red")
                       l2.grid(row =2, column =2)
                       
                       l1 =Label(text ="", font ="Bold", bg ="lightgreen")
                       l1.grid(row=3,column =2)
                       
                       l1 =Label(text ="", font ="Bold", bg ="lightgreen")
                       l1.grid(row=6,column =2)
                       
                       opt =OptionMenu(window,course,*courses)
                       opt.configure(width=19,bg ="purple",fg ="white",font ="Bold")
                       opt.grid(row =4, column =3)
                       
                       opt1 =OptionMenu(window,trs,*teachers)
                       opt1.configure(width=19,bg ="purple",fg="white",font ="Bold")
                       opt1.grid(row =5, column =3)
                       
                       B1 =Button(text ="Assign", command =assign, font ="Bold")
                       B1.configure(width=10,bg="Black",fg="white")
                       B1.grid(row =7,column =2)
                       
                       B2 = Button(text ="Log out", font ="Bold",bg ="yellow", command =back)
                       B2.configure(width =10)
                       B2.grid(row =7, column =3)
                      
                       window.mainloop()
                    
                    opt =OptionMenu(root,s,*Stat)
                    opt.configure(width =6,bg ="purple", fg ="white", font ="Bold")
                    opt.grid(row =2, column =2)
                    text =Text(root,width =13,height =7)
                    text.grid(row =2, column =4)
                    l1 =Label(text ="vnvnv", fg ="lightgreen", bg= "lightgreen")
                    l1.grid(row =2, column =3)
                    
                    l1 =Label(text ="vnvnv", fg ="lightgreen", bg= "lightgreen")
                    l1.grid(row =5, column =2)
                    
                    b1 =Button(text ="View", bg ="Black", fg ="white", font ="Bold",command =view)
                    b1.configure(width =10)
                    b1.grid(row =4, column =2)
                    b2 =Button(text ="Assign", bg= "Blue", fg ="white", font ="Bold", command =assign)
                    b2.grid(row =6, column =4)
                    b2.configure(width =10)
                    
                    b3 =Button(text ="Log out", bg ="Yellow", font ="Bold", command =back)
                    b3.configure(width =10)
                    b3.grid(row =6, column =2)
                    root.mainloop()
                    
               else:
                lg =array('i',[])
                cur.execute("insert into login_details(ECNO, Login) values(?,?)",(u,tm,))
                con.commit()
                cur.execute("select Number from login_details where login =?",(tm,))
                for e in cur:
                    for i in e:
                      lg.append(i)
                for e in lg:
                        lo = e
                self.root.destroy()
                teacher =[]
                cur.execute("select Name from staff where ECNO =?",(u,))
                for e in cur:
                    teacher.append(e)
                for e in teacher:
                    for i in e:
                        nm =i
                teacher.clear()
                main =Tk()
                main.geometry("330x330")
                main.configure(bg ="lightgreen")
                main.title("Teacher")
                
                def courses():
                    cur.execute("select CourseName from courses where ECNO=?",(u,))
                    for e in cur:
                        teacher.append(e)
                    if len(teacher)==0:
                        text.insert(0.0,"No courses assigned to you yet!")
                    else:
                      for e in teacher:
                         for i in e:
                            stm =i,"\n"
                            for i in stm:
                                   text.insert(0.0,i)
                def log_out():
                    cur.execute("Update login_details set logout =? where Number =?",(ti,lo,))
                    con.commit()
                    main.destroy()
                    sign =SignIn()
                    sign.ini()
                    
                    
                
                l1 =Label(text ="Welcome",fg ="Blue",bg ="lightgreen", font ="Bold")
                l1.grid(row =0, column =2)
                
                l1 =Label(text =nm,fg ="Purple",bg ="lightgreen", font ="Bold")
                l1.grid(row =2, column =2)
                
                l1 =Label(text ="",fg ="Red",bg ="lightgreen")
                l1.grid(row =5, column =2)
                
                text =Text(main,width=25,height =13)
                text.configure(fg ="darkgreen")
                text.grid(row =3, column =3)
                  
                B1 = Button(text ="View Courses",fg ="white",bg ="Black", font ="Bold",command =courses)
                B1.configure(width =10)
                B1.grid(row =6, column =2)
                
                B2 =Button(text ="Log out", bg ="Yellow",font ="Bold", command =log_out)
                B2.configure(width =10)
                B2.grid(row =6, column =3)
                
                main.mainloop()
                
            else:
              tkinter.messagebox.showwarning("Alert","Incorrect credentials")
                    
            
        usertxt =StringVar()
        passtxt =StringVar()
        
        l1 =Label(text ="Username", bg ="lightgreen",font ="Bold")
        l1.grid(row =2, column =2)
        
        l2 =Label(text ="Password", bg ="lightgreen",font ="Bold")
        l2.grid(row =4, column =2)
        
        e1 =Entry(self.root,textvar =usertxt,font ="Bold")
        e1.grid(row =2, column =4)
        
        e2 =Entry(self.root,textvar =passtxt, show ="*",font ="Bold")
        e2.grid(row =4, column =4)
        
        menu  =Menu(self.root)
        self.root.config(menu =menu)
        
        submen =Menu(menu)
        menu.add_cascade(label ="File",menu =submen)
        submen.add_command(label ="Exit", command= ex)
        
        
        
        b =Button(text = "SIGN IN" ,fg ="white", bg ="black", font ="Bold", command =sig)
        b.configure(width = 10)
        b.grid(row =6, column = 2)
        
        l3 = Button(text = "Forgot Password ?",font = "Bold", bg ="yellow",command =forget)
        l3.grid(row =6, column =4)
        
        self.root.mainloop()

