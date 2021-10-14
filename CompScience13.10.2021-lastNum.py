num = int(input("Enter number "))
print(num % 10)

if (num % 10) % 3 == 0:
    print("Divisible by 3")
else:
    print("Not divisible by 3")