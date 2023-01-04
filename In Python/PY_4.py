# Prints all odd numbers within a given range
print("Prints all odd numbers within a given range")

lowerLimit = int(input("Enter lower limit: "))
upperLimit = int(input("Enter upper limit: "))

print("Printing all odd numbers within the given range")

for i in range(lowerLimit, upperLimit+1):
    if(i%2 != 0):
        print(i)