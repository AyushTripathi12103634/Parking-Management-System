from tkinter import *
from tkinter import messagebox
from time import strftime
import random
import mysql.connector as m
mydb =m.connect(host='localhost',user ='root',password='root',database='parking_management_system')
mycursor =mydb.cursor()
def removeandadd(uid,tokennumber):
    a="insert into history_logs select * from parking_info where uid_no={}".format(int(uid))
    mycursor.execute(a)
    mydb.commit()
    b="delete from parking_info where uid_no={}".format(int(uid))
    mycursor.execute(b)
    mydb.commit()
    m=messagebox.showinfo("Thank you","Thank You!")
    w.destroy()
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
    v = v*5
    hh = abs(h1 - h2)
    mm = abs(m1 - m2)
    msg = hh*v +(mm/60)*v
    msg = msg + msg*(18/100)
    msg = ('%.2f' % msg)
    messagebox.showinfo("Price","Your total charger(inc gst) is:Rupees {}(₹ {})".format(msg,msg))
def abc():
    a=uident.get()
    b=tokennumberent.get()
    c=vehiclenumberent.get()
    mycursor.execute('select * from parking_info')
    f=0
    for y in mycursor:
        if ((int(a) in y) and (str(b) in y) and (str(c) in y)):
            timestring= (strftime('%H:%M:%S %p'))
            sql= "update parking_info set timeout=%s where uid_no=%s"
            mycursor.execute(sql,(timestring,int(a)))
            mydb.commit()
            f=1
    mydb.commit()
    if(f==0):
        m=messagebox.showerror("Error","No such details were found")
        w.destroy()
        return None
    sql1='select timein from parking_info where uid_no=%s and token_number=%s'
    val1=(a,b)
    mycursor.execute(sql1,val1)
    ti=mycursor.fetchall()
    sql2='select timeout from parking_info where uid_no=%s and token_number=%s'
    val2=(a,b)
    mycursor.execute(sql2,val2)
    to=mycursor.fetchall()
    sql3='select vehicle_type from parking_info where uid_no=%s and token_number=%s'
    val3=(a,b)
    mycursor.execute(sql3,val3)
    vehicle=mycursor.fetchall()
    price(ti,to,vehicle)
    removeandadd(a,b)
w=Tk()
#time label
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
    return string
lbl = Label(w, font = ('calibri', 40, 'bold'),foreground = 'Black')
lbl.grid( sticky="n",padx=50,pady=50)
time()
#for entries
l1=Label(w,text="Enter your Token number")
l2=Label(w,text="Enter your UID")
l4=Label(w,text="\n\n\n\n\n\n\n\n\n")
l5=Label(w,text="Enter your Vehicle Number")
l1.grid(row=5,column=0)
l4.grid(row=0,column=0)
l2.grid(row=3,column=0)
l5.grid(row=7,column=0)
#entries
uid=IntVar()
vehiclenumber=StringVar()
Tokennumber=IntVar()
uident=Entry(w,textvariable=uid, width=20, bd=5)
vehiclenumberent=Entry(w,textvariable=vehiclenumber, width=20, bd=5)
tokennumberent=Entry(w,textvariable=Tokennumber, width=20, bd=5)
uident.grid(row=3,column=1)
tokennumberent.grid(row=5,column=1)
vehiclenumberent.grid(row=7,column=1)
#parkloc.grid(row=3,column=3)
l=Label(w,text="\n\n")
l.grid(row=2,column=0)
l15=Label(w,text="\n\n")
l15.grid(row=4,column=0)
l16=Label(w,text="\n\n")
l16.grid(row=6,column=0)
l17=Label(w,text="\n\n")
l17.grid(row=8,column=0)
w.geometry('700x650')
b=Button(w,text="done",command=lambda:abc(), width=15, bd=5,bg='blue',font=('arial',10,'bold'),fg='black')
b1=Button(w,text="Charge Sheet",command=lambda:chargesheet(), width=15, bd=5,bg='blue',font=('arial',10,'bold'),fg='black')
b.grid(pady=15)
b1.grid(pady=5)
w.resizable(False,False)
w.mainloop()
