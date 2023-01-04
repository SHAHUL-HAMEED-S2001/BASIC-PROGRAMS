# Binary equivalent of a given number using Recursion
print("Binary Equivalent of a given number")

Binary=[]

def convert(b):
    if(b==0):
        return
    dig=b%2
    Binary.append(dig)
    convert(b//2)
    
a=int(input("Enter a number: "))
convert(a)
Binary.reverse()

print("Binary equivalent:")
for i in Binary:
    print (i)