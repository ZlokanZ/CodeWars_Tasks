def duplicate_encode(word):
    word = word.lower()
    solution = list(word)
    index = []

    for i in word:
        sum = 0
        index = []
        for j in range(len(word)):
            if i.lower() == word[j]:
                sum+=1
                index.append(j)

        for j in index:
            if sum > 1:
                solution[j] = ")"
            elif sum == 1:
                solution[j] = "("
    solution = "".join(solution)
    return solution