#input
original_text = input('Введіть слова у розділивши символом "_" ')

#debug
#original_text = "one_two_three"
split_result = original_text.split('_')

#cycle 
cycle_proc = []
for word in split_result:
    cycle_proc.append(word.title())

#concat
joined_result = ''.join(cycle_proc)

#result
print(joined_result)

