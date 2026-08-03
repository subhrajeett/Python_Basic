#len()
#min()
#max()
#sum()
#sorted()
#reversed()

marks=[32,44,56,78,90,12]
print(f"length of list: {len(marks)}")
print(f"minimum value in list: {min(marks)}")
print(f"maximum value in list: {max(marks)}")
print(f"sum of list: {sum(marks)}")
#Sorting in ascending order
print(f"sorted list: {sorted(marks)}")
#Sorting in descending order
print(f"sorted list: {sorted(marks,reverse=True)}")
#Same order ,just reversed
print(f"reversed list: {list(reversed(marks))}")