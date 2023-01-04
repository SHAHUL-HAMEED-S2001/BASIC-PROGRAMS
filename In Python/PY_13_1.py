# Binary equivalent of a given number
print("Binary Equivalent of a given number")

num = int(input("Enter a number: "))

Binary = []
while num > 0:
    bit = num % 2
    Binary.append(bit)
    num = num// 2
    
print("Binary Equivalent of a given number is: ")

len = len(Binary) - 1
while len >= 0:
    print(Binary[len],end=" ")
    len= len-1