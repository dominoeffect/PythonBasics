# def hours2days(intnum):
# 	a = intnum//24
# 	b = intnum-a*24
# 	result_hour = (a,b)
# 	return result_hour
# print(hours2days(25))





def hours2days(input_hours):
    days = input_hours // 24
    hours = input_hours % 24
    return days, hours


