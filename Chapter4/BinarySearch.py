def BinarySearch(data,target,low=0,high=0):

    if low >= high-1:
        if target == data[low]:
            print("Value Found")
            return True
        else:
            print("Value not Found")
            return False
    else:
        mid = (high+low)//2
        if target == data[mid]:
            print("Value Found")
            return True
        if target > data[mid]:
            test = (data[mid+1:high])
            print(test)
            BinarySearch(data, target, mid+1, high)
        else:
            test = (data[low:mid])
            print(test)
            BinarySearch(data,target, low, mid)




data = [1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18]

BinarySearch(data,1,0, len(data))
#print(z)