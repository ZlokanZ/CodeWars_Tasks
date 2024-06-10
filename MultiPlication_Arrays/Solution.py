def comp(array1, array2):
    if array1 is None or array2 is None:
        return False

    # Square the elements of array1
    array1_squared = [x * x for x in array1]

    # Sort both arrays to ensure they can be compared directly
    array1_squared.sort()
    array2.sort()

    # Check if the sorted squared array1 equals the sorted array2
    return array1_squared == array2