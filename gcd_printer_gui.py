from Tkinter import *
from gcd_printer import *

window = Tk()

topFrame = Frame(window)
bottomFrame = Frame(window, background="pink")
topFrame.pack(fill=X)
bottomFrame.pack(side = BOTTOM)

ins = Label(topFrame, text = "Input two integers to find their GCD:", bg = 'gray')

var1 = StringVar()
var2 = StringVar()

ent1 = Entry(topFrame, textvariable = var1)
ent2 = Entry(topFrame, textvariable = var2)
andd = Label(topFrame, text = " and ")

def calc():
    num1 = int(ent1.get())
    num2 = int(ent2.get())
    print gcd(num1, num2) 

but = Button(bottomFrame, text = "Okay!", command = calc, bg = 'brown', fg = 'gray')

ins.pack(fill=X)
ent1.pack(fill=X, side = LEFT)
ent2.pack(fill=X, side = RIGHT)
andd.pack()
#but.pack()

window.mainloop()




