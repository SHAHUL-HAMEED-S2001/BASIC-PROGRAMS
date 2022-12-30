# Count the number of digits in a number

num = int(input("Enter a number to Count the number of digits: "))

count = 0
while(num!= 0):
    count += 1
    num = num//10
    
print("Number of digits is:",count)
