'''
import tkinter as tk
r = tk.Tk()
r.title('Salom s4 kt -----')
button = tk.Button\
         (r, text='--chiqish--',\
          width=25, command=r.destroy)
button.pack()
r.mainloop()

'''









from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='s4',\
            variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='s5', \
            variable=var2).grid(row=1, sticky=W)
mainloop() 


