from collections import Counter


def arrayManipulation(n, queries):
    c = Counter()
    for a, b, k in queries:
        c[a] += k
        c[b+1] -= k
    arrSum = 0
    maxSum = 0
    for i in sorted(c)[:-1]:
        arrSum += c[i]
        maxSum = max(maxSum,arrSum)
    return maxSum


n, m = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(m)]
print(arrayManipulation(n, queries))