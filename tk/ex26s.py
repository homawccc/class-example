from tkinter import *

m = Tk()
m.title("Attendees List")
m.configure(bg="#CCCCEE", padx=20, pady=20)

#Name Entry Labels
lab1 = Label(m, bg="#CCCCEE", pady=6, text="First")
lab2 = Label(m, bg="#CCCCEE", pady=6, text="Last")
#spacer labels
lab3 = Label(m, bg="#CCCCEE")
lab4 = Label(m, bg="#CCCCEE")
lab5 = Label(m, bg="#CCCCEE")
#Entry Fields
ent1 = Entry(m, font=("none",16))
ent1 = Entry(m, font=("none",16))
ent3 = Entry(m, font=("none",16))
#Buttons
btn1 = Button(m, padx=6, pady=6, text="Add Another")
btn2 = Button(m, padx=6, pady=6, text="Insert")
btn3 = Button(m, padx=6, pady=6, text="Add Attendee")
#grid output
lab1.grid(row=0, sticky=W)
lab2.grid(row=1, sticky=W)
ent1.grid(row=0, column=1)
ent2.grid(row=1, column=1)
lab3.grid(row=2, columnspan=2)
btn1.grid(row=3, column=0, sticky=W)
btn2.grid(row=3, column=1, sticky=E)
lab4.grid(row=4, columnspan=2)
ent3.grid(row=5, columnspan=2, sticky=E+W)
lab5.grid(row=5, columnspan=2)
btn3.grid(row=7, column=1, sticky=E)
m.mainloop()