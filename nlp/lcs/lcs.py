a = 'ABCBDAB'
b = 'BDCABA'

def lcs(a, b):
    n = len(a)
    m = len(b)
    # print(m)
    l = [[0] * (m + 1) for i in range(n + 1)]
    # print(l)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                l[i][j] = l[i - 1][j - 1] + 1
            else:
                l[i][j] = max(l[i - 1][j], l[i][j - 1])
    return l


l = lcs(a, b)
for line in l:
    print(line)
