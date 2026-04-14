# Write a function to check if a string is a palindrome.


def is_palindrome(s):
    s = s.lower().replace(" ", "")  # optional: ignore case and spaces
    return s == s[::-1]

print(is_palindrome("madam"))        # True
print(is_palindrome("racecar"))      # True
print(is_palindrome("hello"))        # False
print(is_palindrome("A man a plan a canal Panama"))


