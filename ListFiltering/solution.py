def filter_list(list):
    return [x for x in list if type(x) == int or type(x) == float]

# Better would be : if not isinstance(x, str)
# i didn't know about "isinstance" it checks if variable is given type value

