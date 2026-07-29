#lambda Function : single line func for untility 

#calculate square(normal function)
def square_calculate(n):
    return n*n

square = lambda n: n*n
print(square(5))

#return ture if age>18 else false 

# Ternary if else: Single line if else 
is_age = lambda age: "Eligible" if age >=18 else False
print(is_age(19))

