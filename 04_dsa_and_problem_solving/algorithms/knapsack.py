def knapspack_backtracking(w, weights, values):
    n = len(weights)
    best_val =  -1
    bestX = [0] * n
    x = [0] * n
    def backtracking(i, curr_w, curr_v):
        nonlocal best_val, bestX
        if i == n:
            if curr_v > best_val:
                best_val = curr_v
                bestX = x[:]
            return
        
        x[i] = 0
        backtracking(i+1, curr_w, curr_v)
        if curr_w + weights[i] <= w:
            x[i] = 1
            backtracking(i+1, curr_w + weights[i], curr_v + values[i])
    backtracking(0,0,0)
    print(best_val)
    print(*bestX)
a, b = map(int,input().split())
c = [0] *a
d = [0] *a
for i in range(a):
    c[i], d[i] = map(int,input().split())
knapspack_backtracking(b,c,d)