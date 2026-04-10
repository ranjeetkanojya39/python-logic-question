# wap to reverse a number  using loop 

num = 1234
reverse = 0

while num > 0:

    digit = num % 10        # get the last digit of num
    reverse = reverse * 10 + digit     # add the last digit to the reverse number
    num = num // 10 # remove the last digit from num

print(f"The reverse of the number is {reverse}")

#using for loop

# num = 1234
# reverse = 0

# for i in range(len(str(num))):
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10

# print("Reversed number:", reverse)











num = 1234
reverse = 0

while num > 0:
    digit = num % 10
    revers = reverse * 10 + digit 
    num = num // 10 
print(f"The reverse of the number is {reverse}")






