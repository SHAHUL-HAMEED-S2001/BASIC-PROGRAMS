# Print all integers that are divisible by 7 and Multiple of 5 within a given range
print("All integers that are divisible by 7 and Multiple of 5 within a given range")

lowerLimit = int(input("Enter lower limit: "))
upperLimit = int(input("Enter upper limit: "))

print("Integers that are divisible by 7 and Multiple of 5:")
for i in range(lowerLimit, upperLimit+1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i)