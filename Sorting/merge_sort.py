import sys
from enterarray import enter_array
from merge_sorted_subarrays import merge

sys.setrecursionlimit(10**6)

def merge_sort_fn(arr, l, r):
    if l >= r:
        return arr
    
    mid = l + (r - l + 1)//2

    arr = merge_sort_fn(arr, l, mid-1)
    arr = merge_sort_fn(arr, mid, r)

    return merge(arr, l, mid, r)

if __name__ == '__main__':

    arr = enter_array()
    n = len(arr)
    print(merge_sort_fn(arr, 0, n-1))