# First draft
def impute_average(data):
    new_list = []
    avg_list = []
    for num in data: 
        if num == 0:
            continue
        else:
            avg_list.append(num)
    avg = sum(avg_list)/len(avg_list)
    for item in data:
        if item == 0:
            new_list.append(avg)
        else:
            new_list.append(item)
    return new_list
    

# Second draft
def impute_average(data):
    avg = sum(data)/len(data)
    return [avg if num == 0 else num for num in data ]
