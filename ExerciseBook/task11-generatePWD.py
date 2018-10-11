# Use an import statement at the top
import random

word_file = "words.txt"
word_list = []

#fill up the word_list
with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

# Add your function generate_password here
def generate_password():
	random_num = random.sample(range(len(word_list)),3)

	ran_password = word_list[random_num[0]] + word_list[random_num[1]] + word_list[random_num[2]]
	return ran_password
# It should return a string consisting of three random words 
# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)



# concatenated together without spaces
# def generate_password():
#     return str().join(random.sample(word_list,3))

# test your function
print(generate_password())