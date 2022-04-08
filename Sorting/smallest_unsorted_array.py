# Given an array, find the smallest subarray, after sorting which in ascending order, 
# the complete array will get sorted in ascending order.

# Approach 1: Sort the array and compare with original array to get s and e of subarray.

# Approach 2:

from enterarray import enter_array

def get_subarray(arr):
    
    n = len(arr)

    small = 10**9
    for _ in range(1, n):
        if arr[_] < arr[_-1]:
            small = min(small, arr[_])

    for _ in range(n):
        if arr[_] > small:
            s = _
            break
    
    big = -10**9
    for _ in range(n-2, -1, -1):
        if arr[_] > arr[_+1]:
            big = max(big, arr[_])
    
    for _ in range(n-1, -1, -1):
        if arr[_] < big:
            e = _
            break
    
    return (s, e)

if __name__ == '__main__':
    
    arr = enter_array()
    print(get_subarray(arr))

