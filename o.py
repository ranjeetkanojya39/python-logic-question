# Use a lambda function to square all elements in a list. 
numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
print(squared)