from tkinter import *
from tkinter import ttk

def factorial(num):
    multiple = 1
    for i in range(num):
        multiple =  multiple * (num - i)
    return multiple

def on_click():
    print(factorial(int(entry.get())))
    return True

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Factorial Gui").grid(column=0, row=0)
entry = ttk.Entry(frm)
entry.grid(column=1, row=0)
ttk.Button(frm, text="Enter", command=on_click).grid(column=2, row=0)
root.mainloop()

print(factorial(5))