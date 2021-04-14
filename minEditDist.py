# https://www.geeksforgeeks.org/edit-distance-and-lcs-longest-common-subsequence/
# Edit Distance using Longest Common Subsequence method
def edit_distance(X, Y):
    m = len(X)
    n = len(Y)
    L = [[0 for x in range(n + 1)]
            for y in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                L[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    lcs = L[m][n]

    return (m - lcs) + (n - lcs)

# Given two phrases, find the minmum edit distance between all words
def min_edit_distance(phrase1, phrase2):
    words1 = phrase1.upper().split()
    words2 = phrase2.upper().split()
    min_dist = float('inf')

    for w1 in words1:
        for w2 in words2:
            dist = edit_distance(w1, w2)
            min_dist = min(min_dist, dist)
    return min_dist

# ## Testing
# print(min_edit_distance("LONDON GBR", "LONDON ENG"))
# print(min_edit_distance("LONDON GBR", "LDN"))
# print(min_edit_distance("ASIA", "LDN"))