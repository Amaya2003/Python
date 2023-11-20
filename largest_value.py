largest_number_sofar=-1
print('Before',largest_number_sofar)
for the_num in [9, 41, 12, 74, 3, 15]:
    if largest_number_sofar < the_num:
        largest_number_sofar=the_num
    print(largest_number_sofar,the_num)
print('After',largest_number_sofar)