# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

def NumberOfDigits(number, num_accuracy):
    count=0
    while (num_accuracy!=1):
        num_accuracy*=10
        count+=1
    return count

number=float(input())
accuracy=float(input())
print(round(number, NumberOfDigits(number,accuracy)))