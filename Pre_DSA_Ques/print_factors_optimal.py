from math import sqrt
num = 20
result = []
for i in range(1, int(sqrt(num))+1):#checking till square root of number for better timecomlexity 
    if num % i ==0:
        result.append(i)
        if i != num//i:
            result.append(num//i)
result.sort()
print(result)