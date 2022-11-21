from tkinter import *
from tkinter import messagebox
from time import strftime
import random
import mysql.connector as m
mydb =m.connect(host='localhost',user ='root',password='root',database='parking_management_system')
mycursor =mydb.cursor()
def chargesheet():
    m=messagebox.showinfo("Charge Sheet","The price for every hour is dependent on vehicle.\n\nPrice for parking a two wheeler for 1 hour is: Rupees 10(₹10).\n\nPrice for parking a three wheeler for 1 hour is: Rupees 15(₹15).\n\nPrice for parking a four wheeler for 1 hour is: Rupees 20(₹20).")       
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
def abc():
    a=numberent.get()
    b=uident.get()
    c=nameent.get()
    f=0
    if(len(a)!=10):
        m=messagebox.showerror('ERROR',"The length of phone number is supposed to be 10!!!")
        f=1
    if(b.isdigit()==False):
        m=messagebox.showerror('ERROR',"The uid can't have alphabets!!!")
        f=1
    if(a.isdigit()==False):
        m=messagebox.showerror('ERROR',"The phone number can't have alphabets!!!")
        f=1
    if(f==1):
        w.destroy()
        return None
    timestring= (strftime('%H:%M:%S %p'))
    m=messagebox.showinfo("Done!","Your Parking ticket is: {} and the location for parking is: {}".format(parkingticket,parkloc))
    sql = "INSERT INTO parking_info (name, uid_no, ph_no, timein, park_loc, token_number, vehicle_number, vehicle_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (nameent.get(),uident.get(),numberent.get(),timestring,parkloc,parkingticket,vehiclenumberent.get(),vehicletypeent.get())
    mycursor.execute(sql, val)
    mydb.commit()
    w.destroy()
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
l1=Label(w,text="Enter your name")
l2=Label(w,text="Enter your UID")
l3=Label(w,text="Enter your Phone Number")
l4=Label(w,text="\n\n\n\n\n\n\n\n\n")
l5=Label(w,text="Enter your Vehicle Number")
l6=Label(w,text="Enter the Vehicle Type(2 wheeler, 3 wheeler or 4 wheeler)")
l7=Label(w,text="                                                              ")
l4.grid(row=0,column=0)
l1.grid(row=1,column=0)
l2.grid(row=3,column=0)
l3.grid(row=5,column=0)
l5.grid(row=7,column=0)
l6.grid(row=9,column=0)
l7.grid(row=3,column=2)
#entries
name=StringVar()
uid=IntVar()
number=IntVar()
vehiclenumber=StringVar()
vehicletype=StringVar()
nameent=Entry(w,textvariable=name, width=20, bd=5)
uident=Entry(w,textvariable=uid, width=20, bd=5)
vehiclenumberent=Entry(w,textvariable=vehiclenumber, width=20, bd=5)
vehicletypeent=Entry(w,textvariable=vehicletype, width=20, bd=5)
numberent=Entry(w,textvariable=number, width=20, bd=5)
nameent.grid(row=1,column=1)
uident.grid(row=3,column=1)
numberent.grid(row=5,column=1)
vehiclenumberent.grid(row=7,column=1)
vehicletypeent.grid(row=9,column=1)
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
