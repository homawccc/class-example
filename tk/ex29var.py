from tkinter import *

m = Tk()
m.title("Tip Calculator")
m.configure(bg="#EECCEE", padx=14, pady=14)

def down():
    t=ent2.get()
    t=int(t)
    t=t-1
    ent2.delete(0,END)
    ent2.insert(0,t)
def up():
    t=ent2.get()
    t=int(t)
    t=t+1
    ent2.delete(0,END)
    ent2.insert(0,t)
def calc():
    message="Enter $"
    t=ent2.get()
    t=int(t)
    t=t*.01
    meal=ent1.get()
    if meal=='':
        ent1.insert(0,message)
    meal=float(meal)
    tipamount=meal*t
    total=meal+tipamount
    tipamount = f"${tipamount:.02f}"
    total = f"${total:.02f}"
    ent3.delete(0,END)
    ent3.insert(0,tipamount)
    ent4.delete(0,END)
    ent4.insert(0,total)

#Labels
labt=Label(m, text='Tip Calculator', 
fg='#0000AA', bg="#EECCEE", pady=6, font=('Cambria', 24, 'bold'))
lab1=Label(m, text='Meal Total ', bg="#EECCEE", font=('none', 14), pady=6)
lab2=Label(m, text='Tip Percent ', bg="#EECCEE", font=('none', 14), pady=6)
lab3=Label(m, text='Adjust Tip % ', bg="#EECCEE", font=('none', 14), pady=6)


ent1 = Entry(m, font=("none", 14), width=10)
ent2 = Entry(m, font=("none", 14), width=10)
t=20 #default tip
ent2.insert(0,t) #displays default tip

fra1 = Frame(m, bg="#CCEECC")
btn1=Button(fra1, text=' << ', font=("none", 12), command=down)
btn2=Button(fra1, text=' >> ', font=("none", 12), command=up)

btn3=Button(m, text='Calculate', font=("none", 14, 'bold'), command=calc)
lab4=Label(m, text='Tip Amount ', bg="#EECCEE", font=('none', 14), pady=6)
lab5=Label(m, text='Meal & Tip ', bg="#EECCEE", font=('none', 14), pady=6)
ent3 = Entry(m, font=("none", 14), width=10)
ent4 = Entry(m, font=("none", 14), width=10)

#grid layout
labt.grid(row=0, columnspan=2)
lab1.grid(row=1, column=0, sticky=E)
lab2.grid(row=2, column=0, sticky=E)
lab3.grid(row=3, column=0, sticky=E)
ent1.grid(row=1, column=1, sticky=W)
ent2.grid(row=2, column=1, sticky=W)
fra1.grid(row=3, column=1, sticky=W)
btn1.grid(row=0, column=0, sticky=W)
btn2.grid(row=0, column=1, sticky=W)
btn3.grid(row=4, column=1, sticky=W)
lab4.grid(row=5, column=0, sticky=E)
lab5.grid(row=6, column=0, sticky=E)
ent3.grid(row=5, column=1, sticky=W)
ent4.grid(row=6, column=1, sticky=W)

m.mainloop()