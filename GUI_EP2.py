from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('information') # นี่คือชื่อโปรแกรม
GUI.geometry('500x400') # นี่คือขนาดของโปรแกรม

def Button1():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=0,y=0)
B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท',command=Button1)
B1.pack(ipadx=20,ipady=20)


def Button2():
    text = 'ไม่มีเงินเหลือ'
    messagebox.showinfo('หมด',text)

FB2 = Frame(GUI)
FB2.place(x=300,y=600)
B2 = ttk.Button(GUI,text='เดือนนี้ัเหลือเงิน',command=Button2)
B2.pack(ipadx=20,ipady=20)

GUI.mainloop()

