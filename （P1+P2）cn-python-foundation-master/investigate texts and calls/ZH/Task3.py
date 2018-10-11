"""
下面的文件将会从csv文件中读取读取短信与电话记录，
你将在以后的课程中了解更多有关读取文件的知识。
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

def output_num():
	f = []
	z = []
	for i in range(len(calls)):
		if calls[i][0][:5] == '(080)':
			f.append(calls[i][1])
	f = list(set(f)) #班加罗尔地区呼出的所有电话（已去重）
	for m in range(len(f)):
		if "(" in f[m]:
			z.append(f[m].split(")")[0][1:])
		if " " in f[m]:
			z.append(f[m][:4])
	z = sorted(list(set(z)))
	print("The numbers called by people in Bangalore have codes:")
	for x in range(len(z)):
		print(z[x])

output_num()

def proportion_ban():
	count_up = 0
	count_down = 0
	proportion_num = 0
	for i in range(len(calls)):
		if calls[i][0][:5] == '(080)' and calls[i][1][:5] =='(080)':
			count_up = count_up + 1
		if calls[i][0][:5] =='(080)':
			count_down = count_down + 1
	proportion_num = count_up/count_down
	message = "{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(proportion_num)
	return message

print(proportion_ban())



"""
任务3:
(080)是班加罗尔的固定电话区号。
固定电话号码包含括号，
所以班加罗尔地区的电话号码的格式为(080)xxxxxxx。

第一部分: 找出被班加罗尔地区的固定电话所拨打的所有电话的区号和移动前缀（代号）。
 - 固定电话以括号内的区号开始。区号的长度不定，但总是以 0 打头。
 - 移动电话没有括号，但数字中间添加了
   一个空格，以增加可读性。一个移动电话的移动前缀指的是他的前四个
   数字，并且以7,8或9开头。
 - 电话促销员的号码没有括号或空格 , 但以140开头。

输出信息:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
代号不能重复，每行打印一条，按字典顺序排序后输出。


第二部分: 由班加罗尔固话打往班加罗尔的电话所占比例是多少？
换句话说，所有由（080）开头的号码拨出的通话中，
打往由（080）开头的号码所占的比例是多少？

输出信息:
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
注意：百分比应包含2位小数。
"""
