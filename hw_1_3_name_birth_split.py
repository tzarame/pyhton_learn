#debug input
#name_years = 'Taras Shevchenko*1814-03-09-1861-03-10'

#input 
name_years = input()

# split to date and time 
split_result = name_years.split('*')

# date
date = split_result[1]

# date split
date_split = date.split('-')

# years lived calculation
years_lived = int(date_split[3]) - int(date_split[0])

# name
name = split_result [0]

# debug - output date and name
print('----DEBUG INFO----')
print("date: ", date)
print("name: ", name)
print("date_split: ", date_split)
print("years_lived: ", years_lived)

print('------------------')


# output name
print("Імʼя поважного пана: ", name)

# output years lived
print("Скільки пан мав за щастя прожити: ", years_lived)

