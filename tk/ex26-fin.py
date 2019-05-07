from tkinter import *

def changepurple():
    lab1.config(bg="purple", text="Purple Label")
    #lab1.config(text="Purple Label")

m = Tk()
m.title("Tkinter Color Labels")

#frame
fr1 = Frame(m)
fr2 = Frame(m, pady=16)
#labels
lab1 = Label(fr1, text="Red Label", fg="#ffffff", bg="red", width=12,  height=6, font=("Cambria", 24))
lab2 = Label(fr1, text="Green Label", fg="#ffffff", bg="green", width=12,  height=6, font=("Cambria", 24))
lab3 = Label(fr1, text="Blue Label", fg="#ffffff", bg="blue", width=12,   height=6, font=("Cambria", 24))
#buttons
btn1 = Button(fr2, text="Button1", padx = 6, font=("none", 16), command=changepurple)
btn2 = Button(fr2, text="Button2", padx = 6, font=("none", 16))
btn3 = Button(fr2, text="Button3", padx = 6, font=("none", 16))
#packing
fr1.pack()
lab1.pack(side = LEFT, fill=Y)
lab2.pack(side = LEFT, fill=Y)
lab3.pack(side = LEFT, fill=Y)
fr2.pack()
btn1.pack(side=LEFT)
btn2.pack(side=LEFT)
btn3.pack(side=LEFT)
#mainloop
m.mainloop()