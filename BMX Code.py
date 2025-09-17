from tkinter import *
from tkinter.font import *
from tkinter.messagebox import *
from PIL import Image,ImageTk
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def get1f():
    global age, text1, text2, w1, w2, h, w
    
    agev=age.get()
    if w1.get() == "Metre":
        h=float(text1.get())
    elif w1.get() == "Centimetre":
        h=(float(text1.get()))/100
    elif w1.get() == "Inches":
        h=(float(text1.get()))/39.37
    if w2.get() == "KG":
        w=float(text2.get())
    elif w2.get() == "Pound":
        w=(float(text2.get()))/2.205
        
    global BMI
    BMI=w/(h**2)
    global clas
    clas={18:"Under weight",25:"Healthy",30:"Over weight",40:"Obese"}
    global re
    if BMI <= 18:
        re="Under weight"
    elif BMI <= 25:
        re="Healthy"
    elif BMI <= 30:
        re="Over weight"
    else:
        re="Obese"

def get2f():
    global BMI, h, w, age, sub
    global st1, st2, cal
    global ss1, ss2, ss3
    
    a=age.get()
    if BMI >25 :
        etw=(BMI*(h**2))-(25*(h**2))
        st1="burnt"
        st2="burn"
        ss1="1) Do an exercise for atleast 30 minutes daily."
        ss2="2) Substitute high calorie food with low calorie food."
        ss3="3) Practice intermittent fasting once a week."
    elif BMI <18 :
        etw=(18*(h**2))-(BMI*(h**2))
        st1="gained"
        st2="gain"
        ss1="1) Increase protein in the diet."
        ss2="2) Substitute low calorie food with high calorie food."
        ss3="3) Do meditation twice a week."
    if sub != 0:
        cal=(etw*7700)/sub
    elif sub == 0:
        cal=(etw*7700)
    global pr
    pr=((10*w)+(625*h)-(5*a)-78)*1.4
    
def Buttonf():
    global varadio
    global texter
    global sub
    if varadio.get()==100 and (texter.get()).isdigit():
        sub=int(texter.get())
    else:
        sub=varadio.get()
        
def Classificationwindowf():
    Classificationwindow = Tk()
    Classificationwindow.geometry("1350x750+0+0")
    Classificationwindow.title("BMX")
    Classificationwindow['bg']='#333F50'
    try:
       Classificationwindow.iconbitmap(sys._MEIPASS + '\\BMX.ico')
    except Exception:
       try:
          Classificationwindow.iconbitmap("BMX.ico")
       except Exception:
          pass
    Classificationwindow.resizable(width=False, height=False)
    global sub
    global st1, st2
    global cal, pr
    global ss1, ss2, ss3

    if sub==0 :
        showinfo("Error Message",  "Please select a proper plan")
        Classificationwindow.destroy()
        Resultwindowf()

    logo3=Label(Classificationwindow,
	         text="BMX",
	         fg = "#2BF543",
	         bg = "#333F50",
	         font = "Magneto 55")
    logo3.pack(anchor="ne")
    
    lt=Label(Classificationwindow,
		 text="The extra calories to be "+st1+" :\n"+"%.2f" %cal +" Kcal per day for "+str(sub)+" days",
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=0)
    ls=Label(Classificationwindow,
		 text="Calories to be consumed :\n"+"%.2f" %pr+" Kcal per day",
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=150)
    ls=Label(Classificationwindow,
		 text="Suggestions to "+st2+" calories :",
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=300)
    ls=Label(Classificationwindow,
		 text=ss1+"\n"+ss2+"\n"+ss3,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=375)
    Bc2 = Button(Classificationwindow, text ="Click to go back", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=14, bd=5,command = lambda:[Classificationwindow.destroy(),Resultwindowf()]).place(x=50,y=600)


    
    Classificationwindow.mainloop()
        

def Resultwindowf():
    
    Resultwindow = Tk()
    Resultwindow.geometry("1350x750+0+0")
    Resultwindow.title("BMX")
    Resultwindow['bg']='#333F50'
    try:
       Resultwindow.iconbitmap(sys._MEIPASS + '\\BMX.ico')
    except Exception:
       try:
          Resultwindow.iconbitmap("BMX.ico")
       except Exception:
          pass
    Resultwindow.resizable(width=False, height=False)

    logo2=Label(Resultwindow,
	         text="BMX",
	         fg = "#2BF543",
	         bg = "#333F50",
	         font = "Magneto 55")
    logo2.pack(anchor="ne")
    
    global BMI
    ly=Label(Resultwindow,
		 text="Your BMI is "+"%.2f" %BMI ,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=0)
    global re
    lt=Label(Resultwindow,
		 text="You are "+re ,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=100)
    if BMI >25 or BMI <18 :
        lv=Label(Resultwindow,
		 text="Choose any of the following plans:" ,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 30").place(x=50,y=200)
        global varadio
        global texter
        varadio = IntVar()
        texter=StringVar()
        Er = Entry(Resultwindow, width=3, font = "Barlow 20", textvariable=texter).place(x=100,y=515) 
        R1 = Radiobutton(Resultwindow, text="60 days", variable=varadio, fg = "#2BF543", bg = "#333F50", font = "Georgia 20", value=60).place(x=50,y=300)
        R2 = Radiobutton(Resultwindow, text="90 days", variable=varadio, fg = "#2BF543", bg = "#333F50", font = "Georgia 20", value=90).place(x=50,y=350)
        R3 = Radiobutton(Resultwindow, text="120 days", variable=varadio, fg = "#2BF543", bg = "#333F50", font = "Georgia 20", value=120).place(x=50,y=400)
        R4 = Radiobutton(Resultwindow, text="180 days", variable=varadio, fg = "#2BF543", bg = "#333F50", font = "Georgia 20", value=180).place(x=50,y=450)
        R5 = Radiobutton(Resultwindow, variable=varadio, fg = "#2BF543", bg = "#333F50", font = "Georgia 20", value=100).place(x=50,y=500)
        l5 = Label(Resultwindow,
		 text="days" ,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 20").place(x=200,y=500)

        Br1 = Button(Resultwindow, text ="Click to Proceed", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=14, bd=5,command = lambda:[Buttonf(),Resultwindow.destroy(),get2f(),Classificationwindowf()]).place(x=50,y=600)
        Br2 = Button(Resultwindow, text ="Click to go back", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=14, bd=5,command = lambda:[Resultwindow.destroy(),BMIwindowf()]).place(x=550,y=600)
    else :
        lv=Label(Resultwindow,
		 text="Thanks for using BMX" ,
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Magneto 30").place(x=375,y=375)

        Br2 = Button(Resultwindow, text ="Click to go back", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=14, bd=5,command = lambda:[Resultwindow.destroy(),BMIwindowf()]).place(x=50,y=600)


    
    Resultwindow.mainloop()
    
def BMIwindowf():
    BMIwindow = Tk()
    BMIwindow.geometry("1350x750+0+0")
    BMIwindow.title("BMX")
    BMIwindow['bg']='#333F50'
    try:
       BMIwindow.iconbitmap(sys._MEIPASS + '\\BMX.ico')
    except Exception:
       try:
          BMIwindow.iconbitmap("BMX.ico")
       except Exception:
          pass
    BMIwindow.resizable(width=False, height=False)

    logo1=Label(BMIwindow,
	text="BMX",
	fg = "#2BF543",
	bg = "#333F50",
	font = "Magneto 55")
    logo1.pack(anchor="ne")

    la=Label(BMIwindow, 
		 text="Enter the Values",
                 bg = "#333F50",
		 fg = "#2BF543",
		 font = "Georgia 30").place(x=50,y=0)

    lb=Label(BMIwindow, 
		 text="Age:",
                 bg = "#333F50",
		 fg = "#2BF543",
		 font = "Georgia 20").place(x=50,y=150)
    
    global age
    age = IntVar()
    Age = Scale(BMIwindow, variable = age, orient=HORIZONTAL, length=500, bg = "#333F50", font = "Georgia 15", fg="#2BF543")
    Age.set(30)
    Age.place(x=230,y=150)

    lx=Label(BMIwindow, 
		 text="Height:",
                 bg = "#333F50",
		 fg = "#2BF543",
		 font = "Georgia 20").place(x=50,y=300)
    global w1
    t1=("Metre","Inches","Centimetre")
    w1 = Spinbox(BMIwindow, values=t1, fg = "#333F50", font = "Georgia 20")
    w1.place(x=675,y=300)
    
    global text1
    text1=StringVar()
    global text2
    text2=StringVar()
    E1 = Entry(BMIwindow, font = "Barlow 20", fg = "#333F50", textvariable=text1).place(x=230,y=300)
    ly=Label(BMIwindow,
		 text="Weight:",
		 fg = "#2BF543",
		 bg = "#333F50",
		 font = "Georgia 20").place(x=50,y=450)
    global w2
    t2=("KG","Pound")
    w2 = Spinbox(BMIwindow, values=t2, fg = "#333F50", font = "Georgia 20")
    w2.place(x=675,y=450)
    
    E2 = Entry(BMIwindow, font = "Barlow 20", fg = "#333F50", textvariable=text2).place(x=230,y=450)
    
    B1 = Button(BMIwindow, text ="Click for Result", fg = "#F1E96E", bg = "#595959", font = "Georgia 20", height=2, width=12, bd=5,command = lambda:[get1f(),BMIwindow.destroy(),Resultwindowf()]).place(x=50,y=600)


    
    BMIwindow.mainloop()

def Expwindowf():
    Expwindow = Tk()
    Expwindow.geometry("1350x750+0+0")
    Expwindow.title("BMX")
    Expwindow['bg']='#333F50'
    try:
       Expwindow.iconbitmap(sys._MEIPASS + '\\BMX.ico')
    except Exception:
       try:
          Expwindow.iconbitmap("BMX.ico")
       except Exception:
          pass
    Expwindow.resizable(width=False, height=False)
    logoe=Label(Expwindow,
	      text="BMX",
	      fg = "#2BF543",
	      bg = "#333F50",
	      font = "Magneto 55")
    logoe.pack(anchor="ne")
    lge=Label(Expwindow,
	     text="BMX is a program build to help people with their health using the simple but \nefficient scientific method 'BMI'(Body Mass Index).\n\nThis product is an advanced state of art technology, empowering people \nto use scientific ways to test health condition regularly and maintain a healthy balanced life. \n\nIt uses the Harris–Benedict equation to calculate the BMR(Basal Metabolic Rate) \nthat is the average calories to be consumed per day.",
	     fg = "#2BF543",
	     bg = "#333F50",
	     font = "Georgia 18").place(x=0,y=175)
    Bae = Button(Expwindow, text ="Click to Continue", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=14, bd=5, command = lambda:[Expwindow.destroy(),BMIwindowf()]).place(x=50,y=600)
    ver=Label(Expwindow,
	     text="By Arnob Mitra",
	     fg = "#2BF543",
	     bg = "#333F50",
	     font = "Georgia 20")
    ver.place(x=650,y=700)
    lge1=Label(Expwindow,
	     text="v-1.0.1",
	     fg = "#2BF543",
	     bg = "#333F50",
	     font = "Georgia 15")
    lge1.place(x=1250,y=700)



    Expwindow.mainloop()

main = Tk()
main.geometry("1350x750+0+0")
main.title("BMX")
main['bg']='#333F50'
try:
    main.iconbitmap(sys._MEIPASS + '\\BMX.ico')
except Exception:
    try:
        main.iconbitmap("BMX.ico")
    except Exception:
        pass
main.resizable(width=False, height=False)
lg=Label(main,
	text="Welcome to",
	fg = "#2BF543",
	bg = "#333F50",
	font = "Magneto 45").place(x=450,y=175)
lg1=Label(main,
	text="BMX",
	fg = "#2BF543",
	bg = "#333F50",
	font = "Magneto 55")
lg1.place(x=535,y=275)
Ba = Button(main, text ="Click to Start", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=12, bd=5, command = lambda:[main.destroy(),BMIwindowf()]).place(x=250,y=500)
Bb = Button(main, text ="Click for Explanation", bg = "#595959", fg="#F1E96E", font = "Georgia 20", height=2, width=17, bd=5, command = lambda:[main.destroy(),Expwindowf()]).place(x=700,y=500)


main.mainloop()
