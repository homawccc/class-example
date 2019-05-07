from tkinter import *
import datetime
import csv

def showpace():
    minutes = float(ent1.get())
    seconds = float(ent2.get())
    miles = float(ent3.get())
    #calcs
    mpm = minutes/miles
    mpm_rnd = int(mpm) #cuts off decimal
    mpm_secs = mpm-mpm_rnd #leftover seconds
    mpm_secs = mpm_secs* 60 #converts decimal to seconds
    spm = seconds/miles + mpm_secs
    spm = round(spm)
    pace = f"{mpm_rnd}:{spm:02}"
    ent7.delete(0,END)
    ent7.insert(0,pace)
def usetoday():
    shortdate = str(datetime.date.today())
    ent4.delete(0,END)
    ent4.insert(0,shortdate[5:7])
    ent5.delete(0,END)
    ent5.insert(0,shortdate[8:])
    ent6.delete(0,END)
    ent6.insert(0,shortdate[0:4])
def save():
    paces = []
    month = int(ent4.get())
    day = int(ent5.get())
    year = int(ent6.get())
    date = datetime.date(year, month, day)
    pace = ent7.get()
    paces.append(date)
    paces.append(pace)
    with open('paces.csv', 'a', newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(paces)    
    
m = Tk()
m.title("Running Pace")
m.configure(bg="#CCEECC", padx=16, pady=12)

#Labels
labt=Label(m, text='Running Pace Calculator', 
fg='#0000AA', bg="#CCEECC", pady=6, font=('Cambria', 24, 'bold'))
lab1=Label(m, text='Minutes ', bg="#CCEECC", font=('none', 14), pady=4)
lab2=Label(m, text='Seconds ', bg="#CCEECC", font=('none', 14), pady=4)
lab3=Label(m, text='Miles ', bg="#CCEECC", font=('none', 14), pady=4)
lab4=Label(m, text='Date ', bg="#CCEECC", font=('none', 14), pady=4)
ent1 = Entry(m, font=("none", 14), width=10)
ent2 = Entry(m, font=("none", 14), width=10)
ent3 = Entry(m, font=("none", 14), width=10)
btn1=Button(m, text='USE TODAY', font=("none", 12), command=usetoday)
lab5=Label(m, text='Or Enter Past Date: ', bg="#CCEECC", font=('none', 12), pady=4)
fra1 = Frame(m, bg="#CCEECC")
lab6=Label(fra1, text='Month:', bg='#CCEECC',font=('none', 14), pady=4)
lab7=Label(fra1, text='Day:    ', bg='#CCEECC',font=('none', 14), pady=4)
lab8=Label(fra1, text='Year:', bg='#CCEECC',font=('none', 14), pady=4)
lab9=Label(m, text='ex: 4 8 2019', bg='#CCEECC',font=('none', 12, 'italic'), pady=4)
ent4 = Entry(fra1, font=("none", 14), width=3)
ent5 = Entry(fra1, font=("none", 14), width=3)
ent6 = Entry(fra1, font=("none", 14), width=6)
btn2=Button(m, text='SHOW PACE', font=("none", 12), command=showpace)
lab10=Label(m, text='Pace/Mile:', bg="#CCEECC", font=('none', 14), pady=4)
ent7 = Entry(m, font=("none", 14))
lab11=Label(m, text=' ', bg="#CCEECC", font=('none', 14), pady=10) #empty spacer
btn3=Button(m, text='SAVE', font=("none", 14, 'bold'), command=save)
lab12=Label(m, text=' ', bg="#CCEECC", font=('none', 14), pady=10)

#grid layout
labt.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
lab4.grid(row=4, column=0, sticky=E)
lab5.grid(row=5, column=1, sticky=W)
lab6.grid(row=6, column=1, sticky=W)
ent1.grid(row=1, column=1, sticky=W)
ent2.grid(row=2, column=1, sticky=W)
ent3.grid(row=3, column=1, sticky=W)
btn1.grid(row=4, column=1, sticky=W)
fra1.grid(row=7, column=1, sticky=W)
ent4.grid(row=1, column=0, sticky=W)
ent5.grid(row=1, column=1, sticky=W)
ent6.grid(row=1, column=2, sticky=W)
lab6.grid(row=0, column=0, sticky=W) #fra1
lab7.grid(row=0, column=1, sticky=W) #fra1
lab8.grid(row=0, column=2, sticky=W) #fra1
lab9.grid(row=7, column=0, sticky=S+E)
btn2.grid(row=8, column=1, sticky=W)
lab10.grid(row=9, column=0, sticky=E)
ent7.grid(row=9, column=1, sticky=W)
lab11.grid(row=8, column=0, sticky=E)
btn3.grid(row=10, column=1, sticky=W)
lab12.grid(row=10, column=0, sticky=E)

m.mainloop()