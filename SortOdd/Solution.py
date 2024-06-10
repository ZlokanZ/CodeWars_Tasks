def sort_array(source_array):
    odds = sorted(x for x in source_array if x % 2 != 0)
    odd_iter = iter(odds)

    replace = lambda x: next(odd_iter) if x % 2 != 0 else x
    return list(map(replace, source_array))
