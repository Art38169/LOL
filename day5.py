import random

N = 2

A = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(random.randint(1, 5))
    A.append(row)

real_sol = [random.randint(1, 5) for i in range(N)]


b = [0, 0]
b[0] = A[0][0] * real_sol[0] + A[0][1] * real_sol[1]
b[1] = A[1][0] * real_sol[0] + A[1][1] * real_sol[1]

    


print(f"Matrix is {A}\nRight hand side is {b}")

solved = False

while not solved:
    x = []
    for i in range(N):
        x.append(float(input(f"Enter the x[{i}]: ")))
    print(f"You append the solution: {x}")
    test1 = A[0][0] * x[0] + A[0][1] * x[1]
    test2 = A[1][0] * x[0] + A[1][1] * x[1]
        
    if test1 == b[0] and test2 == b[1]:
        print("Correct")
        solved = True
    else:
        print("Incorrect. Try again, the first error is ", test1 - b[0], "the second error is", test2 - b[1])