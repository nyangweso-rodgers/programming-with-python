digits = int(input("Enter a number: "))

sum = 0

while digits >= 0:
    mod = digits % 10
    sum = sum + mod
    digits = digits % 10
print(sum)