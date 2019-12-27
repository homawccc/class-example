from tkinter import *

#Master Window
m=Tk()
m.title("Attendee List")
m.configure(bg ="#CCCCEE", padx=20, pady=20)

                #Functions
def showname():
    namedisp = ent1.get() + " " + ent2.get()
    ent3.delete(0,END)
    ent3.insert(0,namedisp)

def clearfeilds():
    ent1.delete(0,END)
    ent2.delete(0,END)
    ent3.delete(0,END)

def addattendee():
    pass


                #Fields
#LabelsName
lab1 = Label(m, bg="#CCCCEE", pady = 6, text="First")
lab2 = Label(m, bg="#CCCCEE", pady = 6, text="Last")
#LabelsSpacer
lab3 = Label(m, bg="#CCCCEE")
lab4 = Label(m, bg="#CCCCEE")
lab5 = Label(m, bg="#CCCCEE")
#Entries 
ent1 = Entry(m)
ent2 = Entry(m)
ent3 = Entry(m)
#Buttons
btn1 = Button(m, padx= 6, pady = 6, text = "Add Another")
btn2 = Button(m, padx= 6, pady = 6, text = "Insert", command = showname)
btn3 = Button(m, padx= 6, pady = 6, text = "Add Attendee", command = addattendee)


               #Grid Packing
#PackingLab
lab1.grid(row = 0, column = 0 )
lab2.grid(row = 1, column = 0 )
lab3.grid(row = 2, columnspan = 2 )
lab4.grid(row = 4, columnspan = 2 )
lab5.grid(row = 6, columnspan = 2 )
#PackingBtn
btn1.grid(row = 3, column = 0, sticky = W)
btn2.grid(row = 3, column = 1, sticky = E)
btn3.grid(row = 7, column = 1, sticky = E+W)
#PackingEnt
ent1.grid(row = 0, column = 1)
ent2.grid(row = 1, column = 1)
ent3.grid(row = 5, columnspan = 2, sticky = E+W)


m.mainloop()