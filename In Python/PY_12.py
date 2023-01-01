# Prints the smallest divisor of a given number
print("Prints the smallest divisor of a given number")

num = int(input("Enter a number: "))

for i in range(2, num + 1):
    
    if num ==i :
        print("The smallest divisor of the integer is 1")
        break
    if num % i == 0:
        print("The smallest divisor of the integer is ", i)
        break