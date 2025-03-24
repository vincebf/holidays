
from tkinter import *
from tkinter.simpledialog import *

root= Tk()
root.title('我的第一个Python窗体')
root.geometry('1240x640') # 这里的乘号不是 * ，而是小写英文字母 x

lb = Label(root,text='我是第一个标签',\
        bg='#d3fbfb',\
        fg='red',\
        font=('华文新魏',32),\
        width=20,\
        height=2,\
        relief=SUNKEN)
lb.pack()
def xz():
    s=askstring('请输入','请输入一串文字')
    lb.config(text=s)
lb = Label(root,text='')
lb.pack()
btn=Button(root,text='弹出输入对话框',command=xz)
btn.pack()


root.mainloop()