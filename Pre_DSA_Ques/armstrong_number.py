n = 169
num = n 
nod=len(str(n))
total=0
while num>0:
    last_digit = num%10
    total += last_digit**3
    num=num//10
if(n==total):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")