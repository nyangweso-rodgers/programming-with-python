# i is inialized as 1

i = 1
while i <= 100:
    # output initialied to an empty string
    output = ""
    if i % 3 == 0 and i % 5 == 0:
        output = 'FizzBuzz'
    # if i is divisible by 3, output the variable Fizz
    elif i % 3 == 0:
        output = 'Fizz'
    # if i is divisible by 5, out variable is Buzz
    elif i % 5 == 0:
        output = 'Buzz'
    # if output is "", a blank string, output = i
    elif output == "":
        output = i
    # increment i
    print(output)
    i += 1