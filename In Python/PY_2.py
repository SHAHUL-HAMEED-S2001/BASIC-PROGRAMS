# Determine whether a given number is even or odd recursively

def checkEven(n):
    if(n<2):
        return (n%2)==0
    return checkEven(n-2)

num = int(input("Enter a number to check whether it is odd or even: "))

if(checkEven(num)):
    print("The given number is even!")
else:
    print("The given number is odd!")
