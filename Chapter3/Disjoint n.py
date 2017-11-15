def disjoint(A,B,C):
    for a in A:
        for b in B:
            if a == b:
                for c in C:
                    if a == c:
                        return False
    return True


A = [4,5,1]
B = [8,2,1,7]
C = [1,9,25]

Flag = disjoint(A,B,C)

print(Flag)