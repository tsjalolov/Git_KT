'''import tkinter as tk
r = tk.Tk()
r.title('Salom s5 kt')
button = tk.Button\
         (r, text='chiqish',\
          width=25, command=r.destroy)
button2 = tk.Button\
         (r, text='chiqish',\
          width=25, command=quit)
button.pack()
button2.pack()
r.mainloop()'''








'''
from tkinter import *
master = Tk()
var1 = IntVar()
Checkbutton(master, text='male',\
            variable=var1).grid(row=1, sticky=W)
var2 = IntVar()
Checkbutton(master, text='female', \
            variable=var2).grid(row=0, sticky=W)
mainloop() '''


import tkinter as tk
root = tk.Tk()

on_image = tk.PhotoImage(width=48, height=24)
off_image = tk.PhotoImage(width=48, height=24)
on_image.put(("green",), to=(0, 0, 23,23))
off_image.put(("red",), to=(24, 0, 47, 23))

var1 = tk.IntVar(value=1)
var2 = tk.IntVar(value=0)
cb1 = tk.Checkbutton(root, image=off_image,\
                     selectimage=on_image, indicatoron=False,
                     onvalue=1, offvalue=0,\
                     variable=var1)
cb2 = tk.Checkbutton(root, image=off_image,\
                     selectimage=on_image, indicatoron=False,
                     onvalue=1, offvalue=0, variable=var2)

cb1.pack(padx=20, pady=10)
cb2.pack(padx=20, pady=10)

root.mainloop()

'''

from tkinter import (Tk, ttk, Label, Frame, Button,
    Checkbutton, Radiobutton, IntVar, HORIZONTAL)

class  SimpleGUI(Tk):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.title("Food Order Form")
        self.minsize(300, 200)  # width, height
        self.geometry("400x350+50+50")
        self.setupWindow()

    def setupWindow(self):
        """ Set up the widgets."""
        title = Label(self, text="Food Order Form",
            font=('Helvetica', 20), bd=10)
        title.pack()

        line = ttk.Separator(self, orient=HORIZONTAL)
        line.pack(fill='x')

        order_label = Label(self, text="What would you like to order?", bd=10)
        order_label.pack(anchor='w')

        foods_list = ["Sandwich", "Salad", "Soup", "Pizza"]
        self.foods_dict = {}

        # Populate the dictionary with checkbutton widgets
        for  i, food_item in  enumerate(foods_list):

            # Set the text for each checkbutton
            self.foods_dict[food_item] = Checkbutton(self, text=food_item)

            # Create a new instance of IntVar() for each checkbutton
            self.foods_dict[food_item].var = IntVar()

            # Set the variable parameter of the checkbutton
            self.foods_dict[food_item]['variable'] = self.foods_dict[food_item].var

            # Arrange the checkbutton in the window
            self.foods_dict[food_item].pack(anchor='w')

        payment_label = Label(self, text="How do you want to pay?", bd=10)
        payment_label.pack(anchor='w')

        # Create integer variable
        self.var = IntVar()
        self.var.set(0)  # Use set() initialize the variable
        self.payment_methods = ["PayPal", "Credit Card", "Other"]

        for  i, method in  enumerate(self.payment_methods):
            self.pymt_method = Radiobutton(self, text=method, variable=self.var, value=i)
            self.pymt_method.pack(anchor='w')

        # Use ttk to add styling to button
        style = ttk.Style()
        style.configure('TButton', bg='skyblue', fg='white')

        # Create button that will call the method to display text and
        # close the program
        next_button = ttk.Button(self, text="Next", command=self.printResults)
        next_button.pack()

    def printResults(self):
        """Print the results of the checkboxes and radio buttons."""
        for  cb in  self.foods_dict.values():
            if  cb.var.get():
                print('Item selected: {}'.format(cb['text']))

        index = self.var.get()
        print("Payment method: {}".format(self.payment_methods[index]))
        self.quit()

if  __name__  ==  "__main__":
    app = SimpleGUI()
    app.mainloop() '''

