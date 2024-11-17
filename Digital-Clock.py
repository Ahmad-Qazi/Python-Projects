import tkinter as tk
from tkinter import *
from time import strftime

root = tk.Tk()
root.title("Digital Clock")


def time ():
    string = strftime("%H : %M : %S \n %D")

    label.config(text = string)
    label.after(1000,time)
label = tk.Label(font=("Arial", 50, "bold"), background="#08175E", foreground="white")
label.pack(anchor="center")    


time()

root.mainloop()
