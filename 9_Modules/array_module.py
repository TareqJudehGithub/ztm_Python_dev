from array import array

"""
array takes less memories and performs faster than a list

"""
my_arr = array('i', [1, 2, 3])

print(type(my_arr))
print(my_arr)
print(my_arr[0])

my_arr.append(4)
print(my_arr)


