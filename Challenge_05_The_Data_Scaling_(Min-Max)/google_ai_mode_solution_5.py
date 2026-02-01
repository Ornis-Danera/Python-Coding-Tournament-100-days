def min_max_scale_with_avg(data):
    # 1. Standard Min-Max Scaling setup
    max_value = max(data)
    min_value = min(data)
    range_space = max_value - min_value
    
    # 2. Efficiently calculate non-zero sum and count in one pass
    # This avoids extra list storage by using generator expressions
    non_zero_sum = sum(n for n in data if n != 0)
    non_zero_count = sum(1 for n in data if n != 0)
    
    # Handle division by zero if all elements are zero
    non_zero_avg = non_zero_sum / non_zero_count if non_zero_count > 0 else 0
    
    # 3. Perform Scaling
    # If range_space is 0, return original data or zeros to avoid division error
    if range_space == 0:
        return [0.0 for _ in data], non_zero_avg
        
    scaled_data = [(n - min_value) / range_space for n in data]
    
    return scaled_data, non_zero_avg

# Example usage:
# my_data = [10, 0, 30, 0, 50]
# scaled, avg = min_max_scale_with_avg(my_data)
