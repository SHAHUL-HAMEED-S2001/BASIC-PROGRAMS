# The program takes the upper and lower limit and prints all odd numbers within a given range

print("The program takes the upper and lower limit and prints all odd numbers within a given range")

lowerLimit = int(input("Enter lower limit: "))
upperLimit = int(input("Enter upper limit: "))

print("Printing all odd numbers within the given range")

for i in range(lowerLimit, upperLimit+1):
    if(i%2 != 0):
        print(i)