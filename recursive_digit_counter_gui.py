from Tkinter import *
from recursive_digit_counter import *

window=Tk()                               #opens window`


instr = Label(window, text = "Enter any integer to count its digits:", bg = 'gray')
                                          #^instruction text
#Text and entry:

e = StringVar()
form = Entry(window, textvariable = e)    #maps entry widget to variable 'e'

instr.pack(fill = X)
form.pack(fill = X)                       #packs text and entry

#Button:

def ready():                         #def of function to be run on button-press
    num = int(e.get())
    counter(num)

but = Button(window, text="Count!", bg = 'brown', fg = 'gray', command = ready)
but.pack()                                #button is created and packed


window.mainloop()                         #keeps window open



    


