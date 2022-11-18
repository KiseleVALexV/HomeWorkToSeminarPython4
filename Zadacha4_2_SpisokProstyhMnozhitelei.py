# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.

number=int(input())
pf=2
prime_factors=[]
while (pf<=int(number**(1/2))):
    while (number%pf==0):
        prime_factors.append(pf)
        number/=pf
    pf+=1
if (number!=1):
    prime_factors.append(int(number))
print(" ".join(str(i) for i in prime_factors))