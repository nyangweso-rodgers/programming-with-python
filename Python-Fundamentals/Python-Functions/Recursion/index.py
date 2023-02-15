# Recursion Functions

## Example
def even_numbers(e):
    if (e > 0):
        result = e + even_numbers(e - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example")
even_numbers(5)