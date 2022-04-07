# Given an array of N size. Swapping of non-consecutive elements not allowed. Sort in ascending order.
from enterarray import enter_array
from swap import swap_num

def swap(a, b):

    a = a

def sort_consec_swap(arr):

    n = len(arr)

    for i in range(n, 1, -1):
        for j in range(1, i):
            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = swap_num(arr[j-1], arr[j])
    
    return arr

if __name__ == '__main__':
    arr = enter_array()
    print(sort_consec_swap(arr))