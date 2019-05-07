from tkinter import *

def changecolor():
    lab1.config(text="Purple", bg="purple")
def changeback():
    lab1.config(text="Red", bg="red")

m = Tk()
m.title("ex26 Color Labels")

fr1 = Frame(m)
fr2 = Frame(m, pady=12)
#labels
lab1 = Label(fr1, text="Red", bg="red", fg="white", width=12, height=3, font=("Cambria", 24, "bold"))
lab2 = Label(fr1, text="Green", bg="green", fg="white", width=12, height=3, font=("Cambria", 24, "bold"))
lab3 = Label(fr1, text="Blue", bg="blue", fg="white", width=12, height=3, font=("Cambria", 24, "bold"))
#buttons
btn1 = Button(fr2, text="Button1", padx = 6, font=("none", 16), command=changecolor)
btn2 = Button(fr2, text="Button2", padx = 6, font=("none", 16), command=changeback)
btn3 = Button(fr2, text="Button3", padx = 6, font=("none", 16))

lab1.pack(side=LEFT)
lab2.pack(side=LEFT)
lab3.pack(side=LEFT)
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
fr1.pack(side=TOP)
fr2.pack(side=BOTTOM)

m.mainloop()