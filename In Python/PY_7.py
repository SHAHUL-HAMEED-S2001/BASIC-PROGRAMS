# Print all integers that aren't divisible by either 2 or 3 within a given range
print("All integers that aren't divisible by either 2 or 3 within a given range")

lowerLimit = int(input("Enter lower limit: "))
upperLimit = int(input("Enter upper limit: "))

print("Integers that aren't divisible by either 2 or 3:")
for i in range(lowerLimit, upperLimit+1):
    if(i % 2 != 0 and i % 3!= 0):
            print(i)

