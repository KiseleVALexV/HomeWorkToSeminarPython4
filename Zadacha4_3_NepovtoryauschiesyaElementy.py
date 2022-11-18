# Задайте последовательность чисел.
# Напишите программу, которая выведет список
# неповторяющихся элементов исходной последовательности.

# Условия данной задачи читаются "двояко":
# Вариант со списком без дублирующих элементов:

initial_list = [i for i in input().split()]
final_list=[]
for element in initial_list:
    if element not in final_list:
        final_list.append(element)
print(" ".join(str(i) for i in final_list))

# Вариант со списком, где остаются только неповторявшиеся элементы:

def SearchForRepetitions(array, compar_element):
    for i in range(len(array)):
        if array[i]==compar_element:
            return compar_element
    return False

final_alt_list=initial_list
for j in range(len(initial_list)):  
    if initial_list[j]==SearchForRepetitions(initial_list[j+1:],initial_list[j]):
        final_alt_list = list(filter(lambda x: x!= initial_list[j], final_alt_list))

print(" ".join(str(i) for i in final_alt_list))
