from tkinter import *
import datetime
import csv

def showpace():
    #--will be part of showpace() function
    minutes = int(ent1.get()) #from ent1
    seconds = int(ent2.get()) #from ent2
    miles = float(ent3.get()) #from ent3
    #------------
    #calcs based on 24:59 in 3.1 miles
    mpm = minutes/miles #7.74 mins
    mpm_s = int(mpm * 60) #464.4 secs
    spm = seconds/miles #19.03
    total_s = mpm_s + spm  #483.43
    mpm = total_s/60  #8.05
    mpm_int = int(mpm) #8
    spm = (mpm-mpm_int)*60  #.05*60=3.0
    spm = int(spm)  #3
    pace = f"{mpm_int}:{spm:02}"
    #-----display pace code below
    ent7.delete(0,END)
    ent7.insert(0,pace)

def usetoday():
    shortdate = datetime.date.today()
    shortdate = str(shortdate)
    ent4.delete(0,END)
    ent4.insert(0,shortdate[5:7])
    ent5.delete(0,END)
    ent5.insert(0,shortdate[8:])
    ent6.delete(0,END)
    ent6.insert(0,shortdate[0:4])
    #2019-05-04 
def save_csv():
    #use in save_csv() function
    paces = [] #creates empty list
    month = int(ent4.get())
    day = int(ent5.get())
    year = int(ent6.get())
    date = datetime.date(year, month, day)
    pace = ent7.get()
    paces.append(date)
    paces.append(pace)
    #writes to paces.csv file
    with open('paces.csv', 'a', newline="") as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(paces)           

m = Tk()
m.title("Running Pace")
m.configure(bg="#CCEECC", padx=16, pady=12)

#GUI Widgets
labt=Label(m, text='Running Pace Calculator', fg='#0000AA', bg="#CCEECC", pady=6, font=('Cambria', 24, 'bold'))
lab1=Label(m, text='Minutes ', bg="#CCEECC", font=('none', 14), pady=4)
lab2=Label(m, text='Seconds ', bg="#CCEECC", font=('none', 14), pady=4)
lab3=Label(m, text='Miles ', bg="#CCEECC", font=('none', 14), pady=4)
lab4=Label(m, text='Date ', bg="#CCEECC", font=('none', 14), pady=4)
lab5=Label(m, text='Or Enter Past Date: ', bg="#CCEECC", font=('none', 12), pady=4)
btn1=Button(m, text='USE TODAY', font=("none", 12), command=usetoday)
ent1 = Entry(m, font=("none", 14), width=10)
ent2 = Entry(m, font=("none", 14), width=10)
ent3 = Entry(m, font=("none", 14), width=10)
#--frame widget in row6--2rows,3cols
fra1 = Frame(m, bg="#CCEECC")
lab6=Label(fra1, text='Month:', bg='#CCEECC', font=('none', 14), pady=4)
lab7=Label(fra1, text='Day:    ', bg='#CCEECC', font=('none', 14), pady=4)
lab8=Label(fra1, text='Year:', bg='#CCEECC', font=('none', 14), pady=4)
ent4 = Entry(fra1, font=("none", 14), width=3)
ent5 = Entry(fra1, font=("none", 14), width=3)
ent6 = Entry(fra1, font=("none", 14), width=6)
#--end fra1
btn2=Button(m, text='SHOW PACE', font=("none", 12), command=showpace)
lab9=Label(m, text='ex: 4 8 2019', bg='#CCEECC', font=('none', 12, 'italic'), pady=4)
lab10=Label(m, text='Pace/Mile:', bg='#CCEECC', font=('none', 14), pady=4)
ent7 = Entry(m, font=("none", 14))
btn3=Button(m, text='SAVE', font=("none", 14, 'bold'), command=save_csv)

#grid layout 10 rows, 2 col, 
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
ent4.grid(row=1, column=0, sticky=W) #fra1
ent5.grid(row=1, column=1, sticky=W) #fra1
ent6.grid(row=1, column=2, sticky=W) #fra1
lab6.grid(row=0, column=0, sticky=W) #fra1
lab7.grid(row=0, column=1, sticky=W) #fra1
lab8.grid(row=0, column=2, sticky=W) #fra1
lab9.grid(row=7, column=0, sticky=S+E)
btn2.grid(row=8, column=1, sticky=W)
lab10.grid(row=9, column=0, sticky=E)
ent7.grid(row=9, column=1, sticky=W)
btn3.grid(row=10, column=1, sticky=W)


m.mainloop()