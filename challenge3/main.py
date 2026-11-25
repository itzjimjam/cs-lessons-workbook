import tkinter as Tk
from tkinter import ttk

options = []


def possibility(num1, num2, num3, num4):
    numbers = [num1, num2, num3, num4]
    for i in range(4): #first digit
        # numbers[i]
        for a in range(4): #second digit
            if a != i:
                # numbers[a]
                for b in range(4):
                    if b != i and b != a:
                        # numbers[b]
                        for c in range(4):
                            if c != i and c != a and c != b:
                                #numbers[c]
                                pin = str(numbers[i]) + str(numbers[a]) + str(numbers[b]) + str(numbers[c])
                                options.append(pin)

def on_click():
    possibility(one.get(), two.get(), three.get(), four.get())
    pos.config(text=f"List of options: {options}")

root = Tk.Tk()
root.title("Time Calculation Speeding")
frm = ttk.Frame(root, width=500, height=500)
root.geometry("500x500")
frm.grid()

ttk.Label(frm, text="1st digit:").grid(column=0, row=0)
ttk.Label(frm, text="2nd digit:").grid(column=0, row=1)
ttk.Label(frm, text="3rd digit:").grid(column=0, row=2)
ttk.Label(frm, text="4th digit:").grid(column=0, row=3)

one = ttk.Entry(frm)
one.grid(column=1, row=0)
two = ttk.Entry(frm)
two.grid(column=1, row=1)
three = ttk.Entry(frm)
three.grid(column=1, row=2)
four = ttk.Entry(frm)
four.grid(column=1, row=3)

ttk.Button(frm, text="Enter", command=on_click).grid(column=0, row=4)

pos = ttk.Label(frm, text="List of options: ")
pos.grid(column=0, row=5)


possibility(1,2,3,4)

root.mainloop()