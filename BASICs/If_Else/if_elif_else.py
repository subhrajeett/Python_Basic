mark = int(input("Enter Mark: "))
opt_grade = str(input("Chose O or A+:"))
if mark >= 95:
    if opt_grade=="O":
        print("O")
    else:
        print("A+")
elif mark>70:
    print("A")
elif mark>50:
    print("B")
elif mark>30:
    print("C")
else :
    print("Fail")