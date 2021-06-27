from tkinter import *
from tkinter.ttk import Combobox
from datetime import date
from tkinter import messagebox 
import sqlite3 

window=Tk()

filename = PhotoImage(file = "2pg.png")

mycanvas = Canvas ( window,width = 1366, height = 768)

mycanvas.pack(fill = "both", expand = True)

mycanvas.create_image( 0, 0,image=filename ,anchor = "nw")

def nextpage1():
   window.destroy()
   import Thirdpage

mycanvas.create_text(680,50 ,text = "IMPERIAL  EVENT  SOLUTIONS"   ,fill="white",font=("times new roman", 30,"bold"))
mycanvas.create_text(330,160,text = "Name"                       ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(750,160,text = "Number"                     ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(325,245,text = "Event Genre"                ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(750,245,text = "Hall Size"                  ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(330,335,text = "Book Dates"                 ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(750,335,text = "To"                         ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(350,425,text = "Time"                       ,fill="white",font=("times new roman", 17,"bold"))
mycanvas.create_text(320,605,text = "Total \nPayment in (Rs.)"   ,fill="white",font=("times new roman", 15,"bold"))
mycanvas.create_text(730,605,text = "Advance \nPayment in (Rs.)" ,fill="white",font=("times new roman", 15,"bold"))
mycanvas.create_text(465,360,text = "yyyy"                       ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(535,360,text = "mm"                         ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(590,360,text = "dd"                         ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(875,360,text = "yyyy"                       ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(945,360,text = "mm"                         ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(1000,360,text = "dd"                        ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(1100,605,text = "50% of Total"              ,fill="white",font=("times new roman", 12,"bold"))
mycanvas.create_text(750,415,text = "No.of Days"              ,fill="white",font=("times new roman", 18,"bold"))


data1=("Wedding", "Engagement", "Birthday", "Anniversary", "Group Disco Party")
cb1=Combobox(window, values=data1, font=("times new roman", 13))
cb1.place(x=420, y=225, width=200, height=35)
cb1.set("Select")

data2=("Small (upto 100 guest)", "Medium (upto 250 guest)", "Large (upto 500 guest)", "Grand (upto 1000 guest)")
cb2=Combobox(window, values=data2, font=("times new roman", 13))
cb2.place(x=830, y=225, width=200, height=35)
cb2.set("Select")

#v0=IntVar()
#v0.set(0)

txt1=IntVar()     #y1
txt2=IntVar()     #m1
txt3=IntVar()     #dt1
txt4=IntVar()     #y2
txt5=IntVar()     #m2
txt6=IntVar()     #dt2
txt7=StringVar()  #Startime
txt8=IntVar()     #Check days
txt9=StringVar()  #check availability
txt10=IntVar()    #total payment
txt11=IntVar()    #advacnce payment
txt12=StringVar() #name
txt13=StringVar() #number



    

        

txtfld1=Entry(window,textvariable=txt1, borderwidth="1", font=("Times New Roman", 15)) #date1yyyy
txtfld1.place(x=420, y=310, width=85, height=35)

txtfld2=Entry(window,textvariable=txt2, borderwidth="1", font=("Times New Roman", 15)) #date1mm
txtfld2.place(x=510, y=310, width=50, height=35)

txtfld3=Entry(window,textvariable=txt3, borderwidth="1", font=("Times New Roman", 15)) #date1dd
txtfld3.place(x=565, y=310, width=50, height=35)

txtfld4=Entry(window,textvariable=txt4, borderwidth="1", font=("Times New Roman", 15)) #date2yyyy
txtfld4.place(x=830, y=310, width=85, height=35)

txtfld5=Entry(window,textvariable=txt5, borderwidth="1", font=("Times New Roman", 15)) #date2mm
txtfld5.place(x=920, y=310, width=50, height=35)

txtfld6=Entry(window,textvariable=txt6, borderwidth="1", font=("Times New Roman", 15)) #date2dd
txtfld6.place(x=975, y=310, width=50, height=35)

txtfld7=Entry(window,textvariable=txt7, borderwidth="1", font=("Times New Roman", 15)) #start-time
txtfld7.place(x=420, y=400, width=200, height=35)

txtfld8=Entry(window,textvariable=txt8, borderwidth="1", font=("Times New Roman", 15)) #check-days
txtfld8.place(x=830, y=400, width=200, height=35)

txtfld9=Entry(window,textvariable=txt9, borderwidth="1", font=("Times New Roman", 15)) #availability
txtfld9.place(x=420, y=495, width=200, height=35)

txtfld10=Entry(window,textvariable=txt10, borderwidth="1", font=("Times New Roman", 15)) #total-payment
txtfld10.place(x=420, y=590, width=200, height=35)

txtfld11=Entry(window,textvariable=txt11, borderwidth="1", font=("Times New Roman", 15)) #advance-payment
txtfld11.place(x=830, y=590, width=200, height=35)

txtfld12=Entry(window,textvariable=txt12, borderwidth="1", font=("Times New Roman", 15)) #name
txtfld12.place(x=420, y=135, width=200, height=35)

txtfld13=Entry(window,textvariable=txt13, borderwidth="1", font=("Times New Roman", 15)) #number
txtfld13.place(x=830, y=135, width=200, height=35)


def aval():
    txt9.set(" Available !!")


def total_pay(): 
    caldays()
    length=len(txt13.get())
    value1 = cb1.get()
    value2 = cb2.get()
    day = txt8.get()
    ws=100000
    wm=200000
    wl=300000
    wg=500000
    if(value1=="Wedding" and value2=="Small (upto 100 guest)" and int(day==1)):
       txt10.set(ws)
    elif(value1=="Wedding" and value2=="Medium (upto 250 guest)" and int(day==1)):
       txt10.set(wm)
    elif(value1=="Wedding" and value2=="Large (upto 500 guest)" and int(day==1)):
       txt10.set(wl)
    elif(value1=="Wedding" and value2=="Grand (upto 1000 guest)" and int(day==1)):
        txt10.set(wg)
    elif(value1=="Wedding" and value2=="Small (upto 100 guest)" and int(day>1)):
        txt10.set(ws*day)
    elif(value1=="Wedding" and value2=="Medium (upto 250 guest)" and int(day>1)):
        txt10.set(wm*day)
    elif(value1=="Wedding" and value2=="Large (upto 500 guest)" and int(day>1)):
        txt10.set(wl*day)
    elif(value1=="Wedding" and value2=="Grand (upto 1000 guest)" and int(day>1)):
        txt10.set(wg*day)

    es=30000
    em=45000
    el=50000
    eg=80000
    if(value1=="Engagement" and value2=="Small (upto 100 guest)" and int(day==1)):
       txt10.set(es)
    elif(value1=="Engagement" and value2=="Medium (upto 250 guest)" and int(day==1)):
       txt10.set(em)
    elif(value1=="Engagement" and value2=="Large (upto 500 guest)" and int(day==1)):
       txt10.set(el)
    elif(value1=="Engagement" and value2=="Grand (upto 1000 guest)" and int(day==1)):
        txt10.set(eg)
    elif(value1=="Engagement" and value2=="Small (upto 100 guest)" and int(day>1)):
        txt10.set(es*day)
    elif(value1=="Engagement" and value2=="Medium (upto 250 guest)" and int(day>1)):
        txt10.set(em*day)
    elif(value1=="Engagement" and value2=="Large (upto 500 guest)" and int(day>1)):
        txt10.set(el*day)
    elif(value1=="Engagement" and value2=="Grand (upto 1000 guest)" and int(day>1)):
        txt10.set(eg*day)


    bs=10000
    bm=20000
    bl=35000
    bg=40000
    if(value1=="Birthday" and value2=="Small (upto 100 guest)" and int(day==1)):
       txt10.set(bs)
    elif(value1=="Birthday" and value2=="Medium (upto 250 guest)" and int(day==1)):
       txt10.set(bm)
    elif(value1=="Birthday" and value2=="Large (upto 500 guest)" and int(day==1)):
       txt10.set(bl)
    elif(value1=="Birthday" and value2=="Grand (upto 1000 guest)" and int(day==1)):
       txt10.set(bg)
    elif(value1=="Birthday" and value2=="Small (upto 100 guest)" and int(day>1)):
       txt10.set(bs*day)
    elif(value1=="Birthday" and value2=="Medium (upto 250 guest)" and int(day>1)):
       txt10.set(bm*day)
    elif(value1=="Birthday" and value2=="Large (upto 500 guest)" and int(day>1)):
       txt10.set(bl*day)
    elif(value1=="Birthday" and value2=="Grand (upto 1000 guest)" and int(day>1)):
       txt10.set(bg*day)

    avs=40000
    am=60000
    al=75000
    ag=80000
    if(value1=="Anniversary" and value2=="Small (upto 100 guest)" and int(day==1)):
       txt10.set(avs)
    elif(value1=="Anniversary" and value2=="Medium (upto 250 guest)" and int(day==1)):
       txt10.set(am)
    elif(value1=="Anniversary" and value2=="Large (upto 500 guest)" and int(day==1)):
       txt10.set(al)
    elif(value1=="Anniversary" and value2=="Grand (upto 1000 guest)" and int(day==1)):
        txt10.set(ag)
    elif(value1=="Anniversary" and value2=="Small (upto 100 guest)" and int(day>1)):
        txt10.set(avs*day)
    elif(value1=="Anniversary" and value2=="Medium (upto 250 guest)" and int(day>1)):
        txt10.set(am*day)
    elif(value1=="Anniversary" and value2=="Large (upto 500 guest)" and int(day>1)):
        txt10.set(al*day)
    elif(value1=="Anniversary" and value2=="Grand (upto 1000 guest)" and int(day>1)):
        txt10.set(ag*day)

    ps=40000
    pm=60000
    pl=75000
    pg=80000
    if(value1=="Group Disco Party" and value2=="Small (upto 100 guest)" and int(day==1)):
       txt10.set(ps)
    elif(value1=="Group Disco Party" and value2=="Medium (upto 250 guest)" and int(day==1)):
       txt10.set(pm)
    elif(value1=="Group Disco Party" and value2=="Large (upto 500 guest)" and int(day==1)):
       txt10.set(pl)
    elif(value1=="Group Disco Party" and value2=="Grand (upto 1000 guest)" and int(day==1)):
        txt10.set(pg)
    elif(value1=="Group Disco Party" and value2=="Small (upto 100 guest)" and int(day>1)):
        txt10.set(ps*day)
    elif(value1=="Group Disco Party" and value2=="Medium (upto 250 guest)" and int(day>1)):
        txt10.set(pm*day)
    elif(value1=="Group Disco Party" and value2=="Large (upto 500 guest)" and int(day>1)):
        txt10.set(pl*day)
    elif(value1=="Group Disco Party" and value2=="Grand (upto 1000 guest)" and int(day>1)):
        txt10.set(pg*day)

    if(value1=="Select" and value2=="Select"):
        messagebox.showinfo(title="Event Select Error", message="Please Select any Event")
    
    elif(length>10 or length<10):
        messagebox.showinfo(title="Number Error", message="Phone number Should be of 10 Digits")
    
    else:
      advpay()
    
def caldays():
    def numOfDays(date1, date2):
        return (date2-date1).days

    date1 = date(txt1.get(),txt2.get(),txt3.get())
    date2 = date(txt4.get(),txt5.get(),txt6.get())
    days=numOfDays(date1, date2)
    txt8.set(days+1)
    # total_pay()

def advpay():
    amt=txt10.get()
    avp=amt*0.5
    txt11.set(avp)
    am = str(avp)
    messagebox.showinfo(title="Advance Payment", message="You have to Pay a sum of RS. "+am+" in advance ")
    
def booknow():
    messagebox.showinfo(title="Booked", message="Your Selected Event Has Been Booked !! \n\nKindly Check Your Booking Details in My Events !! ")
    
    #------FILE WRITER PART-----#
    cname=txt12.get()
    cnum=txt13.get()               
    etype=cb1.get()
    hcapa=cb2.get()
    yy1=txt1.get()
    mm1=txt2.get()
    dt1=txt3.get()
    yy2=txt4.get()
    mm2=txt5.get()
    dt2=txt6.get()
    tim=txt7.get()
    dys=txt8.get()
    tpack=txt10.get()
    advp=txt11.get()
    

    file = open("Customer Details.txt","w+")
    file.write("*****IMPERIAL EVENT SOLUTIONS*****")
    file.write("\nCustomer Name: "+cname)
    file.write("\nCustomer Number: "+cnum)
    file.write("\nEvent Genre: "+etype)
    file.write("\nHall Capacity: "+hcapa)
    file.write("\nSchedule:- From: "+str(yy1)+"/"+str(mm1)+"/"+str(dt1)+" to "+str(yy2)+"/"+str(mm2)+"/"+str(dt2))
    file.write("\nTime: "+tim)
    file.write("\nNo.Of Days: "+str(dys))
    file.write("\nTotal Package: "+str(tpack))
    file.write("\nAdvance Amount: "+str(advp))
    
    
    file.close()
    print(cname,cnum,etype,hcapa,yy1,mm1,dt1,yy2,mm2,dt2,tim,dys,tpack,advp)  
    
    #---------------------------------------------------------------#
    
    DATEco= str(yy1)+"/"+str(mm1)+"/"+str(dt1)
    DATEco2= str(yy2)+"/"+str(mm2)+"/"+str(dt2)
    
    #------DATABASE ADDITION PART--------#
    db = sqlite3.connect('IES_EVENTSDB.db')  
    cursor = db.cursor()

    # cursor.execute( """CREATE TABLE iesdb1(
    #              CUSTOMER_NAME text,
    #              CUSTOMER_NO txt,
    #              EVENT_GENRE text, 
    #              HALL_CAPACITY text,
    #              START_DATE text,
    #              END_DATE text,
    #              TIME text,
    #              NO_OF_DAYS text,
    #              TOTAL_PACKAGE text,
    #              ADVANCE_AMOUNT text
    # )""")

    #INSERT INTO TABLE
    db.execute("INSERT INTO iesdb1 (CUSTOMER_NAME,CUSTOMER_NO,EVENT_GENRE,HALL_CAPACITY,START_DATE,END_DATE,TIME,NO_OF_DAYS,TOTAL_PACKAGE,ADVANCE_AMOUNT) ""VALUES (:cnam, :cno, :etype, :hcapa, :d1, :d2, :tm, :nod, :tp, :adp)",
           {
                 'cnam': txt12.get(),
                 'cno': txt13.get(),
                 'etype': cb1.get(),
                 'hcapa': cb2.get(),
                 'd1': DATEco,
                 'd2': DATEco2,
                 'nod': txt8.get(),
                 'tm': txt7.get(),
                 'tp': txt10.get(),
                 'adp': txt11.get()
           })
    cursor = db.execute("SELECT * FROM iesdb1")
    print(cursor.fetchall())

    db.commit()  
    db.close() 
    







# btn1=Button(window, text="Check Total Amount", fg='black',font=("Times New Roman", 12,"bold"),command=total_pay)  #CHECK DAYS
# btn1.place(x=690, y=400, width=100, height=35)

btn2=Button(window, text="Availability", fg='black', font=("Times New Roman", 12,"bold"), command=aval)  #AVAILABILITY
btn2.place(x=285, y=495, width=100, height=35) 

btn3=Button(window, text="Book now ", fg='black', font=("Times New Roman", 12,"bold"),command=booknow)  #BOOK NOW
btn3.place(x=650, y=670, width=100, height=35)
 
btn4=Button(window, text="Check Your Total Payment", fg='black', font=("Times New Roman", 12,"bold"),command=total_pay)  #Total Pay
btn4.place(x=350, y=670, width=250, height=35)

btn5=Button(window, text="My Events", fg='black', font=("Times New Roman", 12,"bold"), command=nextpage1)  #MY EVENTS
btn5.place(x=850, y=670, width=100, height=35)



window.resizable(0,0)
window.title('Imperial Event Solutions')
window.geometry("1366x768")
window.mainloop()