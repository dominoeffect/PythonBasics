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

# 1.观察以上代码所知，text是一个列表，我们需要知道列表的第一个元素和最后一个元素，就需要用到列表切片，所以重点学习列表切片内容即可
# 2.完整的代码应该是新建一个函数，然后对列表切片，取得第一个和最后一个数据，然后Return输出信息的字符串（建议通过format方法对字符串进行格式化，字符串之间的换行用\n实现）
# 3.最后调用一下函数，就完成项目了

# 知识点：函数、列表、列表切片、format()函数

"""
任务0:
短信记录的第一条记录是什么？通话记录最后一条记录是什么？
输出信息:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

