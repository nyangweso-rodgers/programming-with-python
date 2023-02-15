# while loop

# Exampe
## print even values using a while loop
a = 0
while a <= 20:
    print(a)
    a += 2
    
# Example
## printing same value using a while loop
counter = 1
while counter <= 5:
    print("Rodgers Nyangweso")
    counter += 1
    
# Example
## using a TRUE keyword and a break statement with a while loop
b = 5
while True:
    print(b)
    b -= 1
    if b <= 2:
        break

# Example 4: using continue statement
### Unlike break statement, continue jumps back to the top of the loop, rather than stopping it
c = 0
while True:
    c += 1
    if c == 2:
        print("--------------")
        continue
    if c == 5:
        print("Breaking")
        break
        print(c)
print("Finished")

# Example 6: summing numbers in a list using a while loop
sample_list = [i for i in range(100)]

sum_of_list = 0
k = 0
while k < len(sample_list):
    sum_of_list += k
    k += 1
print(sum_of_list)