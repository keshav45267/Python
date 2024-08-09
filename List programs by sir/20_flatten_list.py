def flatten_list(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

# Example nested list
nested_list = [1, [2, [3, 4], 5], 6, [7, 8], 9]

# Flatten the nested list
flattened_list = flatten_list(nested_list)

# Print the original and the flattened list
print("Original nested list:", nested_list)
print("Flattened list:", flattened_list)
