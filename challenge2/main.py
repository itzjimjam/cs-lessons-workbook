import tkinter as Tk
from math import trunc
from tkinter import ttk


def on_click():
    r = int(hour.get())
    r2 = int(hour2.get())
    m = int(min.get())
    m2 = int(min2.get())
    distance = int(dist.get())

    time = (r2 * 60 + m2) - (r * 60+ m)
    time_in_hours = time / 60

    speed = distance / time_in_hours
    speedl.config(text=f"Speed: {trunc(speed)} mph")

    return "True"

root = Tk.Tk()
root.title("Time Calculation Speeding")
frm = ttk.Frame(root, width=500, height=500)
root.geometry("500x500")
frm.grid()

ttk.Label(frm, text="Time for 1st card:").grid(column=0, row=0)
ttk.Label(frm, text="Time for 2st card:").grid(column=0, row=1)
ttk.Label(frm, text="Distance between cameras:").grid(column=0, row=2)
speedl = ttk.Label(frm, text="Speed: ___ mph")
speedl.grid(column=0, row=4)


hour = ttk.Entry(frm)
hour.grid(column=1, row=0)
hour2 = ttk.Entry(frm)
hour2.grid(column=1, row=1)
min = ttk.Entry(frm)
min.grid(column=2, row=0)
min2 = ttk.Entry(frm)
min2.grid(column=2, row=1)

dist = ttk.Entry(frm)
dist.grid(column=1, row=2)

ttk.Button(frm, text="Enter", command=on_click).grid(column=2, row=2)

root.mainloop()