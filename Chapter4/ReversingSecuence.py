def ReverseSequence(S, start, stop):
    #print(S)
    if start+1 < stop:
        S[start], S[stop-1] = S[stop-1], S[start]
        ReverseSequence(S,start+1,stop-1)
    return S



sequence = [1,2,3,4,5,6,7,8,9]
reverse = ReverseSequence(sequence, 0, len(sequence))
print(reverse)