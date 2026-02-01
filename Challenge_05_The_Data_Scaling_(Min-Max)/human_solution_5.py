def min_max_scale(data):
    # Calculate non-zero average without extra list storage
    max_value = max(data)
    min_value = min(data)
    range_space = max_value - min_value
    
    # Use a list comprehension for the final output
    return [ (n - min_value)/range_space for n in data]
