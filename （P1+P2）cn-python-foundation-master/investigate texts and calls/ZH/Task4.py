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

def sells_num():
    pro_phone_num = ""
    pro_List = []    
    callin_List = []

    for index in range(len(calls)):
        callin_List.append(calls[index][1])
    for index in range(len(calls)):
        pro_phone_num = calls[index][0]
        if pro_phone_num not in callin_List and pro_phone_num not in pro_List:
            pro_List.append(pro_phone_num)  #搜集有呼出无接听的电话放入pro_List
    

    phone_num = ""
    text_List = []
    for index in range(len(texts)):
        text_List.append(texts[index][0])
        text_List.append(texts[index][1])

    for index in range(len(text_List)):
        phone_num = text_List[index]    
        if phone_num in pro_List:
            pro_List.remove(phone_num) #移除发送或接收短信的号码在pro_List中
    pro_List = sorted(list(set(pro_List)))
    print("These numbers could be telemarketers: ")
    for index in range(len(pro_List)):
        print(pro_List[index])
sells_num()


"""
任务4:
电话公司希望辨认出可能正在用于进行电话推销的电话号码。
找出所有可能的电话推销员:
这样的电话总是向其他人拨出电话，
但从来不发短信、接收短信或是收到来电


请输出如下内容
"These numbers could be telemarketers: "
<list of numbers>
电话号码不能重复，每行打印一条，按字典顺序排序后输出。
"""

