
def array_diff(a, b):
    b_set = set(b)
    result = [item for item in a if item not in b_set]
    return result
