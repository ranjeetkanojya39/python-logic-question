def remove_duplicates(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique


# Example usage
data = [1, 2, 2, 3, 4, 3, 5]
result = remove_duplicates(data)

print(result)
