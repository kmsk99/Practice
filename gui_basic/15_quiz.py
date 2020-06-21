import os
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

filename = "mynote.txt"

# 메뉴 설정
def open_file():
    if os.path.isfile(filename):
        with open(filename, mode = "rt", encoding = "utf-8") as f:
            data = f.read()
        txt.delete("1.0", END)
        txt.insert(END, data)
    else:
        msgbox.showwarning("경고", "파일이 없습니다.")
        

def save_file():
    with open(filename, mode = "wt", encoding = "utf-8") as f:
        data = txt.get("1.0", END)
        f.writelines(data)
    
# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="열기", command=open_file)
menu_file.add_command(label="저장", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집")
menu.add_cascade(label="서식")
menu.add_cascade(label="보기")
menu.add_cascade(label="도움말")

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# 텍스트 박스
txt=Text(root, yscrollcommand = scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

scrollbar.config(command=txt.yview)

root.config(menu=menu)
root.mainloop()
