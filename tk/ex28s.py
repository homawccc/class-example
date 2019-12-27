from tkinter import *

#Master Window
m=Tk()
m.title("Running Pace Calculator")
m.configure(bg ="#CCCCEE", padx=20, pady=20)


                #Fields
#LabelsName
lab1 = Label(m, bg="#CCCCEE", pady = 6, text="Minutes:")
lab2 = Label(m, bg="#CCCCEE", pady = 6, text="Seconds:")
lab3 = Label(m, bg="#CCCCEE", pady = 6, text="Miles:")
lab4 = Label(m, bg="#CCCCEE", pady = 6, text="Date:")
lab5 = Label(m, bg="#CCCCEE", pady = 6, text="Or Enter Past Date:")
lab6 = Label(m, bg="#CCCCEE", pady = 6, text="Month:")
lab7 = Label(m, bg="#CCCCEE", pady = 6, text="Day:")
lab8= Label(m, bg="#CCCCEE", pady = 6, text="Year:")
lab9= Label(m, bg="#CCCCEE", pady = 6, text="Ex: 4 8 2019")
lab10= Label(m, bg="#CCCCEE", pady = 6, text="Pace/Mile:")
#LabelsSpacer
lab11 = Label(m, bg="#CCCCEE")
lab12 = Label(m, bg="#CCCCEE")
lab13 = Label(m, bg="#CCCCEE")

#Entries 
ent1 = Entry(m)
ent2 = Entry(m)
ent4 = Entry(m)
ent5 = Entry(m, width = 5)
ent6 = Entry(m, width = 5)
ent7 = Entry(m, width = 5)
ent8 = Entry(m)
#Buttons

btn1 = Button(m, padx= 6, pady = 6, text = "USE TODAY")
btn2 = Button(m, padx= 6, pady = 6, text = "Show Pace")
btn3 = Button(m, padx= 6, pady = 6, text = "SAVE")


               #Grid Packing
#PackingLab
lab1.grid(row = 0, column = 1 )
lab2.grid(row = 1, column = 1 )
lab3.grid(row = 2, column = 1 )
lab4.grid(row = 3, column = 1 )
lab5.grid(row = 4, columnspan = 4 )
lab6.grid(row = 5, column = 1 )
lab7.grid(row = 5, column = 2 )
lab8.grid(row = 5, column = 3 )
lab9.grid(row = 6, column = 0 )
lab10.grid(row = 8, column = 1 )
lab11.grid(row = 2, columnspan = 2 )
lab12.grid(row = 4, columnspan = 2 )
lab13.grid(row = 6, columnspan = 2 )
#PackingBtn

btn1.grid(row = 3, column = 2)
btn2.grid(row = 7, column= 5)
btn3.grid(row = 9, column = 5)

#PackingEnt
ent1.grid(row = 0, column = 2)
ent2.grid(row = 1, column = 2)
ent4.grid(row = 2, column = 2)
ent5.grid(row = 6, column = 1)
ent6.grid(row = 6, column = 2)
ent7.grid(row = 6, column = 3)
ent8.grid(row = 8, column = 2)


m.mainloop()