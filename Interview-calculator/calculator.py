# 分析清楚目标，详情出我们需要用到什么库，先导入函数库
from tkinter import *
import re

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
# def calculator(text):
#     return str(eval(text))

#利用正则表达式拆分s四则运算规则 

def multiply_divide(text):
    if '*' in text:
        ret = float(text.split('*')[0])*float(text.split('*')[1])
    elif '/' in text:
        ret = float(text.split('/')[0])/float(text.split('/')[1])
    return ret

def cal_mul_div(text):
    if '*' not in text and '/' not in text:
        return text
    else:
        text_pre = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', text).group()
        text = text.replace(text_pre, '+' + str(multiply_divide(text_pre))) if len(re.findall(r'-', text_pre)) == 2 else text.replace(text_pre, str(
            multiply_divide(text_pre)))
        return cal_mul_div(text)

def cal_plu_min(text):
    l = re.findall('([\d\.]+|-|\+)',text)
    sum = float(l[0])
    for i in range(1, len(l), 2):
        if l[i] == '+' and l[i + 1] != '-':
            sum += float(l[i + 1])
        elif l[i] == '+' and l[i + 1] == '-':
            sum -= float(l[i + 2])
        elif l[i] == '-' and l[i + 1] == '-':
            sum += float(l[i + 2])
        elif l[i] == '-' and l[i + 1] != '-':
            sum -= float(l[i + 1])
    return sum

def calculator(text):
    text = text.replace('%', '/100')
    return cal_plu_min(cal_mul_div(text))


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
text_res = StringVar()
Entry(root, textvariable=text).pack(expand=YES, fill=BOTH, padx=2, pady=4)
Entry(root, textvariable=text_res).pack(expand=YES, fill=BOTH, padx=2, pady=4)
func = UserInterface(root)
button(func, 'del', lambda t=text: t.set(del_num(t.get())))
button(func, 'reset', lambda t=text: t.set(''))
button(func, '%', lambda t=text: t.set(t.get()+'%'))

for key in ('789/', '456*', '123-', '0.=+'):
    num_sin = UserInterface(root)
    for char in key:
        if char == '=':
            button(num_sin, char, lambda t=text, tr=text_res: tr.set(calculator(t.get())))
        else:
            button(num_sin, char, lambda t=text, c=char: t.set(t.get()+c))

root.mainloop()