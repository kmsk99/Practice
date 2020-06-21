import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("R GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "결재오류가 발생했습니다.")

def okcancel():
    msgbox.askokcancel("확인 / 취소", "예매 하시겠습니까.")

def retrycancel():
    msgbox.askretrycancel("확인 / 취소", "예매 하시겠습니까.")

def yesno():
    msgbox.askyesno("확인 / 취소", "예매 하시겠습니까.")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 하시겠습니까.")
    if response == 1:
        print("예")
    elif response ==0:
        print("no")
    else:
        print("none")

Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="확인 취소").pack()
Button(root, command=yesno, text="확인 취소").pack()
Button(root, command=yesnocancel, text="확인 취소").pack()



root.mainloop()
