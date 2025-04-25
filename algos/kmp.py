def kmp_search(text, pattern):
    comparisons = 0
    positions = []

    lps = [0] * len(pattern)
    length = 0
    i = 1
    while i < len(pattern):
        comparisons += 1
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    i = j = 0
    while i < len(text):
        comparisons += 1
        if pattern[j] == text[i]:
            i += 1
            j += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
        if j == len(pattern):
            positions.append(i - j)
            j = lps[j - 1]

    return positions, comparisons
