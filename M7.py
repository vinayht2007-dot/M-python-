year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
 print(f"{year} is a Leap Year")
else:
 print(f"{year} is Not a Leap Year")

num = int(input("Enter a number: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
 print(f"{num} x {i} = {num * i}")