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

# 思路：
# 1.每个号码只统计一次，那么就直接对list使用set()函数去重
# 2.新建一个函数，通过for循环配合列表索引取得号码数据，将说有号码放到一个新的list中，然后在使用set()函数，最后返回即可

# 知识点：set()函数、for循环、列表索引



"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
