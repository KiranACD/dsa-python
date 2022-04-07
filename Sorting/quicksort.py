# Implement the randomized quick sort

from enterarray import enter_array
from swap import swap_num

def partition(arr, l, r):

    s = l+1
    e = r

    while (s<=e):
        if arr[s] <= arr[l]:
            s += 1
        elif arr[e] >= arr[l]:
            e -= 1
        else:
            arr[s], arr[e] = swap_num(arr[s], arr[e])
            s += 1
            e -= 1
    
    arr[l], arr[e] = swap_num(arr[l], arr[e])

    return e

def quick_sort(arr, l, r):

    if l >= r:
        return arr
    
    p = partition(arr, l, r)

    arr = quick_sort(arr, l, p-1)
    arr = quick_sort(arr, p+1, r)

    return arr

if __name__ == '__main__':

    arr = enter_array()
    n = len(arr)
    print(quick_sort(arr, 0, n-1))