# Sum of digits

num = int(input("Enter number to find sum of digits: "))

sum = 0
while(num!= 0):
    rem = num % 10
    sum = sum + rem
    num = num//10
    
print("Sum of digits is:",sum)
