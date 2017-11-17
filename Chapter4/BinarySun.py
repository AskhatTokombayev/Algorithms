def BinarySum(S, low, high):

    if low == high-1:
        return S[low]
    elif low == high - 2:
        return S[low] + S[high-1]
    else:
        mid = (high+low)//2
        test1 = S[low:mid]
        print(test1)
        test2  = S[mid:high]
        print(test2)
        return BinarySum(S,low,mid) + BinarySum(S, mid, high)





S = [52,12,4321,-4321,-12]
Z = BinarySum(S, 0, len(S))
print(Z)