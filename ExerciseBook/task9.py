squares = set()

# todo: populate "squares" with the set of all of the integers less 
# than 2000 that are square numbers





# Note: If you want to call the nearest_square function, you must define
# the function on a line before you call it. Feel free to move this code up!
def nearest_square(limit):
    answer = 0
    while (answer+1)**2 < limit:
        answer += 1
    return answer**2


for i in range(2,2000):
	squares.add(nearest_square(i))


print(squares)

#上面的实现方式存在大量的重复计算，对性能会有一定影响




# n = 1
# while n**2 < 2000:
#     squares.add(n**2)
#     n += 1