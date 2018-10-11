#coding:utf-8
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
    
def first_re():
	list_one = texts[1]
	massage_one = "First record of texts, {} texts {} at time {}".format(list_one[0],list_one[1],list_one[2])
	return massage_one

def last_re():
    list_two = calls[-1]
    massage_two = "Last record of calls, {} calls {} at time {}, lasting {} seconds".format(list_two[0],list_two[1],list_two[2],list_two[3])
    return massage_two

print(first_re() +"\n"+ last_re())

"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

