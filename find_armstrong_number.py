n = int(input("Enter number to check gor Armstrong :"))
sum =0
temp = n
while temp>0:
    x = temp % 10
    sum +=x*x*x
    temp//= 10
    
if n == sum:
    print("number you enterd is an Armstrong number")
else:
    print("number you entered is not an Armstrong number")
