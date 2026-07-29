#print num divisible by 3 & 4

start = 1
End=100
i =start
while i<=End:
    if i%3==0 and i%4==0:
        print(i,end=" ")
    i+=1