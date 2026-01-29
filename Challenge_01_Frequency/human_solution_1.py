def get_frequency(data):
    dic_t = {}
    i = 0
    p = 0
    for item in data:
        if item in dic_t:
            continue
        else:
            while i < len(data):
                if item == data[i]:
                    p += 1
                    dic_t[item] = p
                i += 1
            i = 0
            p = 0

    return dic_t


data = ["apple", "banana", "apple", "cherry", "banana", "apple"]

print(get_frequency(data))
