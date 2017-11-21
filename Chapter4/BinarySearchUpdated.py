def binary_search(data, target, low = 0, high = 10):

    mid = data[len(data)//2]

    if len(data) != 1:

        if mid == target:
           print("Value Found")
           return True

        elif target > mid:
            data = data[(len(data)//2):]
            low = data[0]
            high = data[-1]
            return binary_search(data, target, low, high)
        else:
            data = data[:len(data)//2]
            low = data[0]
            high = data[-1]
            return binary_search(data, target, low,high)

    elif mid == target:
        print("Value Found")
        return True
    else:
        print("Value not Found")
        return False

data = [1,2,3,5,7,8,9,10]
binary_search(data, 4)