from tkinter import *
def onclick():
    print('bosildi')
root = Tk()
label_1 = Label(root,text='salom label')
Button  = Button(root, text='salom',fg ='red',command=onclick)
Button.pack()
label_1.pack()
root.mainloop()
