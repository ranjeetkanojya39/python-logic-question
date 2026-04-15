# Write a function that accepts a number and returns its digital root.


def digital_root(n):
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

# Example
print(digital_root(456))  # Output: 6