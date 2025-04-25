def naive_search(text, pattern):
    comparisons = 0
    positions = []

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
        else:
            positions.append(i)

    return positions, comparisons
