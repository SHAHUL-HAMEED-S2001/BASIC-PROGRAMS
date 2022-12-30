# Check whether a given number is a palindrome

num = int(input("Enter a number to check whether it is a palindrome: "))

duplicateNumber = num
sum = 0
while(duplicateNumber!= 0):
    rem = duplicateNumber % 10
    sum = (sum*10) + rem
    duplicateNumber = duplicateNumber//10

if(sum == num):
    print("The given number is a palindrome.")
else:
    print("The given number is not a palindrome.")
