num_list = [1, 2, 3, 4, 5, 5]
# print(num_list)

for item in num_list[:]:
    if item == 5:
        num_list.remove(item)
    # else:
    #     print(item)

print(num_list)