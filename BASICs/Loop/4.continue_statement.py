#continue skips the rest of the current iteration
i=1
while i<=20:
    i+=1
    if i % 2==0:#skip this actual condition
        continue
    print(i,end=" ")
    
