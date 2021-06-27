from tkinter import *
from tkinter import messagebox 
window = Tk() 

filename = PhotoImage(file = "homepage.png")

mycanvas = Canvas(window, width=1366, height=768)
mycanvas.pack(fill="both", expand="True")
mycanvas.create_image(0,0, image = filename, anchor="nw")

def nextpage():
    window.destroy()
    import secondpage


btn1 = Button(window,borderwidth="2",text="Book Now", fg='Black', font=("Times New Roman", 17,"bold"),command=nextpage)
btn1.place(x = 420, y = 500,  width=180, height=45)

def mevent():
   messagebox.showinfo(title="My Events", message="YOU DONT HAVE ANY EVENTS !!!")

btn2 = Button(window, command=mevent, borderwidth="2",text="My Events", fg='Black', font=("Times New Roman", 17,"bold"))
btn2.place(x = 730, y = 500,  width=180, height=45)

window.resizable(0,0)
window.title(" HOMEPAGE ")
window.geometry("1366x768")  
window.mainloop()  