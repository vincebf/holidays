from tkinter import *


def run1():
    a = float(tdxml.get())
    b = float(qmtml.get())
    s = "%0.2f+%0.2f=%0.2f\n" % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    tdxml.delete(0, END)  # 清空输入
    qmtml.delete(0, END)  # 清空输入


def run2(x, y):
    a = float(x)
    b = float(y)
    s = "%0.2f+%0.2f=%0.2f\n" % (a, b, a + b)
    txt.insert(END, s)  # 追加显示运算结果
    tdxml.delete(0, END)  # 清空输入
    qmtml.delete(0, END)  # 清空输入


# window.geometry("800x500+374+182")
window = Tk()
window.geometry("1024x800")
window.title("LookAtMyLOGO")  # 更改标题名字
window.iconbitmap("sb.ico")
window.resizable(True, True)

程序表头 = Label(
    window,
    text="请输入两个数，按下面两个按钮之一进行加法计算",
    bg="#d3fbfb",
    font=("华文新魏", 16),
    width=20,
    height=2,
    relief=SUNKEN,
).place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.1)


tdx目录 = Label(
    window,
    text="tdx目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.01, rely=0.2, relwidth=0.05, relheight=0.031)
tdxml = Entry(window)
tdxml.place(relx=0.063, rely=0.2, relwidth=0.46, relheight=0.031)

QMT目录 = Label(
    window,
    text="QMT目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.495, rely=0.2, relwidth=0.07, relheight=0.031)
qmtml = Entry(window)
qmtml.place(relx=0.56, rely=0.2, relwidth=0.43, relheight=0.031)

lb4 = Label(
    window,
    text="tdx目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.01, rely=0.24, relwidth=0.05, relheight=0.031)
inp4 = Entry(window)
inp4.place(relx=0.063, rely=0.24, relwidth=0.46, relheight=0.031)

lb5 = Label(
    window,
    text="QMT目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.495, rely=0.24, relwidth=0.07, relheight=0.031)
inp5 = Entry(window)
inp5.place(relx=0.56, rely=0.24, relwidth=0.43, relheight=0.031)

lb6 = Label(
    window,
    text="tdx目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.01, rely=0.28, relwidth=0.05, relheight=0.031)
inp6 = Entry(window)
inp6.place(relx=0.063, rely=0.28, relwidth=0.46, relheight=0.031)

lb7 = Label(
    window,
    text="QMT目录",
    # bg="#d3fbfb",
    font=("宋体", 12),
    width=12,
    height=2,
    # relief=SUNKEN,
).place(relx=0.495, rely=0.28, relwidth=0.07, relheight=0.031)
inp7 = Entry(window)
inp7.place(relx=0.56, rely=0.28, relwidth=0.43, relheight=0.031)

# 方法-直接调用 run1()
btn1 = Button(window, text="方法一", command=run1)
btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)

# 方法二利用 lambda 传参数调用run2()
btn2 = Button(window, text="方法二", command=lambda: run2(tdxml.get(), qmtml.get()))
btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
txt = Text(window)
txt.place(rely=0.55, relwidth=0.9, relheight=0.3)
window.mainloop()
