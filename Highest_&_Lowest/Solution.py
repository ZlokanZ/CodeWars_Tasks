solution = ""

def high_and_low(numbers):
    numbers = list(map(int, numbers.split()))

    max = numbers[0]
    min = numbers[0]

    for i in range(len(numbers)):
        print(numbers[i])
        if max < numbers[i]:
            max = numbers[i]
        if min > numbers[i]:
            min = numbers[i]

    solution = f"{max} {min}"

    return solution

print(high_and_low("8 3 -5 42 -1 0 8 -9 4 7 4 -4"))