# 分析清楚目标，详情出我们需要用到什么库，先导入函数库
from tkinter import *

# 通过逻辑思维分析项目逻辑流程，抽象出函数并定义，定义函数之前的思考过程是最重要的

#使用Tkinter中的Frame组件，在屏幕上显示一个矩形区域，将用来作为容器
def UserInterface(master):
    cal = Frame(master)
    cal.pack(side=TOP, expand=YES, fill=BOTH)
    return cal

#快速缺省创建计算器按钮
def button(master, text, command):    
    cal = Button(master, text=text, command=command, width=6)
    cal.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return cal

# 增加计算机主要功能,巧妙利用内置函数
def calculator(text):
    return str(eval(text))

#我们开始补充计算机功能！删除按键
def del_num(text):
    if len(text) > 0:
        return text[:-1]
    else:
        return text

# 开始构建界面
root = Tk()
main_menu = Menu()
root.title("SimpleCalculator")

text = StringVar()
Entry(root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)
func = UserInterface(root)
button(func, 'del', lambda t=text: t.set(del_num(t.get())))
button(func, 'reset', lambda t=text: t.set(''))

for key in ('789/', '456*', '123-', '0.=+'):
    num_sin = UserInterface(root)
    for char in key:
        if char == '=':
            button(num_sin, char, lambda t=text: t.set(calculator(t.get())))
        else:
            button(num_sin, char, lambda t=text, c=char: t.set(t.get()+c))

root.mainloop()