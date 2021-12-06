
# sorting unsorted list function
def selectionSort(my_list):
  for i in range (len(my_list)):
    for j in range(i + 1, len(my_list)):
      if(my_list[i] > (my_list[j])):
        temp = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = temp
        
  return my_list

print(selectionSort([7, 5, 8, 2, 4, 6, 1, 11, 3, 15]))
