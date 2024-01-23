uni_list = [2, 3, 5, 4, 3, 5, 6]
# uni_list = []

#debug


# counter
dig_count = len(uni_list)
if dig_count == 0:
    print ("First list empty ")
    print ("Second list empty")
else:
    print("Original list:", uni_list)
    print("digits in list", dig_count)

# split in two
    middle_index = dig_count // 2 + 1
    first_half = uni_list[:middle_index]
    second_half = uni_list[middle_index:]

    print("First Half:", first_half)
    print("Second Part:", second_half)