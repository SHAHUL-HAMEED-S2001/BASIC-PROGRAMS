# Generate all the divisors of a given number
print("Generate all the divisors of a given number")

num = int(input("Enter the number: "))

print("The divisors of " + str(num) + " are: ")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
