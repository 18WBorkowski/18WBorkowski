days = ["monday", "tuesday", "wednesday",
        "thursday", "friday", "saturday",
        "sunday"]

num = int(input("Enter number from 1 - 7 "))
if (num > 7):
    print("Nope")
else:
    print(days[num - 1])