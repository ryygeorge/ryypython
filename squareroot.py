from math import sqrt

while True:
    num = float(input("Enter a number: "))

    if num < 0:
        print("Enter a positive number")
    else:
        print("Square root of", num, "is", sqrt(num))
        break
