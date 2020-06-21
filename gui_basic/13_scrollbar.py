import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("R GUI")
root.geometry("640x480")

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

listbox = Listbox(frame, selectmod="extended", height=10, yscrollcommand = scrollbar.set)
for i in range(1, 32):
    listbox.insert(END, str(i) + "일")
listbox.pack(side="left")

scrollbar.config(command=listbox.yview)

root.mainloop()
