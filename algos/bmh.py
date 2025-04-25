def boyer_moore_horspool(text, pattern):
    comparisons = 0
    positions = []

    m, n = len(pattern), len(text)
    if m > n:
        return positions, comparisons

    skip = {pattern[i]: m - i - 1 for i in range(m - 1)}
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j -= 1
        if j == -1:
            positions.append(i)
            i += 1
        else:
            i += skip.get(text[i + j], m)

    return positions, comparisons
