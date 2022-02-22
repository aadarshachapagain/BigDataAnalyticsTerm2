
a_list = []
country_list = []
a_file = open("world_cup_champions.txt")
reduced_dict = {}

for line in a_file:
    a_dictionary = {}
    a_line = line.split(",")
    year = (a_line[0])
    country = a_line[1]
    country_list.append(a_line[1])
    a_dictionary[country] = year
    a_list.append(a_dictionary)
print(a_list)
print("country_list:", country_list)
for item in a_list:
    print("item:", item,)

#     print("item:", item.keys())
#     temp_keys = item.keys()
#     print("jj", temp_keys)
#     print("item:", item.values())

#     print("a_list:", a_list)

#     a_dictionary['year'] = year
#     a_dictionary['wins'] = 1

#     a_list.append(a_dictionary)

#     print("a_line_year:", a_line[0])
#     print("a_line_country:", a_line[1])

#     if country not in a_dictionary:
#         a_dictionary[country] = year

#     print("a_line:", a_line[1])
#     for word in a_line:
#         print("word:"+word)

#     for Year, Country, Coach, Captain in line.split(','):
#         print("Year:"+Year)

# Split line into a tuple

# Add tuple values to dictionary

# OUTPUT
