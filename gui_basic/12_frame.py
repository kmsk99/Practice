import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("R GUI")
root.geometry("640x480")

Label(root, text="menu").pack(side="top")
Label(root, text="wn").pack(side="bottom")



frame_burger = Frame(root, relief="solid", bd=1)
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="gamburger").pack()
Button(frame_burger, text="gamburasdger").pack()
Button(frame_burger, text="sad").pack()

frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill="both", expand=True)

Button(frame_drink, text="sad").pack()

root.mainloop()
