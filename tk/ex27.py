from tkinter import *
import csv
m = Tk()
m.title("Running Pace Calculator")
m.configure(bg="#d4e28a", padx=20, pady=20)
fr1=Frame(m, bg="#d4e28a")
lab1=Label(m, text="Running Pace Calculator", fg="dark blue", bg="#d4e28a", font=("System", 24), width=25)
lab2=Label(m, text="Minutes:", bg="#d4e28a", font=("Cambria", 16), pady=6)
lab3=Label(m, text="Seconds:", bg="#d4e28a", font=("Cambria", 16), pady=6)
lab4=Label(m, text="Miles:", bg="#d4e28a", font=("Cambria", 16), pady=6)
lab5=Label(m, text="Date:", bg="#d4e28a", font=("Cambria", 16), pady=6)
lab6=Label(fr1, text="Month:", bg="#d4e28a", font=("Cambria", 16), pady=12, width=6)
lab7=Label(fr1, text="Day:", bg="#d4e28a", font=("Cambria", 16), pady=12, width=6)
lab8=Label(fr1, text="Year:", bg="#d4e28a", font=("Cambria", 16), pady=12, width=6)
lab9=Label(m, text="Pace/Mile:", bg="#d4e28a", font=("Cambria", 16), pady=6)
ent1=Entry(m, font=("none", 16))
ent2=Entry(m, font=("none", 16))
ent3=Entry(m, font=("none", 16))
ent4=Entry(fr1, font=("none", 16), width=4)
ent5=Entry(fr1, font=("none", 16), width=4)
ent6=Entry(fr1, font=("none", 16), width=5)
btn1=Button(m, pady=6, padx=6, text="USE TODAY")
btn2=Button(m, pady=6, padx=6, text="Show Pace")
btn3=Button(m, pady=6, padx=6, text="SAVE")
lab1.grid(columnspan=2)
ent1.grid(row=1, column=1)
ent2.grid(row=2, column=1)
ent3.grid(row=3, column=1)
lab2.grid(row=1, sticky=E)
lab3.grid(row=2, sticky=E)
lab4.grid(row=3, sticky=E)
lab5.grid(row=4, sticky=E)
btn1.grid(row=4, column=1)
fr1.grid(row=6, columnspan=4)
lab6.grid(row=0)
lab7.grid(row=0, column=1)
lab8.grid(row=0, column=2)
ent4.grid(row=1, column=0)
ent5.grid(row=1, column=1)
ent6.grid(row=1, column=2)
m.mainloop()