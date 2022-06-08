def find_min(l_R):
    val = l_R[0]
    for item in l_R:
        if val[0] > item[0]:
            val = item
    return val


n = 6
d = [0, 10, 20, 30, 40, 50]
p = [0, 9, 1, 5, 2, 4]
q = [3, 1, 5, 2, 4, 3]
C = [["-" for _ in range(n)] for _ in range(n)]
R = [["-" for _ in range(n)] for _ in range(n)]
W = [["-" for _ in range(n)] for _ in range(n)]
for i in range(n):
    W[i][i] = q[i]
    C[i][i] = q[i]
for i in range(n-1):
    W[i][i+1] = W[i][i] + p[i+1] + q[i+1]
    R[i][i+1] = i + 1
    C[i][i+1] = W[i][i+1] + C[i][i] + C[i+1][i+1]

for l in range(2, n):
    for i in range(n-l):
        j = i + l
        W[i][j] = W[i][j-1] + p[j] + q[j]
        l_R = [(C[i][k-1] + C[k][j], k) for k in range(R[i][j-1], R[i+1][j]+1)]
        min = find_min(l_R)
        C[i][j] = W[i][j] + min[0]
        R[i][j] = min[1]
print("\nW:")
for i in range(n):
    for j in range(n):
        print(W[i][j], end='\t')
    print()
print("\nC:")
for i in range(n):
    for j in range(n):
        print(C[i][j], end='\t')
    print()
print()
print("\nR:")
for i in range(n):
    for j in range(n):
        print(R[i][j], end='\t')
    print()

    # l_R = [C[i][k-1] + C[k][j] for k in range(R[i][j-1], R[i+1][j]+1)]
