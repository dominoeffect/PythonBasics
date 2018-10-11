countryList = ['Angola','Maldives','India','United States','India','Maldives','India']

# countryList1 = set(countryList)

# print (countryList1) 

# countryList.remove('India')

# print (countryList)


# longList = countryList
# current_obj = 'India'
# for current_obj in longList[:]:
# 	if current_obj == 'India':
# 		longList.remove(current_obj)
# print (longList)






# def remove_duplicates(longList):
# 	"""
# 	去除列表中的重复项并把原列表变为空
# 	"""
# 	newlist = []
# 	for index in range(len(longList)):
# 		# count = 0
# 		if  longList[index] in longList[index+1:]:
# 			newlist.append(longList[index])
# 			current_obj = longList[index]
# 			for current_obj in longList[:]:
# 				if current_obj in longList:
# 					longList.remove(current_obj)


# 		else:
# 			newlist.append(longList[index])
# 		print (newlist)
# 	return newlist

# remove_duplicates(countryList)





def remove_duplicates(longList):
	"""
	去除列表中的重复项并把原列表变为空
	"""
	newlist = []
	for index in range(len(longList)):
		if  longList[index] in longList and longList[index] not in newlist:
			newlist.append(longList[index])
	# print (newlist)
	return newlist

print (remove_duplicates(countryList))




def remove_duplicates(source):
    target = []

    for element in source:
        if element not in target:
            target.append(element)

    return target



# def remove_duplicates(longList):
# 	"""
# 	去除列表中的重复项并把原列表变为空
# 	"""
# 	newlist = set(countryList)

# 	newlist = list(newlist)

	
# 	# print (newlist)
# 	return newlist

# print (remove_duplicates(countryList))

