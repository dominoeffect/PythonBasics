#TODO: Implement the nearest_square function
def nearest_square(limit):
    list1 = []
    list2 = []
    list3 = []
    for num in range(limit):
        num2 =  num * num
        list2.append(num2)
    # print (list2)
    for index in range(len(list2)):
        count = list2[index]
        if count < limit:
            list3.append(count)

    # print (list3)    
    return max(list3)
    # print (list2[range(len(list2))])
    # while (num2 < limit):
    #     list2.append(num2)
    #     print (list2)
            
        #     list2.append(num2)
        #     # print (list2)
        #     return max(list2)

test1 = nearest_square(40)
print("expected result: 36, actual result: {}".format(test1))
        



# for index in range(len(names)): # iterate over the index numbers of the names list
#     names[index] = names[index].title()







def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2    