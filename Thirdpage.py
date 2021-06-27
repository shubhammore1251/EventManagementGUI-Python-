from tkinter import * 
from tkinter import messagebox 
window = Tk() 

filename = PhotoImage(file = "thirdpage.png")


mycanvas = Canvas(window, width=1366, height=768)
mycanvas.pack(fill="both", expand="True")
mycanvas.create_image(0,0, image = filename, anchor="nw")

mycanvas.create_text(420,80 ,text = "CUSTOMER NAME : "   , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(400,150,text = "CUSTOMER NUMBER :"  , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(430,220,text = "EVENT GENRE :"      , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(420,290,text = "HALL CAPACITY :"    , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(410,360,text = "SCHEDULE:-  FROM "  , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(755,360,text = "TO"                 , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(480,430,text = "TIME :"             , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(435,500,text = "NO. OF DAYS :"      , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(415,570,text = "TOTAL PACKAGE :"    , fill="white",font=("times new roman", 16,"bold"))
mycanvas.create_text(410,640,text = "ADVANCE AMOUNT :"   , fill="white",font=("times new roman", 16,"bold"))

mycanvas.create_text(1160,555,text = "I.E.S"              ,fill="white" , font=("times new roman", 16,"bold"))
mycanvas.create_text(1200,595,text = "ies@gmail.com"      ,fill="white" , font=("times new roman", 14,"bold"))
mycanvas.create_text(1200,635,text = "Powai, Mumbai"      ,fill="white" , font=("times new roman", 14,"bold"))
mycanvas.create_text(1220,675,text = "Mob.no: 84xxxxxxxx" ,fill="white" , font=("times new roman", 14,"bold"))


txt1= StringVar()
txt2= StringVar()
txt3= StringVar()
txt4= StringVar()
txt5= IntVar()
txt6= IntVar()
txt7= StringVar()
txt8= IntVar()
txt9= IntVar()
txt10=IntVar()



# TEXT FILED 
cname_entry =   Entry(window, textvariable=txt1, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 55,  width=410, height=35)
cnum_entry =    Entry(window, textvariable=txt2, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 125,  width=410, height=35) 
etype_entry =   Entry(window, textvariable=txt3, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 195, width=410, height=35)  
capa_entry =    Entry(window, textvariable=txt4, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 265, width=410, height=35)  
date1_entry = Entry(window, textvariable=txt5, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 335, width=150, height=35) 
date2_entry = Entry(window, textvariable=txt6, borderwidth="1", font=("Times New Roman", 16)).place(x = 810, y = 335, width=150, height=35) 
time_entry =    Entry(window, textvariable=txt7, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 405, width=410, height=35)
days_entry =    Entry(window, textvariable=txt8, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 475, width=410, height=35)
tp_entry =      Entry(window, textvariable=txt9, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 545, width=410, height=35)
adtp_entry =    Entry(window, textvariable=txt10, borderwidth="1", font=("Times New Roman", 16)).place(x = 550, y = 615, width=410, height=35)

 

def fetch():
    file = open("Customer Details.txt","r+")                     #//FILE READ CODE
    str = file.readlines()

    txt1.set(str[1] [14:])
    txt2.set(str[2] [16:])
    txt3.set(str[3] [12:])
    txt4.set(str[4] [14:])
    txt5.set(str[5] [16:27])
    txt6.set(str[5] [30:])
    txt7.set(str[6] [6:])
    txt8.set(str[7] [11:])
    txt9.set(str[8] [14:])
    txt10.set(str[9] [16:])
    file.close()
      

def pay():
    window1=Tk()
    file = open("Customer Details.txt","r+")                     #//FILE READ CODE
    str1 = file.readlines()
    
    adv = (str1[9] [16:] )
    mycanvas = Canvas(window1, width=200, height=300,bg = 'moccasin')
    mycanvas.pack(fill="both", expand="True")
    mycanvas.create_text(80,20 ,text = "Amount Payable " , fill="black",font=("times new roman", 16,"bold"))
    mycanvas.create_text(250,20 ,text = "Rs."  , fill="black",font=("times new roman", 16,"bold"))
    mycanvas.create_text(320,34 ,text = adv  , fill="black",font=("times new roman", 16,"bold"))
    mycanvas.create_text(320,40 ,text = "-------------------------------------------------------------------------------------------"  , fill="black",font=("times new roman", 16,"bold"))
    
    checkvar1 = IntVar()  
  
    checkvar2 = IntVar()  
  
    checkvar3 = IntVar()  

    def check1():

        t1=StringVar()
        t2=IntVar()
        t3=IntVar()
        t4=IntVar()
        t5=StringVar()

        
        cno=Entry(window1, textvariable=t1, borderwidth="1", font=("Times New Roman", 15)).place(x = 200, y = 220,  width=200, height=25)
        expm= Entry(window1, textvariable=t2, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 260,  width=60, height=25) 
        expy= Entry(window1, textvariable=t3, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 300, width=70, height=25)  
        cvvc=Entry(window1, textvariable=t4, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 340, width=60, height=25) 
        nom= Entry(window1, textvariable=t5, borderwidth="1", font=("Times New Roman", 12)).place(x = 120, y = 380, width=400, height=25) 

        mycanvas.create_text(80,230 ,text = "Enter Card Number: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(60,270 ,text = "Expiry Month: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(55,310 ,text = "Expiry Year: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(50,350 ,text = "CVV Code: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(57,390 ,text = "Name on Card: " , fill="black",font=("times new roman", 12,"bold"))

        def msg():
            messagebox.showinfo(title="Redirecting", message="We are redirecting you to your Bank's Payment window..........")
        
        b=Button(window1, text="PAY", fg='black',font=("Times New Roman", 12,"bold"),command=msg)
        b.place(x=57,y=420,width=150,height=30)  
    
     

    def check2():
        t1=StringVar()
        t2=IntVar()
        t3=IntVar()
        t4=IntVar()
        t5=StringVar()

        cno=Entry(window1, textvariable=t1, borderwidth="1", font=("Times New Roman", 15)).place(x = 200, y = 220,  width=200, height=25)
        expm= Entry(window1, textvariable=t2, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 260,  width=60, height=25) 
        expy= Entry(window1, textvariable=t3, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 300, width=70, height=25)  
        cvvc=Entry(window1, textvariable=t4, borderwidth="1", font=("Times New Roman", 14)).place(x = 120, y = 340, width=60, height=25) 
        nom= Entry(window1, textvariable=t5, borderwidth="1", font=("Times New Roman", 12)).place(x = 120, y = 380, width=400, height=25) 

        mycanvas.create_text(80,230 ,text = "Enter Card Number: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(60,270 ,text = "Expiry Month: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(55,310 ,text = "Expiry Year: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(50,350 ,text = "CVV Code: " , fill="black",font=("times new roman", 12,"bold"))
        mycanvas.create_text(57,390 ,text = "Name on Card: " , fill="black",font=("times new roman", 12,"bold"))

        def msg():
            messagebox.showinfo(title="Redirecting", message="We are redirecting you to your Bank's Payment window..........")
        
        b=Button(window1, text="PAY", fg='black',font=("Times New Roman", 12,"bold"),command=msg)
        b.place(x=57,y=420,width=150,height=30)  
    
       

    chkbtn1 = Checkbutton(window1, text = "Credit Card", variable = checkvar1, onvalue = 1, offvalue = 0, height = 2, width = 10, command=check1)  
  
    chkbtn2 = Checkbutton(window1, text = "Debit/Atm Card", variable = checkvar2, onvalue = 1, offvalue = 0, height = 2, width = 10,command=check2)  
  
    chkbtn3 = Checkbutton(window1, text = "Net Banking", variable = checkvar3, onvalue = 1, offvalue = 0, height = 2, width = 10)  
  
    chkbtn1.place(x=20,y=150)  
  
    chkbtn2.place(x=130,y=150,width=140)  
  
    chkbtn3.place(x=280,y=150)
    
    
    def paytm():
        window1.destroy()
        messagebox.showinfo(title="Opening Paytm", message="Wait Opening Paytm..........")
    
    def gpay():
        window1.destroy()
        messagebox.showinfo(title="Opening G Pay", message="Wait Opening Google Pay..........")
    
    def upi():
        window1.destroy()
        messagebox.showinfo(title="Opening BHIM", message="Wait Opening BHIM-UPI..........")

    bt1=Button(window1, text="Paytm", fg='navyblue',bg="lightblue",font=("Stencil", 18,"bold"),command=paytm)  #payTM BUTTON 
    bt1.place(x=20, y=70, width=100, height=40)

    bt2=Button(window1, text="G Pay", fg='darkgreen',bg="yellow", font=("Stencil", 18,"bold"),command=gpay)  #GPAY BUTTON
    bt2.place(x=150, y=70, width=100, height=40)

    bt3=Button(window1, text="U P I", fg='#515659',bg="#c98b26", font=("Stencil", 18,"bold"),command=upi)  #UPI BUTTON
    bt3.place(x=280, y=70, width=100, height=40)


    window1.resizable(0,0)
    window1.title('Payment Window')
    window1.geometry("600x600")
    window1.mainloop()
   
    

def cancel():
    txt1.set(" ")  
    txt2.set(" ") 
    txt3.set(" ") 
    txt4.set(" ") 
    txt5.set(0)
    txt6.set(0) 
    txt7.set(" ")
    txt8.set(0)
    txt9.set(0)
    txt10.set(0)
    messagebox.showinfo(title="Cancel Booking", message="Your Booking has Been Cancelled...\n\nIf any money is deducted from your bank account ,it will be refunded within 2-3 Business days!\n\nHope we see you back :)")

def back():
    window.destroy()
    import secondpage



btn1=Button(window, text="Pay Here", fg='black',font=("Times New Roman", 12,"bold"),command=pay)  #pay here  
btn1.place(x=1150, y=280, width=100, height=35)

btn2=Button(window, text="Cancel", fg='black', font=("Times New Roman", 12,"bold"),command=cancel)  #clear
btn2.place(x=1150, y=380, width=100, height=35)

btn3=Button(window, text="Back", fg='black', font=("Times New Roman", 12,"bold"),command=back)  #BACK
btn3.place(x=1150, y=480, width=100, height=35)


 
    
fetch()
window.resizable(0,0)
window.title(" MY EVENTS ")
window.geometry("1366x768")  
window.mainloop()



