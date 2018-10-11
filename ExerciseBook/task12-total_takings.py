# monthly_takings = {'January': [54, 63], 'February': [64, 60], 'March': [63, 49],
#                    'April': [57, 42], 'May': [55, 37], 'June': [34, 32],
#                    'July': [69, 41, 32], 'August': [40, 61, 40], 'September': [51, 62],
#                    'October': [34, 58, 45], 'November': [67, 44], 'December': [41, 58]}




# def total_takings(monthly_takings):
# 	income_List = []
# 	income_sum = 0
# 	for i in monthly_takings:
# 		for m in range(len(monthly_takings[i])):
# 			income_List.append(monthly_takings[i][m])
# 	for x in range(len(income_List)):
# 		income_sum = income_sum + income_List[x]
# 	return income_sum

		

# print(total_takings(monthly_takings))









def total_takings(yearly_record):
    #total is used to sum up the monthly takings
    total = 0
    for month in yearly_record.keys():
        #I use the Python function sum to sum up over 
        #all the elements in a list
        total = total + sum(yearly_record[month])
    return total
    