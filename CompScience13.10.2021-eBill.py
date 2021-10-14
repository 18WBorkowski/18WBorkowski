units = float(input("Enter your electricity bill "))
bill = 0
if (units <= 100):
    print("Your electricity bill is", bill / 100, "Euro")
else:
    if (units < 200):
        units -= 100
        bill = units * 5
        print("Your electricity bill is", bill / 100, "Euro")
    else:
        bill += 500 # 100 units at 5c
        bill += (units - 200) * 10
        print("Your electricity bill is", bill / 100, "Euro")
