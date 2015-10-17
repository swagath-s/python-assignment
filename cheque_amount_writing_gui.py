from Tkinter import *
from cheque_amount_writing import *

window = Tk()

ins = Label(window, text="Enter any number smaller than a trillion to textify it:")


v = StringVar()
ent = Entry(window, textvariable = v)

def gen():
    textify(int(v.get()))

but = Button(window, text = "Do it!", command = gen, bg = 'brown', fg = 'gray')

ins.pack(fill = X)
ent.pack(fill = X)
but.pack()

window.mainloop()
