# n! n x (n-1) x (n - 2) x .....x1
num = int(input("Enter a number: "))
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # use a temporary variable to preserve the original 'num' for printing
    temp  = num 
    while temp > 1:
        factorial *= temp # multiply the current value of temp to factorial
        temp -= 1 # decrement temp by 1
    print(f"The factorial of {num} is {factorial}")