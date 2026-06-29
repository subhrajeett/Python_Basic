n = 4334
num = n
reverse =0
while num>0:
    last_digit = num%10
    num=num//10
    reverse = reverse * 10 + last_digit
if(n==reverse):
    print("Palindrome")
else:
    print("Not Palindrome")