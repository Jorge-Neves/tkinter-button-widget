from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()

root.geometry("500x500")


def popup_one():
    messagebox.showinfo("Popup Content")


Label(root, text="Screen one").pack(pady=30)

ttk.Button(root, text="Click", command=popup_one).pack(pady=20)
root.mainloop()
