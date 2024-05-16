'''import tkinter as tk
r = tk.Tk()
r.title('Salom s6 kt')
button = tk.Button\
         (r, text='quit',width=25, command=r.destroy)
button.pack()
r.mainloop()'''


from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male',\
            variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', \
            variable=var2).grid(row=1, sticky=W)
mainloop()

