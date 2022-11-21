from tkinter import *
from tkinter import messagebox
import mysql.connector as m
import os
import time
from time import strftime
import random
mydb =m.connect(host='localhost',user ='root',password='root',database='parking_management_system')
mycursor =mydb.cursor(buffered=True)
def parkingticket():
    a=""
    for i in range(6):
        a+=str(random.randint(0,9))
    mycursor.execute('select * from parking_info')
    for y in mycursor:
        while a in y:
            a=""
            for i in range(6):
                a+=str(random.randint(0,9))
    return a
parkingticket=parkingticket()
def parkloc():
    d={1: 'a:101', 2: 'a:102', 3: 'a:103', 4: 'a:104', 5: 'b:105', 6: 'b:106', 7: 'a:107', 8: 'a:108', 9: 'b:109', 10: 'a:110', 11: 'b:111', 12: 'b:112', 13: 'a:113', 14: 'b:114', 15: 'a:115', 16: 'a:116', 17: 'b:117', 18: 'a:118', 19: 'a:119', 20: 'b:120', 21: 'b:121', 22: 'a:122', 23: 'b:123', 24: 'b:124', 25: 'a:125', 26: 'a:126', 27: 'b:127', 28: 'b:128', 29: 'a:129', 30: 'a:130', 31: 'a:131', 32: 'a:132', 33: 'a:133', 34: 'b:134', 35: 'b:135', 36: 'b:136', 37: 'b:137', 38: 'b:138', 39: 'b:139', 40: 'a:140', 41: 'b:141', 42: 'b:142', 43: 'a:143', 44: 'a:144', 45: 'a:145', 46: 'a:146', 47: 'a:147', 48: 'a:148', 49: 'b:149', 50: 'a:150', 51: 'a:151', 52: 'a:152', 53: 'a:153', 54: 'b:154', 55: 'b:155', 56: 'b:156', 57: 'b:157', 58: 'a:158', 59: 'a:159', 60: 'a:160', 61: 'a:161', 62: 'b:162', 63: 'b:163', 64: 'b:164', 65: 'b:165', 66: 'a:166', 67: 'a:167', 68: 'b:168', 69: 'b:169', 70: 'a:170', 71: 'b:171', 72: 'a:172', 73: 'b:173', 74: 'a:174', 75: 'a:175', 76: 'a:176', 77: 'a:177', 78: 'a:178', 79: 'b:179', 80: 'b:180', 81: 'a:181', 82: 'a:182', 83: 'b:183', 84: 'a:184', 85: 'b:185', 86: 'b:186', 87: 'a:187', 88: 'b:188', 89: 'a:189', 90: 'b:190', 91: 'b:191', 92: 'b:192', 93: 'b:193', 94: 'a:194', 95: 'a:195', 96: 'a:196', 97: 'a:197', 98: 'b:198', 99: 'b:199', 100: 'b:200'}
    x= d[random.randint(1,100)]
    mycursor.execute('select * from parking_info')
    for y in mycursor:
        while x in y:
            x= d[random.randint(1,100)]
    return x
parkloc=parkloc()
def mainwindow():
    def signup():
        messagebox.showinfo("Redirecting","Redirecting to the sign up page(takes 3 seconds)...")
        w.destroy()
        time.sleep(3)
        w1=Tk()
        def change(w1):
            w1.destroy()
            w1=Tk()
            w1.geometry('500x500')
            w1.resizable(False,False)
            l2=Label(w1,text="Enter your Name").place(x=50,y=50)
            l3=Label(w1,text="Enter your UID").place(x=50,y=100)
            l4=Label(w1,text="Enter your Phone Number").place(x=50,y=150)
            l5=Label(w1,text="Enter your Vehicle Number").place(x=50,y=200)
            l6=Label(w1,text="Enter your Vehicle Type 2/3/4 wheeler").place(x=50,y=250)
            t1=Text(w1,height=10,width=50)
            t1.configure(state="disabled")
            t1.place(x=50,y=300)
            def insert():
                t1.configure(state="normal")
                t1.insert(END,"Your Name: {}\n\nYour UID: {}\n\nYour Phone Number: {}\n\nYour Vehicle Number: {}\n\nYour Vehicle Type: {}".format(name.get(),int(uid.get()),int(pn.get()),vn.get(),vt.get()))
                t1.configure(state="disabled")
                def confirm():                    
                    mycursor.execute("insert into login values(%s,%s,%s,%s,%s)",(name.get(),int(uid.get()),int(pn.get()),vn.get(),vt.get(),))
                    mydb.commit()
                    messagebox.showinfo("Success","You have successfully signed up in LPU Database!")
                    w1.destroy()
                    mainwindow()
                b5=Button(w1,text="Confirm",command=lambda:confirm(),bd=5).place(x=360,y=245)
                b6=Button(w1,text="Change entries?",command=lambda:change(w1)).place(x=360,y=220)
            b4=Button(w1,text="Submit",command=lambda:insert()).place(x=360,y=245)
            name=StringVar()
            uid=StringVar()
            pn=StringVar()
            vn=StringVar()
            vt=StringVar()
            ne=Entry(w1,textvariable=name).place(x=210,y=50)
            ue=Entry(w1,textvariable=uid).place(x=210,y=100)
            pne=Entry(w1,textvariable=pn).place(x=210,y=150)
            vne=Entry(w1,textvariable=vn).place(x=210,y=200)
            vte=Entry(w1,textvariable=vt).place(x=210,y=250)
        w1.geometry('500x500')
        w1.resizable(False,False)
        l2=Label(w1,text="Enter your Name").place(x=50,y=50)
        l3=Label(w1,text="Enter your UID").place(x=50,y=100)
        l4=Label(w1,text="Enter your Phone Number").place(x=50,y=150)
        l5=Label(w1,text="Enter your Vehicle Number").place(x=50,y=200)
        l6=Label(w1,text="Enter your Vehicle Type 2/3/4 wheeler").place(x=50,y=250)
        t1=Text(w1,height=10,width=50)
        t1.configure(state="disabled")
        t1.place(x=50,y=300)
        def insert():
            t1.configure(state="normal")
            t1.insert(END,"Your Name: {}\n\nYour UID: {}\n\nYour Phone Number: {}\n\nYour Vehicle Number: {}\n\nYour Vehicle Type: {}".format(name.get(),int(uid.get()),int(pn.get()),vn.get(),vt.get()))
            t1.configure(state="disabled")
            def confirm():                    
                mycursor.execute("insert into login values(%s,%s,%s,%s,%s)",(name.get(),int(uid.get()),int(pn.get()),vn.get(),vt.get(),))
                mydb.commit()
                messagebox.showinfo("Success","You have successfully signed up in LPU Database!")
                w1.destroy()
                mainwindow()
            b5=Button(w1,text="Confirm",command=lambda:confirm(),bd=5).place(x=360,y=245)
            b6=Button(w1,text="Change entries?",command=lambda:change(w1)).place(x=360,y=220)
        b4=Button(w1,text="Submit",command=lambda:insert()).place(x=360,y=245)
        name=StringVar()
        uid=StringVar()
        pn=StringVar()
        vn=StringVar()
        vt=StringVar()
        ne=Entry(w1,textvariable=name).place(x=210,y=50)
        ue=Entry(w1,textvariable=uid).place(x=210,y=100)
        pne=Entry(w1,textvariable=pn).place(x=210,y=150)
        vne=Entry(w1,textvariable=vn).place(x=210,y=200)
        vte=Entry(w1,textvariable=vt).place(x=210,y=250)
    def login():
        messagebox.showinfo("Redirecting","Redirecting you to login page(takes 3 seconds)...")
        w.destroy()
        time.sleep(3)
        w1=Tk()
        def parking():
            w2=Tk()
            def parkin(a):
                mycursor.execute("select name from login where uid_no = {}".format(a))
                name=str(mycursor.fetchall())
                mycursor.execute("select ph_no from login where uid_no = %s",(a,))
                ph=str(mycursor.fetchall())
                mycursor.execute("select vehicle_number from login where uid_no = %s",(a,))
                vn=str(mycursor.fetchall())
                mycursor.execute("select vehicle_type from login where uid_no = %s",(a,))
                vt=str(mycursor.fetchall())
                name=name[3:len(name)-4]
                ph=ph[11:len(ph)-5]
                vn=vn[3:len(vn)-4]
                vt=vt[3:len(vt)-4]
                timestring= (strftime('%H:%M:%S %p'))
                sql = "INSERT INTO parking_info (name, uid_no, ph_no, timein, park_loc, token_number, vehicle_number, vehicle_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (name,int(a),int(ph),timestring,parkloc,parkingticket,vn,vt)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("Success","Your token number is: {} and parking location is: {}".format(parkingticket,parkloc))
                w2.destroy()
                mainwindow()
            def unpark(a):
                def price(t1,t2,vehicle):
                    h1=t1[0]
                    h2=t2[0]
                    m1=t1[0]
                    m2=t2[0]
                    v=vehicle[0][0][0]
                    h1=str(h1)
                    h2=str(h2)
                    m1=str(m1)
                    m2=str(m2)
                    v=int(v)
                    h1=h1[2:4]
                    h2=h2[2:4]
                    m1=m1[5:7]
                    m2=m2[5:7]
                    h1=int(h1)
                    h2=int(h2)
                    m1=int(m1)
                    m2=int(m2)
                    v = v*2.5
                    hh = abs(h1 - h2)
                    mm = abs(m1 - m2)
                    msg = hh*v +(mm/60)*v
                    msg = msg + msg*(18/100)
                    msg = ('%.2f' % msg)
                    messagebox.showinfo("Price","Your total charger(inc gst) is:Rupees {}(₹ {})".format(msg,msg))
                def removeandadd(x):
                    a="insert into history_logs select * from parking_info where uid_no=%s"
                    val=(int(x),)
                    mycursor.execute(a,val)
                    mydb.commit()
                    b="delete from parking_info where uid_no=%s"
                    mycursor.execute(b,val)
                    mydb.commit()
                    m=messagebox.showinfo("Thank you","Thank You!")
                    w2.destroy()
                timestring= (strftime('%H:%M:%S %p'))
                mycursor.execute("update parking_info set timeout =%s where uid_no =%s",(timestring,int(a),))
                mydb.commit()
                sql1='select timein from parking_info where uid_no=%s'
                val1=(int(a),)
                mycursor.execute(sql1,val1)
                ti=mycursor.fetchall()
                sql2='select timeout from parking_info where uid_no=%s'
                val2=(int(a),)
                mycursor.execute(sql2,val2)
                to=mycursor.fetchall()
                sql3='select vehicle_type from parking_info where uid_no=%s'
                val3=(int(a),)
                mycursor.execute(sql3,val3)
                vehicle=mycursor.fetchall()
                price(ti,to,vehicle)     
                removeandadd(a)           
            b1=Button(w2,text="Park in",command=lambda:parkin(uid.get())).place(x=50,y=50)
            b2=Button(w2,text="Unpark",command=lambda:unpark(uid.get())).place(x=50,y=100)
            w2.geometry('150x150')
            w2.resizable(False,False)
        def validate():
            mycursor.execute("select * from login")
            y=mycursor.fetchall()
            flag=0
            for z in y:
                if ((name.get() in z) and (uid.get() in z)):
                    x=uid.get()
                    messagebox.showinfo("Success","Verification Successful! Redirecting to main page(takes 3 seconds)")
                    w1.destroy()
                    time.sleep(3)
                    parking()
                    flag=1
            if(flag==0):
                time.sleep(3)
                messagebox.showerror("Error","Enter correct details")
        name=StringVar()
        uid=IntVar()
        l1=Label(w1,text="Enter Name").place(x=50,y=50)
        l2=Label(w1,text="Enter UID").place(x=50,y=100)
        ne=Entry(w1,textvariable=name).place(x=200,y=50)
        ue=Entry(w1,textvariable=uid).place(x=200,y=100)
        b1=Button(w1,text="Submit",command=lambda:validate()).place(x=200,y=150)
        w1.geometry('400x250')
        w1.resizable(False,False)
    def parkingforguest():
        messagebox.showinfo("Redirecting","Redirecting you to parking for guests page(takes 3 seconds)...")
        time.sleep(3)
        os.startfile(r'Parking.py')
    w=Tk()
    l1=Label(w,text="Parking Management System",font=("arial",25,"bold"),bg="pink",fg="orange").place(x=50,y=20)
    t=Text(w,height=8,width=55)
    t.insert(END,"Select Login if you are an existing staff\n\n\nSelect Sign Up if you are a new staff\n\n\nSelect Parking For Guest if you are a guest")
    t.configure(state="disabled")
    t.place(x=50,y=250)
    i=PhotoImage(file=r'lpulogo.png')
    l2=Label(w,image=i).place(x=206,y=70)
    b1=Button(w,text="Sign Up",font=("arial",10,"bold"), width=15, bd=5,bg='blue',fg='black',command=lambda:signup()).place(x=50,y=100)
    b2=Button(w,text="Login",font=("arial",10,"bold"), width=15, bd=5,bg='blue',fg='black',command=lambda:login()).place(x=50,y=150)
    b3=Button(w,text="Parking For Guest",font=("arial",10,"bold"), width=15, bd=5,bg='blue',fg='black',command=lambda:parkingforguest()).place(x=50,y=200)
    w.geometry('550x400')
    w.resizable(False,False)
    w.mainloop()
mainwindow()
