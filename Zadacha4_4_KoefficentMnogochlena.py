# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def write_file(name_file, str_polynom):
    with open(name_file, 'w') as data:
        data.write(str_polynom)

def create_coefficients(k):
    coefficients = [random.randint(0, 101) for i in range(k+1)]
    return coefficients
    
def create_polynom(coeff):
    array=coeff[::-1]
    note =''
    if k==0:
        note += f'{array[len(array)-1]} - {array[len(array)-1]} = 0'
    else:
        if len(array) < 1:
            note='x = 0'
        else:
           for i in range(len(array)):
                if i != len(array)-1 and array[i] != 0 and i != len(array)-2:
                   note+=f'{array[i]}x^{len(array)-i-1}'
                   if array[i+1] != 0:
                       note+=' + '
                elif i == len(array)-2 and array[i] != 0:
                    note+=f'{array[i]}x'
                    if array[i+1] != 0:
                       note+=' + '
                elif i == len(array)-1 and array[i] != 0:
                    note+=f'{array[i]} = 0'
                elif i == len(array)-1 and array[i] == 0:
                    note+=' = 0'
    return note

k = int(input("Введите натуральную степень k = "))
coefficients = create_coefficients(k)
print(create_polynom(coefficients))
write_file('file.txt', create_polynom(coefficients))