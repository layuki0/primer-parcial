def binarySerch(arr, targetval):
    left = 0
    right = len(arr) -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr [mid]== targetval:
            return mid
        
        if arr[mid]< targetval:
            left = mid + 1
        else:
            right = mid  -1

    return -1

myArray = []
mytarget = 8

result = binarySerch(myArray,mytarget)


