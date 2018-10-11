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

def count_num():
    phone_num_list_one = []
    for phone_num_one in texts:
        phone_num_list_one.append(phone_num_one[0])
        phone_num_list_one.append(phone_num_one[1])
    phone_num_list_two = []
    for phone_num_two in calls:
        phone_num_list_two.append(phone_num_two[0])
        phone_num_list_two.append(phone_num_two[1])
    message = "There are {} different telephone numbers in the records.".format(len(set(phone_num_list_one+phone_num_list_two)))
    return message

print (count_num())

"""
任务1：
短信和通话记录中一共有多少电话号码？每个号码只统计一次。
输出信息：
"There are <count> different telephone numbers in the records."""
