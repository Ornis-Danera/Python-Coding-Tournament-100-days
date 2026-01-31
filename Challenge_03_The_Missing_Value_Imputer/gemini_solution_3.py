def impute_average(data):
    # Calculate non-zero average without extra list storage
    non_zeros = [n for n in data if n != 0]
    avg = round(sum(non_zeros) / len(non_zeros), 2)
    
    # Use a list comprehension for the final output
    return [n if n != 0 else avg for n in data]
