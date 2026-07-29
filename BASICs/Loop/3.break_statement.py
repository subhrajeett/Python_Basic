#break immediately stops the loop and exits it
#even if condition true it exits

#1. print to 5, loop stop
i=1
while i<=10:
    if i==6:
        break
    print(i,end=" ")
    i+=1