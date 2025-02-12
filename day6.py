import random

N = 3

A = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(1/(i+j+1))
    A.append(row)
    
real_sol = [random.randint(1, 5) for i in range(N)]

b = [0 for i in range(N)]

for i in range(N):
    for j in range(N):
        b[i] += A[i][j] * real_sol[j]
        
        
print(A, real_sol, b)

k = []
for i in range(N-1):
    k.append(A[i+1][0] / A[0][0])

for i in range(N-1):
    for j in range(N):
        A[i+1][j] += (-k[i] * A[0][j])
    b[i+1] += (-k[i] * b[0])

print(A)
print(b)
