# The O(n) Approach:
def get_frequency_optimized(data):
    dic_t = {}
    for item in data:
        if item in dic_t:
            dic_t[item] += 1
        else:
            dic_t[item] = 1
    return dic_t
