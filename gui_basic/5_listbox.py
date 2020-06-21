from tkinter import *

root = Tk()
root.title("R GUI")
root.geometry("640x480")
# root.geometry("640x480+300+100")

listbox = Listbox(root, selectmod="extended", height=0)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()

def btncmd():
    # listbox.delete(0)

    # print("리스트에는", listbox.size())
    # print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))

    print("선택된 항목 : ", listbox.get(listbox.curselection()))

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()
