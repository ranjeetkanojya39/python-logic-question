# Write a lambda function to check if a given number is odd./
is_odd = lambda x: x % 2 != 0
# Test the lambda function
number = 4
if is_odd(number):
    print(f"{number} is an odd number.")        
else:
    print(f"{number} is not an odd number.")