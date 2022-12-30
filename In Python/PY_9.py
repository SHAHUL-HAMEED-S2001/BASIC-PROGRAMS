# Sum of Digit of a Number using Recursion

def sum_of_digit(number):
    if(number==0):
        return 0
    return number%10 + sum_of_digit(number//10)
    
num = int(input("Enter a Number to find sum of digits: "))

print("Sum of digits is:",sum_of_digit(num))


