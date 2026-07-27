#Operator precedense
# **
# *,/,//,%
# +,-
#------------------------------
# - : substract
# * : multipication
# //: floor division
# / : division
# % : modulus
# **: exponent
#------------------------------
a = 13
b = 4 
add = a+b 
print(f"addition: {add}")
sub = a-b
print(f"substract: {sub}")
mult=a*b
print(f"multipication: {mult}")
div =a/b
print(f"division: {div}")
fdiv=a//b
print(f"floorDiv: {fdiv}")
mod=a%b
print(f"modulus: {mod}")
sqr=a**b
print(f"square: {sqr}")
#-----------------------------
#Comparision operator: compare two value returns bool
#==
#!=
#>=
#<=
#>
#<
print(a==b)
print(a!=b)
print(a>=b)
print(a<b)
#-----------------------------
#logical operator
# and
# or
# not
print("comparision and")
print(a>10 and (not b>5))
