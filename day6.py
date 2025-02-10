import random

N = 3
A = []

for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1, 5))
    A.append(row)
    
real_sol = [random.randint(1, 5) for i in range(N)]

b = [0 for i in range(N)]

for i in range(N):
    for j in range(N):
        b[i] += A[i][j] * real_sol[j]
        
        
# print(A, real_sol, b)

