from Tkinter import *
import tkMessageBox
import ttk
from PIL import ImageTk, Image
import os

def rbsel():
   selection = "You selected the E-Newspaper Site url name:- " + str(var.get())
   label.config(text = selection)
def aboutus():
    tkMessageBox.showinfo("----------About Us----------", "This software is developed by ABHISHEK KUMAR from PONDICHERRY UNIVERSITY MCA Computer Science Department under the guidance of Dr. K.S. KUPPUSAMMY Assistant Professor Of Computer Science Department.\nPurpose of the development of this sofware is to extract the genuine text content by removing unwanted content like adds and other mislanious items.\n After this text content is converted into audio. \n\nSo, basically this project is for VISUALLY IMPAIRED PERSON")
def hp():
    tkMessageBox.showinfo("--------------------Help--------------------", "1. Select the e-Newspaper Website url\n2. Coinfrm that you have selected correct url\n3. After that press button named VIEW RESULT\n4. Then your default system browser is trigger and result are displayed\n5. And the result is converted into speach.\n6. Thanks")
def browser():
   tkMessageBox.showinfo("----------Supported Browser List----------", "1. Internet Explorer \n2. Google Chrome \n3. Mozila Firefox \n4. Safari")

root = Tk()
root.state('zoomed')
root.title("E-Newspaper Web Scrapping System")
root.configure(background = '#e1d8b9')

#------------Frame Section-----------------
topframe = Frame(root, highlightbackground="black", highlightthickness=5, width=300, height=100)
topframe.configure(background = '#e1d8b9')
topframe.pack(side=TOP)

leftframe = Frame(root, highlightbackground="darkgreen", highlightthickness=5, width=700, height=500)
leftframe.configure(background = '#e1d8b9')
leftframe.pack(side=LEFT)

rightframe = Frame(root, highlightbackground="darkgreen", highlightthickness=5, width=900, height=900)
rightframe.configure(background = '#e1d8b9')
rightframe.pack(side=RIGHT)

bottomframe = Frame(root, width=800, height=300)
bottomframe.configure(background = '#e1d8b9')
bottomframe.pack(side=BOTTOM)

#------------DropDownMenu-------------------
menu=Menu(root)
root.config(menu=menu)
submenu = Menu(menu)
menu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Help....", command=hp)
submenu.add_separator()                                     
submenu.add_command(label="Exit....")
submenu = Menu(menu)
menu.add_cascade(label="About", menu=submenu)
submenu.add_command(label="Supported Browser", command=browser)
submenu.add_command(label="About Us", command=aboutus)

#------------Image-------------------------
thelabel6 = Label(topframe, compound=TOP)
thelabel6.configure(background = '#e1d8b9')
thelabel6.pack(anchor=N)
img = ImageTk.PhotoImage(Image.open("C:\Users\ABHISHEK\Desktop\image\download.jpg"))
panel = Label(topframe, image = img, compound=LEFT)
panel.configure(background = '#e1d8b9')
panel.pack(side = "left", fill = "both", expand = "1")

#------------Label--------------------------
extralabel = Label(topframe, compound=TOP)
extralabel.configure(background = '#e1d8b9')
extralabel.pack(anchor=N)
titlelabel = Label(topframe, text="WELCOME TO THE e-NEWSPAPER WEB SCRAPPING SYSTEM", font=('Rockwell Extra Bold', 23, 'bold','underline'), fg="dark blue",compound=TOP)
titlelabel.configure(background = '#e1d8b9')
titlelabel.pack(anchor=N)
titlelabel1 = Label(topframe, text="Life is really simple, but we insist on making it complicated", font=('Rockwell Extra Bold', 20, 'bold','underline'), fg="dark blue",compound=TOP)
titlelabel1.configure(background = '#e1d8b9')
titlelabel1.pack(anchor=N)
titlelabel2 = Label(topframe, text="Source Service Solution", font=('Rockwell Extra Bold', 18, 'bold','underline'), fg="dark blue",compound=TOP)
titlelabel2.configure(background = '#e1d8b9')
titlelabel2.pack(anchor=N)
thelabel1 = Label(topframe, compound=TOP)
thelabel1.configure(background = '#e1d8b9')
thelabel1.pack(anchor=N)
thelabel2 = Label(leftframe, text="_______________________________________________________________________________________________________",compound=TOP)
thelabel2.configure(background = '#e1d8b9')
thelabel2.pack(anchor=N)
thelabel3 = Label(leftframe, text="Please Select The Desired Option From Given Link", font=('Cooper Black', 15,'underline'), fg="purple",compound=TOP)
thelabel3.configure(background = '#e1d8b9')
thelabel3.pack(anchor=N)
thelabel9 = Label(leftframe, compound=TOP)
thelabel9.configure(background = '#e1d8b9')
thelabel9.pack(anchor=N)

#------------Radio Button------------------
var = IntVar()
R1 = Radiobutton(leftframe, text="https://www.bbc.com", variable=var, value=1, fg="black", font=(10), command=rbsel)
R1.configure(background = '#e1d8b9')
R1.pack(anchor = N)
R2 = Radiobutton(leftframe, text="https://www.cnn.com", variable=var, value=2, fg="black", font=(10), command=rbsel)
R2.configure(background = '#e1d8b9')
R2.pack(anchor = N)
R3 = Radiobutton(leftframe, text="https://www.hindustantimes.com", variable=var, value=3, fg="black", font=(10),command=rbsel)
R3.configure(background = '#e1d8b9')
R3.pack(anchor = N)
R4 = Radiobutton(leftframe, text="https://www.timesofindia.indiatimes.com", variable=var, value=4, fg="black", font=(10),command=rbsel)
R4.configure(background = '#e1d8b9')
R4.pack(anchor = N)
R5 = Radiobutton(leftframe, text="https://www.thehindu.com", variable=var, value=5, fg="black", font=(10),command=rbsel)
R5.configure(background = '#e1d8b9')
R5.pack(anchor = N)
label = Label(leftframe)
label.configure(background = '#e1d8b9')
label.pack()

#----------Button Section--------------
thelabel8 = Label(root, anchor=S)
thelabel8.configure(background = '#e1d8b9', font=2)
thelabel8.pack(anchor=N)
button1 = Button(leftframe, text="View Result", font=('Cooper Black', 9), fg="red", bg="white", bd=10)
button1.pack(anchor = S)
thelabel4 = Label(leftframe, compound=BOTTOM)
thelabel4.configure(background = '#e1d8b9')
thelabel4.pack(anchor=N)
thelabel8 = Label(leftframe, compound=BOTTOM)
thelabel8.configure(background = '#e1d8b9')
thelabel8.pack(anchor=N)
thelabel5 = Label(bottomframe, anchor=S)
thelabel5.configure(background = '#e1d8b9')
thelabel5.pack(anchor=N)
thelabel7 = Label(bottomframe, text="@Copyright By Abhishek", font=(12),anchor=S)
thelabel7.configure(background = '#e1d8b9')
thelabel7.pack(anchor=N)

#---------Entrybox-------------------
thelabel11 = Label(rightframe, text="____________________________________________________________________________________________________________________",compound=TOP)
thelabel11.configure(background = '#e1d8b9')
thelabel11.pack(anchor=N)
thelabel10 = Label(rightframe, text="Enter The Any Specific Url For Which You Want to check", font=('Cooper Black', 15,'underline'), fg="purple", compound=TOP)
thelabel10.configure(background = '#e1d8b9')
thelabel10.pack(anchor=E)
thelabel12 = Label(rightframe)
thelabel12.pack(anchor=E)
E1 = Text(rightframe, height=10, width=50)
E1.pack(anchor=N)
thelabel13 = Label(rightframe)
thelabel13.pack(anchor=E)
thelabel14 = Label(rightframe)
thelabel14.pack(anchor=E) 
button2 = Button(rightframe, text="View Result", font=('Cooper Black', 9), fg="red", bg="white", bd=10)
button2.pack(anchor = S)
root.mainloop()




