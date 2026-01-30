def filter_outliers(numbers, threshold):
    new_list = []
    for num in numbers: 
        if num <= threshold:
             new_list.append(num)
    return new_list
