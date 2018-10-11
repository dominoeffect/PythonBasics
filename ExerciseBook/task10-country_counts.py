# population = {'Shanghai': 17.8,
#               'Istanbul': 13.3,
#               'Karachi': 13.0,
#               'Mumbai': 12.5}

# print(population['Karachi'])

# >>> elements.get('dilithium')
# None
# >>> elements['dilithium']
# KeyError: 'dilithium'
# >>> elements.get('kryptonite', 'There\'s no such element!')
# "There's no such element!"



from countries import country_list # Note: since the list is so large, it's tidier
                                   # to put in in a separate file. We'll learn more
                                   # about "import" later on.

country_counts = {}
for country in country_list:
    if country not in country_counts:
        country_counts[country] = 1
    else:
    	country_counts[country] = int(country_counts[country]) + 1
    print (country_counts)
    #todo: insert countries into the country_count dict.
    # If the country isn't in the dict already, add it and set the value to 1
    # If the country is in the dict, increment its value by one to keep count


# for country in countries:
#     if country in country_counts:
#         country_counts[country] += 1
#     else:
#         country_counts[country] = 1



# Beatles_Discography = {"Please Please Me": 1963, "With the Beatles": 1963, 
#     "A Hard Day's Night": 1964, "Beatles for Sale": 1964, "Twist and Shout": 1964,
#     "Help": 1965, "Rubber Soul": 1965, "Revolver": 1966,
#     "Sgt. Pepper's Lonely Hearts Club Band": 1967,
#     "Magical Mystery Tour": 1967, "The Beatles": 1968,
#     "Yellow Submarine": 1969 ,'Abbey Road': 1969,
#     "Let It Be": 1970}

# for album_title in Beatles_Discography:
#     print("title: {}, year: {}".format(album_title, Beatles_Discography[album_title]))





