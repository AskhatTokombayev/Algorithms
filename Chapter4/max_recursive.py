def max_recursive(S, next = 0):
    if (next == len(data) - 1):
        return (S[next], S[next])
    result_so_far = max_recursive(S, next+1)
    return (max(S[next], result_so_far[0]), min(S[next], result_so_far[1]))


data = [10,2,3,11,5,3,55524,2,1,3,2,32]
Z = max_recursive(data)
print(str(Z))